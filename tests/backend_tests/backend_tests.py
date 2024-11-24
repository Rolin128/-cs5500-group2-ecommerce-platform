from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from store.models import Category, Product
from payment.models import ShippingAddress, Order, OrderItem
from cart.cart import Cart
import json
import os
from unittest.mock import patch, MagicMock

class StoreViewTests(TestCase):
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
        
        # Create a test image
        image_content = b'GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00ccc,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'
        self.test_image = SimpleUploadedFile(
            name='test_image.gif',
            content=image_content,
            content_type='image/gif'
        )
        
        self.product = Product.objects.create(
            category=self.category,
            title='Test Product',
            brand='Test Brand',
            slug='test-product',
            price='9.99',
            description='Test Description',
            image=self.test_image
        )

    def test_store_view(self):
        """Test store view with and without authentication"""
        # Test unauthenticated view
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/store.html')
        self.assertIn('products', response.context)
        self.assertNotIn('recent_items', response.context)

        # Test authenticated view
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('products', response.context)

    def test_category_view(self):
        """Test category listing view"""
        response = self.client.get(f'/search/{self.category.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/list-category.html')
        self.assertEqual(response.context['category'], self.category)

    def test_product_info_view(self):
        """Test product detail view"""
        response = self.client.get(f'/product/{self.product.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/product-info.html')
        self.assertEqual(response.context['product'], self.product)

class CartViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.product = Product.objects.create(
            category=self.category,
            title='Test Product',
            slug='test-product',
            price='9.99',
            description='Test Description'
        )

    def test_cart_add(self):
        """Test adding items to cart"""
        response = self.client.post('/cart/add/', {
            'action': 'post',
            'product_id': self.product.id,
            'product_quantity': 1
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['qty'], 1)
        self.assertIn('exceeded', data)

    def test_cart_delete(self):
        """Test removing items from cart"""
        # First add an item
        self.client.post('/cart/add/', {
            'action': 'post',
            'product_id': self.product.id,
            'product_quantity': 1
        })
        
        # Then delete it
        response = self.client.post('/cart/delete/', {
            'action': 'post',
            'product_id': self.product.id
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['qty'], 0)
        self.assertIn('total', data)

    def test_cart_update(self):
        """Test updating cart quantities"""
        # First add an item
        self.client.post('/cart/add/', {
            'action': 'post',
            'product_id': self.product.id,
            'product_quantity': 1
        })
        
        # Then update its quantity
        response = self.client.post('/cart/update/', {
            'action': 'post',
            'product_id': self.product.id,
            'product_quantity': 2
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['qty'], 2)
        self.assertIn('total', data)

class PaymentViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.product = Product.objects.create(
            category=self.category,
            title='Test Product',
            slug='test-product',
            price='9.99',
            description='Test Description'
        )

    def test_checkout_view_empty_cart(self):
        """Test checkout with empty cart"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/payment/checkout')
        self.assertEqual(response.status_code, 302)

    def test_checkout_view_with_items(self):
        """Test checkout with items in cart"""
        # Add item to cart
        self.client.login(username='testuser', password='testpass123')
        self.client.post('/cart/add/', {
            'action': 'post',
            'product_id': self.product.id,
            'product_quantity': 1
        })
        
        response = self.client.get('/payment/checkout')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'payment/checkout.html')

class ChatbotViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.product = Product.objects.create(
            category=self.category,
            title='Test Product',
            brand='Test Brand',
            slug='test-product',
            price='9.99',
            description='Test Description'
        )

    @patch('openai.OpenAI')
    def test_chatbot_recommendations(self, mock_openai):
        """Test chatbot recommendations"""
        # Mock OpenAI response
        mock_completion = MagicMock()
        mock_completion.choices = [
            MagicMock(message=MagicMock(
                content='{"category": "Test Category", "brand": "Test Brand", "min_price": 0, "max_price": 100}'
            ))
        ]
        mock_openai.return_value.chat.completions.create.return_value = mock_completion

        response = self.client.post('/chatbot/recommendations/', 
            json.dumps({'query': 'Show me products in Test Category'}),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('response', data)
        recommendations = data['response']
        self.assertTrue(len(recommendations) > 0)
        self.assertEqual(recommendations[0]['title'], 'Test Product')
        self.assertEqual(recommendations[0]['brand'], 'Test Brand')

    @patch('openai.OpenAI')
    def test_openai_error_handling(self, mock_openai):
        """Test OpenAI API error handling"""
        mock_openai.return_value.chat.completions.create.side_effect = Exception("OpenAI API Error")

        response = self.client.post('/chatbot/recommendations/', 
            json.dumps({'query': 'Show me products'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 500)
        data = json.loads(response.content)
        self.assertEqual(data['response'], 'Error processing user intent with OpenAI.')

    def test_chatbot_invalid_request(self):
        """Test chatbot with invalid request"""
        # Test GET request
        response = self.client.get('/chatbot/recommendations/')
        self.assertEqual(response.status_code, 405)  # Method not allowed
        
        # Test empty query
        response = self.client.post('/chatbot/recommendations/', 
            json.dumps({'query': ''}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)  # Bad request
        
        # Test invalid JSON
        response = self.client.post('/chatbot/recommendations/', 
            'invalid json',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)  # Bad request
