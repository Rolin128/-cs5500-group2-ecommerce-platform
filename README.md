# Simple E-Commerce Website (First Iteration)

This is the initial version of a basic e-commerce site, designed to showcase essential online shopping functionality. This project serves as a foundational step in developing a full-featured e-commerce platform.

## Project Structure (First Iteration)

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

## Installation and Setup
### 1. Clone the Repository
If you haven't already cloned the repository, run:

```bash
git clone https://github.com/Rolin128/-cs5500-group2-ecommerce-platform
cd -cs5500-group2-ecommerce-platform
```

### 2. Set Up a Virtual Environment
To keep dependencies isolated, create and activate a virtual environment:

```bash
python3 -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate     # On Windows
```

### 3. Install Project Dependencies
Install the required packages from requirements.txt:

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
Set up the database by applying migrations:

```bash
python manage.py migrate
```

### 5. Create a Superuser
To access the Django admin panel, create a superuser account:

```bash
python manage.py createsuperuser
```

### 6. Start the Development Server
Run the Django development server: 
This will start the server at http://127.0.0.1:8000/. Open this URL in your browser to view your project.

```bash
python manage.py runserver
```
### 7. Access Admin Panel Visit
http://127.0.0.1:8000/admin and log in with the superuser credentials to access Django’s admin interface.




