# Backend Testing Suite

This directory contains tests for the backend components of our e-commerce platform.

## Test Scope

1. **API Endpoint Tests**
   - Product endpoints (CRUD operations)
   - User authentication endpoints
   - Shopping cart operations
   - Order processing
   - Search and filtering
   - Payment processing

2. **Business Logic Tests**
   - Price calculation
   - Discount application
   - Inventory management
   - Order validation
   - User permissions

3. **Data Validation Tests**
   - Input validation
   - Data sanitization
   - Error handling
   - Response formatting

## Testing Tools

- Python unittest framework
- pytest for advanced testing features
- requests library for API testing
- unittest.mock for mocking dependencies

## Test Categories

1. **Unit Tests**
   - Individual function testing
   - Model method testing
   - Utility function testing
   - Validation logic testing

2. **Integration Tests**
   - API endpoint integration
   - Service layer integration
   - External service integration
   - Database interaction

3. **Performance Tests**
   - Response time testing
   - Load testing
   - Concurrent request handling
   - Resource utilization

## Backend Tests Explanation

This document explains the backend testing infrastructure for our Django-based e-commerce platform.

## Test Structure

The backend tests are organized into four main test classes:

### 1. StoreViewTests
Tests the core store functionality:
- `test_store_view`: Tests homepage with and without authentication
  * Verifies product listing
  * Validates template rendering
  * Checks context data
- `test_category_view`: Tests category listing functionality
  * Validates category-specific product display
  * Checks template rendering
- `test_product_info_view`: Tests product detail pages
  * Verifies product information display
  * Validates template usage

Key features:
- Tests both authenticated and unauthenticated states
- Validates context data
- Checks template rendering
- Tests product display logic

### 2. CartViewTests
Tests shopping cart functionality:
- `test_cart_add`: Tests adding items to cart
  * Validates quantity tracking
  * Checks JSON response format
  * Verifies cart state
- `test_cart_delete`: Tests removing items from cart
  * Validates item removal
  * Checks cart quantity updates
- `test_cart_update`: Tests updating cart quantities
  * Verifies quantity constraints
  * Validates total price updates

Key validations:
- Cart item management
- Quantity limits
- Total price calculations
- Session handling

### 3. PaymentViewTests
Tests checkout and payment processing:
- `test_checkout_view_empty_cart`: Tests checkout with empty cart
  * Verifies redirect behavior
  * Validates user authentication
- `test_checkout_view_with_items`: Tests checkout with items
  * Checks shipping form
  * Validates order creation

Key aspects:
- Cart validation
- User authentication checks
- Shipping information handling
- Order processing

### 4. ChatbotViewTests
Tests AI-powered product recommendations:
- `test_chatbot_recommendations`: Tests recommendation functionality
  * Mocks OpenAI API responses
  * Validates product filtering
- `test_chatbot_invalid_request`: Tests error handling
  * Validates request method restrictions
  * Checks input validation

## Test Data Setup

The tests use:
- Mock user accounts
- Test categories and products
- Simulated image files
- Mock OpenAI responses
- Session data for cart testing

## Running the Tests

To run the backend tests:
```bash
python manage.py test tests.backend_tests.backend_tests
```

## Important Notes

1. **Test Independence**
   - Each test is independent
   - Uses setUp/tearDown for test data
   - No shared state between tests

2. **Mock Usage**
   - Images use SimpleUploadedFile
   - OpenAI API is mocked
   - Test data is isolated

3. **Error Handling**
   - Tests cover error scenarios
   - Validates error messages
   - Checks status codes

4. **Response Validation**
   - Verifies HTTP status codes
   - Checks context data
   - Validates JSON responses

## Best Practices

1. **Test Data Management**
   - Create fresh test data in setUp
   - Use appropriate test fixtures
   - Clean up after tests

2. **Error Testing**
   - Test both success and failure cases
   - Validate error messages
   - Check edge cases

3. **Response Checking**
   - Validate status codes
   - Check template usage
   - Verify context data

4. **Security Testing**
   - Test authentication requirements
   - Validate user permissions
   - Check input sanitization

## Backend Tests Documentation

### Overview
The backend test suite (`backend_tests.py`) contains comprehensive tests for core backend functionality including store operations, cart management, payment processing, and chatbot features.

### Test Categories

#### 1. Store View Tests (`StoreViewTests`)
Tests the basic store functionality and views:
- Store homepage view (authenticated and unauthenticated)
- Category listing functionality
- Product detail views
- Template rendering
- Context data validation

#### 2. Cart View Tests (`CartViewTests`)
Validates shopping cart operations:
- Adding items to cart
- Removing items from cart
- Quantity updates
- Cart total calculations
- Session management

#### 3. Payment View Tests (`PaymentViewTests`)
Tests the checkout process:
- Empty cart handling
- Checkout with items
- Order creation
- Shipping address validation

#### 4. Chatbot View Tests (`ChatbotViewTests`)
Tests the AI-powered chatbot functionality:
- Product recommendations
- OpenAI API integration
- Error handling
- Invalid request handling

### Test Coverage

#### Store Views
- Homepage rendering 
- Category filtering 
- Product details 
- Authentication states 
- Context data 

#### Cart Operations
- Add to cart 
- Remove from cart 
- Update quantities 
- Cart calculations 
- Session persistence 

#### Payment Processing
- Checkout flow 
- Order creation 
- Empty cart handling 
- Address validation 

#### Chatbot Features
- AI recommendations 
- Error handling 
- Request validation 
- OpenAI integration 

### Setup Requirements
- Django TestCase framework
- Mock objects for OpenAI API
- Test database configuration
- Sample product and user data

### Common Issues and Solutions
1. **OpenAI API Mocking**
   - Use `unittest.mock` for API calls
   - Handle potential API errors
   - Mock response formats

2. **Database State**
   - Clean up after tests
   - Use `setUp` and `tearDown`
   - Isolate test data

3. **Authentication**
   - Test both authenticated and anonymous users
   - Verify session handling
   - Check permission levels
