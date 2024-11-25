# Simplista: AI-Enhanced E-Commerce Platform

> A modern, Django-based e-commerce platform featuring AI-powered chatbot assistance, secure payment processing, and real-time inventory management.

## Part 1: Installation and Setup

### 1. Clone the Repository
If you haven't already cloned the repository, run:

```bash
git clone https://github.com/Rolin128/-cs5500-group2-ecommerce-platform
cd -cs5500-group2-ecommerce-platform
```

### 2. Set Up Environment Variables

Create a `.env` file in the root directory with the following content:

```plaintext
OPENAI_API_KEY=your_openai_api_key_here
```

This API key is required for the chatbot functionality. Replace `your_openai_api_key_here` with your actual OpenAI API key.

### 3. Set Up a Virtual Environment

To keep dependencies isolated, follow these steps to create and activate a virtual environment:

1. **Deactivate any existing virtual environment:**

   ```bash
   deactivate
   rm -rf venv
   ```

2. **Create a new virtual environment using Python 3.10:**

   ```bash
   python3.10 -m venv venv
   ```

3. **Activate the virtual environment:**

   - **For macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

   - **For Windows:**

     ```bash
     venv\Scripts\activate
     ```

> **Note**: Ensure you use Python 3.10 specifically, as using a different version may lead to dependency issues. If you don't have Python 3.10 installed, refer to the documentation on how to download and install it.

### 4. Install Project Dependencies
Install the required packages from requirements.txt:

```bash
pip install -r requirements.txt
```

### 5. Create a Superuser
To access the Django admin panel, create a superuser account:

```bash
python manage.py createsuperuser
```

Default superuser credentials for development:
```
Username: test1126
Email: test1126@example.com
Password: H8MrR-Qu&50
```

> **Note**: These credentials are for development purposes only. In a production environment, always use secure, unique credentials.

### 6. Start the Development Server
Run the Django development server: 
This will start the server at http://127.0.0.1:8000/. Open this URL in your browser to view your project.

```bash
python manage.py runserver
```

### 7. Access Admin Panel Visit
http://127.0.0.1:8000/admin and log in with the superuser credentials to access Django’s admin interface.

## Part 2: Testing Guide

Our project includes a comprehensive test suite that ensures reliability across all components. You can run specific test categories or all tests at once.

### Running All Tests
To run the complete test suite:
```bash
python manage.py test tests
```

### Running Specific Test Categories

#### Backend Tests
```bash
python manage.py test tests.backend_tests.backend_tests
```
Tests API endpoints, business logic, and server-side functionality.

#### Frontend Tests
```bash
python manage.py test tests.frontend_tests.frontend_tests
```
Validates UI components, user interactions, and client-side functionality.

#### AI Chatbot Tests
```bash
python manage.py test tests.chatbot_tests.chatbot_tests
```
Ensures proper functioning of the AI-powered customer service chatbot.

#### Database Tests
```bash
python manage.py test tests.database_tests.database_tests
```
Verifies data integrity, model relationships, and database operations.

#### Integration Tests
```bash
python manage.py test tests.integration_tests.integration_tests
```
Tests interactions between different components and services.

#### End-to-End Tests
```bash
python manage.py test tests.e2e_tests.e2e_tests
```
Validates complete user workflows and system functionality.

### Quick Test Commands
For convenience, here are all test commands in a single block:
```bash
# Run backend tests
python manage.py test tests.backend_tests.backend_tests

# Run frontend tests
python manage.py test tests.frontend_tests.frontend_tests

# Run chatbot tests
python manage.py test tests.chatbot_tests.chatbot_tests

# Run database tests
python manage.py test tests.database_tests.database_tests

# Run integration tests
python manage.py test tests.integration_tests.integration_tests

# Run end-to-end tests
python manage.py test tests.e2e_tests.e2e_tests
```

### Test Coverage
To generate a test coverage report:
```bash
coverage run --source='.' manage.py test tests
coverage report
```

For detailed HTML coverage report:
```bash
coverage html
```
Then open `htmlcov/index.html` in your browser.

For more detailed information about our test suite, please refer to `tests/tests_readme.md`.

## Part 3: Project Overview

### 1. Home Page
   - **Purpose**: Creates a strong first impression by displaying key products and providing intuitive navigation.
   - **Key Elements**:
     - Featured product display with images and names.
     - Navigation bar with links to the Product Listing and Shopping Cart pages.
     - Footer with basic site information (optional).

### 2. Product Listing Page
   - **Purpose**: Allows users to browse all available products.
   - **Key Elements**:
     - Displays products in a list or grid format with images, names, and prices.
     - Each product includes an **Add to Cart** button.

### 3. Shopping Cart Page
   - **Purpose**: Summarizes items added to the cart, showing total costs.
   - **Key Elements**:
     - Lists selected items with names and prices.
     - Displays the total price.
     - Simple **Checkout** button (no full checkout process).

### 4. Login/Signup Page (Optional)
   - **Purpose**: Enables user account creation and login. Can be skipped for a basic setup.
   - **Key Elements**:
     - **Login** and **Signup** forms.

### 5. Chatbot
   - **Purpose**: Provides customer support and guidance on the homepage.
   - **Key Elements**:
     - A small chatbot popup, integrated using a basic chatbot framework.
