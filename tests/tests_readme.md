# E-Commerce Platform Test Suite

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


### Test Coverage
Our test suite includes 44 tests across different categories:
- Backend Tests: Core functionality tests
- Frontend Tests: UI and template tests
- Integration Tests: Cross-component interaction tests
- E2E Tests: Full user journey tests
- Database Tests: Model and data integrity tests
- Chatbot Tests: AI recommendation system tests

### Common Test Issues
1. **Missing OpenAI API Key**: Ensure your OpenAI API key is set in `.env` for chatbot tests
2. **Static Files**: Some "Not Found" warnings for static files are expected during tests
3. **Database**: Tests use a separate test database, no production data is affected

## Part 3: Test Categories

### 1. Frontend Tests (`/tests/frontend_tests/`)
- Template rendering tests
- View functionality tests
- Form validation tests
- Authentication flow tests
- See `frontend_tests_explanation.md` for details

### 2. Backend Tests (`/tests/backend_tests/`)
- Store functionality tests (authenticated/unauthenticated)
- Cart management (add/update/delete)
- Payment processing (checkout flow)
- Basic error handling
- See `backend_tests_explanation.md` for details

### 3. Chatbot Tests (`/tests/chatbot_tests/`)
- Product recommendation tests
- Natural language processing tests
- OpenAI integration tests
- Error handling tests
- See `chatbot_tests_explanation.md` for details

### 4. Database Tests
Located in `/tests/database_tests/`, these tests verify the integrity and functionality of our database models:

#### Files
- `database_tests.py`: Comprehensive model tests
  - CategoryModelTest: Tests for Category model
  - ProductModelTest: Tests for Product model
- `database_tests_explanation.md`: Detailed testing documentation

#### Coverage Areas
1. Model Creation and Validation
   - Field constraints and validation
   - Default values
   - String representation
   - Unique constraints

2. Relationships
   - Category-Product relationships
   - Reverse relationship access
   - Optional relationship handling

3. URL Generation
   - Absolute URL generation
   - Slug-based URLs
   - URL pattern validation

4. Business Logic
   - Default value handling
   - Optional field behavior
   - Model-specific constraints

#### Key Features
- Independent test methods
- Comprehensive validation
- Clear test organization
- Detailed documentation
- Database cleanup handling

### 5. Integration Tests
Located in `/tests/integration_tests/`, these tests verify the interactions between different components and end-to-end workflows:

#### Files
- `integration_tests.py`: End-to-end test scenarios
  - User authentication flow
  - Product management
  - Shopping cart operations
  - Checkout process
- `integration_tests_explanation.md`: Detailed testing documentation

#### Coverage Areas
1. User Authentication
   - Registration and login
   - Protected views
   - Session management

2. Product Management
   - Category and product views
   - Search functionality
   - Content verification

3. Shopping Cart
   - Cart operations (Add/Update/Delete)
   - Session handling
   - AJAX interactions

4. Checkout Process
   - Cart to checkout flow
   - Price calculations
   - Authentication requirements

#### Key Features
- End-to-end workflow testing
- Component interaction verification
- Session and state management
- HTTP request/response testing
- Authentication flow validation
- Unique user generation using UUID
- Proper product slug handling
- Comprehensive AJAX testing
- Session state validation

## Part 4: Directory Structure

```
tests/
├── frontend_tests/
│   ├── frontend_tests.py           # Frontend test cases
│   └── frontend_tests_explanation.md # Frontend test documentation
├── backend_tests/
│   ├── backend_tests.py            # Backend test cases
│   └── backend_tests_explanation.md # Backend test documentation
├── chatbot_tests/
│   ├── chatbot_tests.py            # Chatbot test cases
│   └── chatbot_tests_explanation.md # Chatbot test documentation
├── database_tests/
│   ├── database_tests.py           # Database test cases
│   └── database_tests_explanation.md # Database test documentation
├── integration_tests/
│   ├── integration_tests.py        # Integration test cases
│   └── integration_tests_explanation.md # Integration test documentation
└── tests_readme.md                 # This file
```

## Part 5: Test Coverage

### Frontend Coverage
- Template rendering
- View responses
- Form validations
- Authentication flows
- Basic cart functionality

### Backend Coverage
- Store views (authenticated/unauthenticated)
- Cart operations (add/update/delete)
- Payment processing (checkout flow)
- Error handling
- Session management
- Template validation
- Context data verification

### Chatbot Coverage
- Product recommendations:
  * Category-based filtering with flexible matching
  * Brand-based filtering with flexible matching
  * Price range filtering (string and dictionary formats)
  * Combined filter handling
- Error handling:
  * Invalid HTTP methods
  * Empty/invalid queries
  * OpenAI API failures
  * Malformed responses
- OpenAI integration:
  * Mock client responses
  * Various response formats
  * Error simulation

### Database Coverage
- Model operations:
  * CRUD operations for all models
  * Field validation and constraints
  * Model relationships
- Data integrity:
  * Transaction management
  * Concurrent operations
  * Race condition handling
- Stock management:
  * Stock updates and validation
  * Concurrent stock modifications
- Cart and order operations:
  * Cart management
  * Order processing
  * Price calculations

### Integration Coverage
- User Authentication: 100%
- Product Management: 100%
- Cart Operations: 100%
- Checkout Process: 100%
- View Access Control: 100%

## Part 6: Best Practices

1. **Test Independence**
   - Each test should be independent
   - Use setUp/tearDown for test data
   - Avoid test interdependencies
   - Clean up after tests

2. **Mock External Services**
   - Mock OpenAI API calls
   - Use SimpleUploadedFile for images
   - Simulate third-party responses
   - Isolate test data

3. **Test Data Management**
   - Create fresh test data in setUp
   - Use appropriate test fixtures
   - Clean up in tearDown
   - Maintain data isolation

4. **Error Handling**
   - Test both success and failure cases
   - Validate error messages
   - Check edge cases
   - Verify status codes

5. **Response Validation**
   - Check HTTP status codes
   - Validate template usage
   - Verify context data
   - Test JSON responses

## Part 7: Important Notes

1. **Environment Setup**
   - OpenAI API key must be set in `.env` file
   - Tests will fail without proper API key
   - Use test database for all tests

2. **Mock Usage**
   - All external API calls are mocked
   - Images use SimpleUploadedFile
   - No actual OpenAI API calls during tests
   - Mock responses match real API format

3. **Test Isolation**
   - Each test suite runs independently
   - Fresh database for each test
   - No shared state between tests
   - Clean test data management

4. **Security Testing**
   - Validate authentication requirements
   - Check user permissions
   - Test input sanitization
   - Verify error handling
