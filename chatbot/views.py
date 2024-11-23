import openai
from openai import OpenAI
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from store.models import Product  # Ensure the Product model is correctly defined
import logging

# Configure OpenAI API client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
logger = logging.getLogger(__name__)

@csrf_exempt
def chatbot_recommendations(request):
    if request.method != "POST":
        return JsonResponse({"response": "Only POST requests are allowed."}, status=405)

    try:
        # Parse request body
        data = json.loads(request.body)
        query = data.get("query", "").strip()

        if not query:
            return JsonResponse({"response": "Query cannot be empty."}, status=400)

        # Use OpenAI API to process user intent
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a product recommendation assistant. Analyze the user's query to extract details such as category, brand, price range, and preferences. Return these details in JSON format."},
                    {"role": "user", "content": query},
                ],
                max_tokens=150
            )

            # Extract user intent from OpenAI response
            user_intent = response.choices[0].message.content.strip()
            logger.info(f"OpenAI interpreted intent: {user_intent}")
            semantic_data = json.loads(user_intent)
        except json.JSONDecodeError:
            logger.error("OpenAI response is not valid JSON.")
            return JsonResponse({"response": "Error parsing OpenAI response."}, status=500)
        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            return JsonResponse({"response": "Error processing user intent with OpenAI."}, status=500)

        # Extract user preferences
        category = semantic_data.get("category")
        brand = semantic_data.get("brand")
        min_price = semantic_data.get("min_price")
        max_price = semantic_data.get("max_price")

        logger.info(f"Extracted details - Category: {category}, Brand: {brand}, Min Price: {min_price}, Max Price: {max_price}")

        # Build query filters
        filters = {}
        if category:
            filters["title__icontains"] = category
        if brand:
            filters["brand__icontains"] = brand
        if min_price is not None:
            filters["price__gte"] = min_price
        if max_price is not None:
            filters["price__lte"] = max_price

        try:
            # Query the database
            matching_products = Product.objects.filter(**filters)[:5]

            # Format product recommendations
            recommendations = [
                {
                    "title": product.title,
                    "brand": product.brand,
                    "price": str(product.price),
                    "image": product.image.url if product.image else None,
                    "description": product.description,
                    "url": product.get_absolute_url()  # Add product URL
                }
                for product in matching_products
            ]

            # Handle case with no matching products
            if not recommendations:
                recommendations.append({
                    "title": "No matching products found.",
                    "brand": "",
                    "price": "",
                    "image": None,
                    "description": "",
                    "url": None
                })

            return JsonResponse({"response": recommendations})
        except Exception as e:
            logger.error(f"Database query error: {e}")
            return JsonResponse({"response": "Error fetching product recommendations from the database."}, status=500)

    except json.JSONDecodeError:
        return JsonResponse({"response": "Invalid JSON format in request."}, status=400)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return JsonResponse({"response": "An unexpected error occurred."}, status=500)
