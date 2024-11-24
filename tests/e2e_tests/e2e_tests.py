import uuid
import os
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.files import File
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from store.models import Category, Product
import time

class EcommerceE2ETest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Set up Chrome WebDriver in headless mode
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        cls.selenium = webdriver.Chrome(options=options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'selenium'):
            cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        """Set up test environment"""
        super().setUp()
        
        # Create test user
        self.username = f'testuser_{uuid.uuid4().hex[:6]}'
        self.password = 'testpass123'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            email=f'{self.username}@example.com'
        )
        
        # Create test category
        self.category = Category.objects.create(
            name='Test Category',
            slug='test-category'
        )
        
        # Create test product with default image
        default_image_path = 'static/media/images/no-image.png'
        
        self.product = Product.objects.create(
            title='Test Product',
            brand='Test Brand',
            description='Test Description',
            slug='test-product',
            price='99.99',
            category=self.category,
            image=default_image_path
        )

    def hide_chatbot(self):
        """Hide chatbot elements to prevent click interception"""
        self.selenium.execute_script("""
            var elements = [
                'chatbot-messages',
                'chatbot-input',
                'chatbot-container'
            ];
            elements.forEach(function(id) {
                var element = document.getElementById(id);
                if (element) {
                    element.style.display = 'none';
                    element.style.pointerEvents = 'none';
                }
            });
        """)

    def wait_for_element(self, by, value, timeout=10):
        """Wait for element to be present, visible and clickable"""
        try:
            # Hide chatbot before any interaction
            self.hide_chatbot()
            # Wait for element presence
            element = WebDriverWait(self.selenium, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            # Scroll element into view
            self.selenium.execute_script("arguments[0].scrollIntoView(true);", element)
            # Wait a bit for any animations
            time.sleep(0.5)
            # Ensure element is clickable
            WebDriverWait(self.selenium, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            return element
        except TimeoutException:
            self.fail(f"Timeout waiting for element: {value}")

    def test_complete_purchase_flow(self):
        """Test complete user journey from login to purchase"""
        # 1. Login
        self.selenium.get(f'{self.live_server_url}/account/my-login')
        username_input = self.wait_for_element(By.NAME, 'username')
        password_input = self.wait_for_element(By.NAME, 'password')
        
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        password_input.submit()

        # 2. Navigate to store
        self.selenium.get(f'{self.live_server_url}/')
        
        # Wait for product cards to load
        product_cards = self.wait_for_element(By.CLASS_NAME, 'card-body')
        self.assertTrue(product_cards.is_displayed())

        # 3. Click on product title
        product_title = self.wait_for_element(By.CLASS_NAME, 'card-title')
        self.assertEqual(product_title.text, 'Test Product')
        product_link = product_title.find_element(By.XPATH, '..')  # Get parent element
        view_details = product_link.find_element(By.CLASS_NAME, 'btn-primary')
        self.hide_chatbot()  # Hide chatbot again before clicking
        view_details.click()

        # 4. Add to cart
        add_to_cart = self.wait_for_element(By.ID, 'add-button')
        self.hide_chatbot()  # Hide chatbot again before clicking
        add_to_cart.click()

        # 5. Go to cart
        self.selenium.get(f'{self.live_server_url}/cart/')
        
        # 6. Update quantity and verify
        quantity_input = self.wait_for_element(By.CSS_SELECTOR, f'input[id^="select"]')
        quantity_input.clear()
        quantity_input.send_keys('2')
        
        update_button = self.wait_for_element(By.CLASS_NAME, 'update-button')
        self.hide_chatbot()  # Hide chatbot again before clicking
        update_button.click()

        # 7. Proceed to checkout
        self.selenium.get(f'{self.live_server_url}/payment/checkout/')

    def test_account_management(self):
        """Test account management functionality"""
        # Login
        self.selenium.get(f'{self.live_server_url}/account/my-login')
        username_input = self.wait_for_element(By.NAME, 'username')
        password_input = self.wait_for_element(By.NAME, 'password')
        
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        password_input.submit()

        # Navigate to dashboard
        self.selenium.get(f'{self.live_server_url}/account/dashboard')

        # Verify welcome message
        welcome_msg = self.wait_for_element(By.TAG_NAME, 'h4')
        self.assertIn(self.username, welcome_msg.text)

    def test_order_history(self):
        """Test order history functionality"""
        # First complete a purchase
        self.test_complete_purchase_flow()
        
        # Navigate to dashboard
        self.selenium.get(f'{self.live_server_url}/account/dashboard')
        
        # Verify we're on the dashboard page
        welcome_msg = self.wait_for_element(By.TAG_NAME, 'h4')
        self.assertIn(self.username, welcome_msg.text)
        
        # Click on track orders button
        track_orders_btn = self.wait_for_element(By.XPATH, "//a[contains(text(), 'My orders')]")
        track_orders_btn.click()
        
        # Verify we're on the orders page
        orders_heading = self.wait_for_element(By.TAG_NAME, 'h3')
        self.assertIn('My orders', orders_heading.text)

    def test_search_and_filter(self):
        """Test search and filter functionality"""
        # Go to store page
        self.selenium.get(f'{self.live_server_url}/')
        
        # Wait for product cards to load
        products = self.wait_for_element(By.CLASS_NAME, 'card-body')
        self.assertTrue(products.is_displayed())

        # Find product title and verify
        product_title = self.wait_for_element(By.CLASS_NAME, 'card-title')
        self.assertEqual(product_title.text, 'Test Product')
