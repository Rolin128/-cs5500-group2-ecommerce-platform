from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from store.models import Category, Product
from decimal import Decimal
import uuid

class EcommerceIntegrationTest(TestCase):
    def setUp(self):
        """Set up test data"""
        # Create test category
        self.category = Category.objects.create(
            name='Test Category',
            slug='test-category'
        )

        # Create test products
        self.product1 = Product.objects.create(
            title='Test Product 1',
            slug='test-product-1',
            price=Decimal('99.99'),
            description='Test Description 1',
            category=self.category,
            image='test1.jpg'
        )

        self.product2 = Product.objects.create(
            title='Test Product 2',
            slug='test-product-2',
            price=Decimal('49.99'),
            description='Test Description 2',
            category=self.category,
            image='test2.jpg'
        )

    def test_user_login(self):
        """Test user login functionality"""
        # Create a test user with unique username
        username = f'testuser_{uuid.uuid4().hex[:8]}'
        user = User.objects.create_user(
            username=username,
            password='testpass123',
            email=f'{username}@example.com'
        )
        
        # Attempt login
        login_data = {
            'username': username,
            'password': 'testpass123'
        }
        response = self.client.post(reverse('my-login'), login_data)
        
        # Should redirect to store after login
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.endswith(reverse('store')))
        
        # Verify user is logged in
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_product_listing_and_detail(self):
        """Test product listing and detail views"""
        # Test category listing
        response = self.client.get(reverse('list-category', args=[self.category.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product1.title)
        self.assertContains(response, self.product2.title)

        # Test product detail
        response = self.client.get(reverse('product-info', args=[self.product1.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product1.title)
        self.assertContains(response, self.product1.description)

    def test_cart_operations(self):
        """Test shopping cart operations"""
        # Create a test product with slug
        product = Product.objects.create(
            title='Test Cart Product',
            slug='test-cart-product',
            price=Decimal('10.00'),
            description='Test Description',
            category=self.category
        )
        
        # Add to cart
        add_url = reverse('cart-add')
        response = self.client.post(add_url, {
            'action': 'post',
            'product_id': product.id,
            'product_quantity': 1
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'qty': 1, 'exceeded': False})

        # Test cart summary
        response = self.client.get(reverse('cart-summary'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart-summary.html')

    def test_checkout_process(self):
        """Test checkout process"""
        # Create and login test user with unique username
        username = f'testuser_{uuid.uuid4().hex[:8]}'
        user = User.objects.create_user(
            username=username,
            password='testpass123',
            email=f'{username}@example.com'
        )
        self.client.login(username=username, password='testpass123')
        
        # Create a test product with slug
        product = Product.objects.create(
            title='Test Checkout Product',
            slug='test-checkout-product',
            price=Decimal('10.00'),
            description='Test Description',
            category=self.category
        )
        
        # Add product to cart
        add_url = reverse('cart-add')
        self.client.post(add_url, {
            'action': 'post',
            'product_id': product.id,
            'product_quantity': 1
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        
        # Access cart summary
        response = self.client.get(reverse('cart-summary'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart-summary.html')

    def test_user_authentication_required(self):
        """Test authentication requirements for protected views"""
        # Try accessing dashboard without login
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)  # Should redirect to login
        self.assertTrue(response.url.startswith(reverse('my-login')))

        # Login with unique username
        username = f'testuser_{uuid.uuid4().hex[:8]}'
        user = User.objects.create_user(
            username=username,
            password='testpass123',
            email=f'{username}@example.com'
        )
        self.client.login(username=username, password='testpass123')

        # Try accessing dashboard after login
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)  # Should now be accessible
