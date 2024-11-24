from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.files.uploadedfile import SimpleUploadedFile
from account.forms import CreateUserForm, LoginForm, UpdateUserForm
from store.models import Category, Product
import os

class TemplateTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        # Create test category and product
        self.category = Category.objects.create(
            name='Test Category',
            slug='test-category'
        )
        
        # Create a test image file
        image_content = b'GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00ccc,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'
        self.test_image = SimpleUploadedFile(
            name='test_image.gif',
            content=image_content,
            content_type='image/gif'
        )
        
        self.product = Product.objects.create(
            category=self.category,
            title='Test Product',
            slug='test-product',
            price='9.99',
            description='Test Description',
            image=self.test_image
        )

    def test_home_page_template(self):
        """Test if homepage template renders correctly"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/store.html')
        self.assertTemplateUsed(response, 'store/base.html')

    def test_product_info_template(self):
        """Test product info template"""
        response = self.client.get(f'/product/{self.product.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/product-info.html')

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_login_view(self):
        """Test login functionality"""
        response = self.client.post('/account/my-login', {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after login
        self.assertTrue(response.url.startswith('/'))

    def test_register_view(self):
        """Test registration functionality"""
        response = self.client.get('/account/register')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/registration/register.html')

class FormTests(TestCase):
    def test_user_registration_form(self):
        """Test user registration form validation"""
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpass123',
            'password2': 'newpass123'
        }
        form = CreateUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_update_form(self):
        """Test user update form validation"""
        form_data = {
            'username': 'updateduser',
            'email': 'updated@example.com'
        }
        form = UpdateUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form(self):
        """Test login form validation"""
        user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        form_data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_cart_access(self):
        """Test cart access with and without authentication"""
        # Test cart access without login (should still work)
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)

        # Test cart access with login
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
