# Chatbot Tests Explanation

This document explains the testing infrastructure for our AI-powered product recommendation chatbot.

## Test Structure

The chatbot tests are organized into a single comprehensive test class: `ChatbotRecommendationTests`

### Test Categories

1. **Product Recommendations by Category**
   - `test_product_recommendation_by_category`
   - Tests chatbot's ability to filter products by category
   - Uses `category__name__icontains` for flexible matching
   - Handles "all" and "any" category values

2. **Product Recommendations by Brand**
   - `test_product_recommendation_by_brand`
   - Tests brand-specific product filtering
   - Uses `brand__icontains` for flexible matching
   - Handles "all" and "any" brand values

3. **Price Range Filtering**
   - `test_product_recommendation_by_price_range`
   - Tests price-based product filtering
   - Supports both string format ("under $100") and dictionary format
   - Handles min/max price constraints
   - Safely handles empty price strings

4. **Combined Filtering**
   - `test_product_recommendation_combined_filters`
   - Tests multiple filter combinations (category, brand, price)
   - Validates complex query handling
   - Tests interaction between different filter types

5. **Error Handling**
   - `test_chatbot_invalid_request`: Tests various invalid request scenarios
     * GET requests (405 Method Not Allowed)
     * Empty queries (400 Bad Request)
     * Invalid JSON (400 Bad Request)
   - `test_openai_error_handling`: Tests OpenAI API error handling
     * Simulates OpenAI API failures
     * Verifies error response format
     * Checks status codes (500 Internal Server Error)

## Test Data Setup

The test suite uses:
- Multiple product categories (Electronics, Clothing)
- Various products with different attributes
- Mock OpenAI responses for different query types:
  * Category-based queries
  * Brand-based queries
  * Price range queries (string and dictionary formats)
  * Combined filter queries
- Test products with specific price ranges for filtering tests

## OpenAI Integration

The tests use Python's `unittest.mock` to mock OpenAI API calls:
- Mocks the client instance directly from views module
- Simulates different AI response formats:
  * Basic category/brand responses
  * Price range in string format ("under $X")
  * Price range in dictionary format (min/max)
  * Combined filter responses
- Tests error handling with OpenAIError

## Running the Tests

### Prerequisites
1. Set up your environment variables in `.env`:
```bash
OPENAI_API_KEY=your_api_key_here
```

2. Run the tests:
```bash
python manage.py test tests.chatbot_tests.chatbot_tests
```

## Important Notes

1. **Environment Setup**
   - OpenAI API key must be set in `.env`
   - Tests will fail without proper environment configuration

2. **Mock Responses**
   - Tests use predefined mock responses
   - Each test case simulates different AI interpretations
   - Response format matches OpenAI's API structure
   - Handles various price range formats

3. **Error Handling**
   - Tests cover various error scenarios:
     * Invalid HTTP methods
     * Empty queries
     * Invalid JSON
     * OpenAI API failures
     * Malformed responses

4. **Test Independence**
   - Each test is self-contained
   - Uses fresh database for each test
   - Mocked external dependencies
   - Independent test data setup

## Best Practices

1. **API Mocking**
   - Mock the OpenAI client directly from views
   - Use realistic response formats
   - Test both success and error scenarios
   - Handle different response structures

2. **Data Validation**
   - Verify response formats
   - Check filter applications
   - Validate price ranges
   - Handle empty/null values

3. **Error Cases**
   - Test invalid inputs
   - Verify error messages
   - Check status codes
   - Test API failures

4. **Price Range Handling**
   - Test string format ("under $X")
   - Test dictionary format (min/max)
   - Handle empty price strings
   - Validate price constraints

5. **Filter Combinations**
   - Test individual filters
   - Test combined filters
   - Handle special values ("all", "any")
   - Verify filter interactions
