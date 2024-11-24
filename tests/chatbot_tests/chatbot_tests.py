from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from store.models import Category, Product
import json
import os
from unittest.mock import patch, MagicMock
import logging
from decimal import Decimal
import openai

logger = logging.getLogger(__name__)

class ChatbotRecommendationTests(TestCase):
    def setUp(self):
        """Set up test data"""
        self.client = Client()
        
        # Create test categories
        self.category1 = Category.objects.create(name='Electronics', slug='electronics')
        self.category2 = Category.objects.create(name='Clothing', slug='clothing')
        
        # Create test products with prices within the allowed range (max 99.99)
        self.product1 = Product.objects.create(
            category=self.category1,
            title='USB Drive',
            brand='Samsung',
            slug='usb-drive',
            price=Decimal('29.99'),
            description='High-speed USB drive'
        )
        
        self.product2 = Product.objects.create(
            category=self.category1,
            title='Mouse',
            brand='Apple',
            slug='apple-mouse',
            price=Decimal('79.99'),
            description='Wireless mouse'
        )
        
        self.product3 = Product.objects.create(
            category=self.category2,
            title='T-Shirt',
            brand='Nike',
            slug='nike-shirt',
            price=Decimal('19.99'),
            description='Cotton T-shirt'
        )

    @patch('openai.OpenAI')
    def test_product_recommendation_by_category(self, mock_openai):
        """Test product recommendations by category"""
        # Mock OpenAI response for category-based query
        mock_completion = MagicMock()
        mock_completion.choices = [
            MagicMock(message=MagicMock(
                content='{"category": "Electronics", "brand": null, "min_price": null, "max_price": null}'
            ))
        ]
        mock_openai.return_value.chat.completions.create.return_value = mock_completion

        response = self.client.post('/chatbot/recommendations/', 
            json.dumps({'query': 'Show me electronics'}),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('response', data)
        recommendations = data['response']
        self.assertTrue(len(recommendations) > 0)
        self.assertIn('USB Drive', [p['title'] for p in recommendations])
        self.assertIn('Mouse', [p['title'] for p in recommendations])

    @patch('openai.OpenAI')
    def test_product_recommendation_by_brand(self, mock_openai):
        """Test product recommendations by brand"""
        # Mock OpenAI response for brand-based query
        mock_completion = MagicMock()
        mock_completion.choices = [
            MagicMock(message=MagicMock(
                content='{"category": null, "brand": "Samsung", "min_price": null, "max_price": null}'
            ))
        ]
        mock_openai.return_value.chat.completions.create.return_value = mock_completion

        response = self.client.post('/chatbot/recommendations/', 
            json.dumps({'query': 'Show me Samsung products'}),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        recommendations = data['response']
        self.assertTrue(any(p['brand'] == 'Samsung' for p in recommendations))

    @patch('openai.OpenAI')
    def test_product_recommendation_by_price_range(self, mock_openai):
        """Test product recommendations by price range"""
        # Mock OpenAI response
        mock_completion = MagicMock()
        mock_completion.choices = [
            MagicMock(message=MagicMock(
                content='{"price_range": "under $100", "min_price": 0, "max_price": 100}'
            ))
        ]
        mock_openai.return_value.chat.completions.create.return_value = mock_completion

        response = self.client.post('/chatbot/recommendations/', 
            json.dumps({'query': 'Show me products under $100'}),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        recommendations = data['response']
        self.assertTrue(len(recommendations) > 0)
        
        # Skip any recommendations with empty price strings
        prices = [float(p['price']) for p in recommendations if p['price']]
        self.assertTrue(any(price < 100 for price in prices))

    @patch('openai.OpenAI')
    def test_product_recommendation_combined_filters(self, mock_openai):
        """Test product recommendations with multiple filters"""
        # Mock OpenAI response for combined query
        mock_completion = MagicMock()
        mock_completion.choices = [
            MagicMock(message=MagicMock(
                content='{"category": "Electronics", "brand": "Samsung", "min_price": 20, "max_price": 50}'
            ))
        ]
        mock_openai.return_value.chat.completions.create.return_value = mock_completion

        response = self.client.post('/chatbot/recommendations/', 
            json.dumps({'query': 'Show me Samsung electronics between $20 and $50'}),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        recommendations = data['response']
        for product in recommendations:
            if product['title'] != 'No matching products found.':
                self.assertEqual(product['brand'], 'Samsung')
                self.assertGreaterEqual(float(product['price']), 20)
                self.assertLessEqual(float(product['price']), 50)

    def test_invalid_requests(self):
        """Test invalid request handling"""
        # Test GET request
        response = self.client.get('/chatbot/recommendations/')
        self.assertEqual(response.status_code, 405)

        # Test empty query
        response = self.client.post('/chatbot/recommendations/', 
            json.dumps({'query': ''}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

        # Test invalid JSON
        response = self.client.post('/chatbot/recommendations/', 
            'invalid json',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    @patch('chatbot.views.client')
    def test_openai_error_handling(self, mock_client):
        """Test OpenAI API error handling"""
        # Mock the OpenAI API to raise an error
        mock_client.chat.completions.create.side_effect = openai.OpenAIError("OpenAI API Error")

        response = self.client.post('/chatbot/recommendations/', 
            json.dumps({'query': 'Show me products'}),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 500)
        data = json.loads(response.content)
        self.assertEqual(data['response'], 'Error processing user intent with OpenAI.')
