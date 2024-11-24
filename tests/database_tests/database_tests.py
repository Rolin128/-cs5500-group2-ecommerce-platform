from django.test import TestCase
from django.core.exceptions import ValidationError
from django.urls import reverse
from store.models import Category, Product
from decimal import Decimal

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Electronics',
            slug='electronics'
        )

    def test_category_creation(self):
        """Test category creation and string representation"""
        self.assertEqual(str(self.category), 'Electronics')
        self.assertEqual(self.category.slug, 'electronics')

    def test_category_name_max_length(self):
        """Test category name length validation"""
        category = Category(name='a' * 251, slug='test')
        with self.assertRaises(ValidationError):
            category.full_clean()

    def test_get_absolute_url(self):
        """Test category URL generation"""
        expected_url = reverse('list-category', args=[self.category.slug])
        self.assertEqual(self.category.get_absolute_url(), expected_url)

    def test_slug_uniqueness(self):
        """Test that category slugs must be unique"""
        duplicate_category = Category(
            name='Electronics 2',
            slug='electronics'  # Same slug as self.category
        )
        with self.assertRaises(ValidationError):
            duplicate_category.full_clean()

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Electronics',
            slug='electronics'
        )
        self.product = Product.objects.create(
            category=self.category,
            title='Test Product',
            brand='Test Brand',
            description='Test Description',
            slug='test-product',
            price=Decimal('99.99'),
            image='test.jpg'
        )

    def test_product_creation(self):
        """Test basic product creation and string representation"""
        self.assertEqual(str(self.product), 'Test Product')
        self.assertEqual(self.product.brand, 'Test Brand')
        self.assertEqual(self.product.price, Decimal('99.99'))

    def test_product_title_max_length(self):
        """Test product title length validation"""
        product = Product(
            category=self.category,
            title='a' * 251,
            brand='Test',
            slug='test',
            price=Decimal('99.99'),
            image='test.jpg'
        )
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_product_brand_default(self):
        """Test brand field default value"""
        product = Product.objects.create(
            category=self.category,
            title='No Brand Product',
            slug='no-brand',
            price=Decimal('79.99'),
            image='test.jpg'
        )
        self.assertEqual(product.brand, 'un-branded')

    def test_product_category_relationship(self):
        """Test product-category relationship"""
        self.assertEqual(self.product.category, self.category)
        self.assertIn(self.product, self.category.product.all())

    def test_get_absolute_url(self):
        """Test product URL generation"""
        expected_url = reverse('product-info', args=[self.product.slug])
        self.assertEqual(self.product.get_absolute_url(), expected_url)

    def test_blank_description_allowed(self):
        """Test that blank description is allowed"""
        product = Product.objects.create(
            category=self.category,
            title='No Description Product',
            brand='Test Brand',
            slug='no-description',
            price=Decimal('79.99'),
            image='test.jpg',
            description=''
        )
        product.full_clean()  # Should not raise ValidationError
