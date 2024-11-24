# Database Tests Explanation

This document explains the database testing strategy and implementation for our e-commerce platform.

## Test Structure

The database tests are organized into two main test classes:
1. `CategoryModelTest`: Tests for the Category model
2. `ProductModelTest`: Tests for the Product model

## Test Categories

### Category Model Tests
- Basic creation and string representation
- Field validations:
  - Name length (max 250 characters)
  - Slug uniqueness
- URL generation with 'list-category' endpoint

### Product Model Tests
- Basic creation and string representation
- Field validations:
  - Title length (max 250 characters)
  - Brand default value ('un-branded')
  - Optional description field
- Category relationship validation
- URL generation with 'product-info' endpoint

## Test Operations

Each test focuses on a specific aspect of the model:

1. **Creation Tests**
   - Object creation with valid data
   - String representation (__str__ method)
   - Default value handling

2. **Validation Tests**
   - Field length constraints
   - Required vs optional fields
   - Unique constraints (Category slug)
   - Default values (Product brand)

3. **Relationship Tests**
   - Product-to-Category relationship
   - Reverse relationship (Category.product)
   - Null handling for optional relationships

4. **URL Tests**
   - get_absolute_url() method
   - Correct URL pattern names
   - Slug usage in URLs

## Best Practices Implemented

1. **Test Isolation**
   - Independent test methods
   - setUp method for test data
   - Django's TestCase for database handling

2. **Comprehensive Coverage**
   - Valid and invalid scenarios
   - Edge cases (max length, blank fields)
   - Default values
   - Model relationships

3. **Clear Documentation**
   - Descriptive test method names
   - Docstrings for each test
   - Organized test structure

## Testing Approach

1. **Model Integrity**
   - Field constraints
   - Data validation
   - Relationship integrity

2. **Business Logic**
   - URL generation
   - Default values
   - Optional fields

3. **Error Handling**
   - ValidationError for invalid data
   - Length constraints
   - Unique constraints

## Current Test Coverage

1. **Category Model**
   - test_category_creation
   - test_category_name_max_length
   - test_get_absolute_url
   - test_slug_uniqueness

2. **Product Model**
   - test_product_creation
   - test_product_title_max_length
   - test_product_brand_default
   - test_product_category_relationship
   - test_get_absolute_url
   - test_blank_description_allowed
