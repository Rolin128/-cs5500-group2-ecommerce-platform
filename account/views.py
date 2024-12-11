from django.shortcuts import redirect, render
from .forms import CreateUserForm, LoginForm, UpdateUserForm
from payment.forms import ShippingForm
from payment.models import ShippingAddress
from payment.models import Order, OrderItem
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from . token import user_tokenizer_generate
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.conf import settings
import uuid


from django.contrib.auth.decorators import login_required


from django.contrib import messages




def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # 设置为未激活
            user.save()

            # 生成验证邮件
            current_site = get_current_site(request)
            subject = 'Account Verification Email'
            message = render_to_string('account/registration/email-verification.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': user_tokenizer_generate.make_token(user),
            })

            user.email_user(subject=subject, message=message)
            messages.success(request, 'Your account was created! Please verify your email.')
            return redirect('email-verification-sent')

    else:
        form = CreateUserForm()
    return render(request, 'account/registration/register.html', {'form': form})




def email_verification(request, uidb64, token):

    # uniqueid

    unique_id = force_str(urlsafe_base64_decode(uidb64))

    user = User.objects.get(pk=unique_id)
    
    # Success

    if user and user_tokenizer_generate.check_token(user, token):

        user.is_active = True

        user.save()

        return redirect('email-verification-success')


    # Failed 

    else:
        return redirect('email-verification-failed')


def email_verification_sent(request):
    return render(request, 'account/registration/email-verification-sent.html')


def email_verification_success(request):
    return render(request, 'account/registration/email-verification-success.html')


def email_verification_failed(request):
    return render(request, 'account/registration/email-verification-failed.html')



def my_login(request):
    if request.user.is_authenticated:
        return redirect('store')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Try to authenticate the user
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            
            # Check if there's a next parameter in the URL
            next_url = request.GET.get('next', 'store')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('my-login')
            
    return render(request, 'account/my-login.html')


# logout

def user_logout(request):

    try:

        for key in list(request.session.keys()):

            if key == 'session_key':

                continue

            else:

                del request.session[key]


    except KeyError:

        pass


    messages.success(request, "Logout success")

    return redirect("store")




@login_required(login_url='my-login')
def dashboard(request):


    return render(request, 'account/dashboard.html')




@login_required(login_url='my-login')
def profile_management(request):    

    # Updating our user's username and email

    user_form = UpdateUserForm(instance=request.user)

    if request.method == 'POST':

        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():

            user_form.save()

            messages.info(request, "Update success!")

            return redirect('dashboard')

   

    context = {'user_form':user_form}

    return render(request, 'account/profile-management.html', context=context)




@login_required(login_url='my-login')
def delete_account(request):

    user = User.objects.get(id=request.user.id)

    if request.method == 'POST':

        user.delete()


        messages.error(request, "Account deleted")


        return redirect('store')


    return render(request, 'account/delete-account.html')

def mock_register(request):
    # Only allow mock registration in local development
    if not settings.DEBUG:
        return redirect('register')
    
    # Generate unique username to avoid conflicts
    unique_id = str(uuid.uuid4())[:8]
    username = f'test_user_{unique_id}'
    email = f'{username}@example.com'
    password = 'mockuser123'
    
    # Create mock user
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name='Test',
        last_name='User'
    )
    user.save()
    
    # Set mock user flag in profile
    profile = user.userprofile
    profile.is_mock_user = True
    profile.save()
    
    # Log the user in
    login(request, user)
    
    # Get the next URL from the query parameters
    next_url = request.GET.get('next', 'store')
    return redirect(next_url)

# Shipping view
@login_required(login_url='my-login')
def manage_shipping(request):

    try:

        # Account user with shipment information

        shipping = ShippingAddress.objects.get(user=request.user.id)


    except ShippingAddress.DoesNotExist:

        # Account user with no shipment information

        shipping = None


    form = ShippingForm(instance=shipping)


    if request.method == 'POST':

        form = ShippingForm(request.POST, instance=shipping)

        if form.is_valid():

            # Assign the user FK on the object

            shipping_user = form.save(commit=False)

            # Adding the FK itself

            shipping_user.user = request.user


            shipping_user.save()

            messages.info(request, "Update success!")

            return redirect('dashboard')


    context = {'form':form}

    return render(request, 'account/manage-shipping.html', context=context)





@login_required(login_url='my-login')
def track_orders(request):

    try:

        orders = OrderItem.objects.filter(user=request.user)

        context = {'orders':orders}

        return render(request, 'account/track-orders.html', context=context)

    except:

        return render(request, 'account/track-orders.html')
