# Simple E-Commerce Website (First Iteration)

## Part 1: Installation and Setup

### 1. Clone the Repository
If you haven't already cloned the repository, run:

```bash
git clone https://github.com/Rolin128/-cs5500-group2-ecommerce-platform
cd -cs5500-group2-ecommerce-platform
```

### 2. Set Up a Virtual Environment

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

### 3. Install Project Dependencies
Install the required packages from requirements.txt:

```bash
pip install -r requirements.txt
```

### 4. Create a Superuser
To access the Django admin panel, create a superuser account:

```bash
python manage.py createsuperuser
```

### 5. Start the Development Server
Run the Django development server: 
This will start the server at http://127.0.0.1:8000/. Open this URL in your browser to view your project.

```bash
python manage.py runserver
```

### 6. Access Admin Panel Visit
http://127.0.0.1:8000/admin and log in with the superuser credentials to access Django’s admin interface.

## Part 2: Running Tests

Our project includes a comprehensive test suite covering frontend, backend, database, and integration tests.

### Running Specific Test Categories
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
