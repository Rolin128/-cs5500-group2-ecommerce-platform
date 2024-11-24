# E2E Tests Documentation

## Quick Start

### Dependencies
```bash
# Install all dependencies including test dependencies
pip install -r requirements.txt

# Note: The following dependencies are included in requirements.txt:
# Core dependencies:
# - django==5.0.1
# - django-crispy-forms==1.14.0
# - pillow==10.1.0

# Test dependencies:
# - selenium==4.15.2
# - webdriver-manager==4.0.1
# - coverage==7.3.2
```

### Running Tests
```bash
# Run all E2E tests
python manage.py test tests.e2e_tests.e2e_tests -v 2

# Run specific test case
python manage.py test tests.e2e_tests.e2e_tests.EcommerceE2ETest.test_complete_purchase_flow -v 2

# Run with coverage
coverage run manage.py test tests.e2e_tests.e2e_tests -v 2
coverage report
```

### Browser Requirements
- Chrome/Chromium browser installed
- ChromeDriver (automatically managed by webdriver-manager)
- Internet connection for first-time ChromeDriver download

## End-to-End Tests Explanation

This document explains the End-to-End (E2E) test suite for our e-commerce platform, which verifies complete user workflows using Selenium WebDriver.

## Test Architecture

### Technology Stack
- Django's `StaticLiveServerTestCase`
- Selenium WebDriver
- Chrome in headless mode
- Python's unittest framework

### Key Components
1. Browser Automation
   - Chrome WebDriver in headless mode
   - Automated UI interactions
   - Real DOM manipulation

2. Test Data Management
   - Dynamic user creation with UUID
   - Test products and categories
   - Isolated test environment

3. Wait Mechanisms
   - Explicit waits for elements
   - Implicit timeout configuration
   - Robust element detection

## Test Categories

### 1. Complete Purchase Flow
`test_complete_purchase_flow()`
- User login
- Store browsing
- Product selection
- Cart management
- Purchase completion

### 2. Search and Filter
`test_search_and_filter()`
- Category navigation
- Product filtering
- Search functionality
- Results verification

### 3. Account Management
`test_account_management()`
- User dashboard access
- Profile information
- Account settings
- Session handling

### 4. Order History
`test_order_history()`
- Order tracking
- Purchase history
- Order details
- Status updates

## Implementation Details

### 1. Setup and Teardown
- WebDriver configuration
- Test data creation
- Environment cleanup
- Resource management

### 2. Helper Methods
- Element waiting utilities
- Common interactions
- Verification helpers
- Error handling

### 3. Test Isolation
- Unique user generation
- Fresh test data
- Independent scenarios
- Clean state management

## Recent Updates

### Chatbot Handling
- Added comprehensive chatbot element handling to prevent click interception
- Implemented `hide_chatbot()` method to hide all chatbot-related elements
- Method handles multiple chatbot elements: messages, input, and container
- Added pointer-events control for better interaction reliability

### Element Interaction Improvements
- Enhanced `wait_for_element()` method with better element visibility handling
- Added scroll into view functionality for better element accessibility
- Implemented small animation delay for more reliable interactions
- Added multiple element presence and clickability checks

### Test Case Refinements
1. Order History Test
   - Updated to match actual UI structure
   - Added navigation through dashboard to orders page
   - Improved element selection using correct heading tags
   - Added verification of order listing presence

2. General Improvements
   - Better error handling and timeout messages
   - More reliable element selection strategies
   - Enhanced test stability with better wait conditions
   - Improved chatbot interference handling

## Best Practices

1. Reliability
   - Explicit waits
   - Error handling
   - Stable selectors
   - Timeout management

2. Maintainability
   - Modular test cases
   - Reusable components
   - Clear documentation
   - Consistent patterns

3. Performance
   - Headless browser
   - Efficient setup
   - Resource cleanup
   - Parallel execution ready

## Best Practices Implemented

1. **Element Selection**
   - Use of multiple selection strategies (ID, class, XPath)
   - Fallback mechanisms for element location
   - Proper wait conditions before interactions

2. **Test Stability**
   - Chatbot interference prevention
   - Scroll into view before interactions
   - Animation completion waits
   - Proper element state verification

3. **Error Handling**
   - Descriptive timeout messages
   - Proper exception handling
   - Clear test failure messages

4. **Code Organization**
   - Modular helper methods
   - Clear test case structure
   - Comprehensive documentation
   - Maintainable test suite

## Known Issues and Solutions

### Image Not Found Warnings
The following warnings during test execution are expected and don't affect functionality:
```
Not Found: /media/static/media/images/no-image.png
Not Found: /favicon.ico
```
These occur because:
1. Tests run with a clean test database
2. Static files are not served during testing
3. Default images are not required for functional testing

### Broken Pipe Messages
Messages like `Broken pipe from ('127.0.0.1', XXXXX)` are expected when:
- Browser closes after test completion
- Test database connections are properly cleaned up

## Future Improvements

1. **Performance**
   - Optimize wait times
   - Reduce redundant checks
   - Better test isolation

2. **Coverage**
   - Add negative test cases
   - Test edge cases
   - Add more complex user flows

3. **Maintenance**
   - Regular selector updates
   - Documentation updates
   - Performance monitoring
