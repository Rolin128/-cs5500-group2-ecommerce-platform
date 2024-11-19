import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from store.models import Product  # 确保 Product 模型定义正确
import logging

# 配置 OpenAI API 密钥
openai.api_key = "apikey"
logger = logging.getLogger(__name__)

@csrf_exempt
def chatbot_recommendations(request):
    if request.method == "POST":
        try:
            # 解析请求体
            data = json.loads(request.body)
            query = data.get("query", "").strip()

            if not query:
                return JsonResponse({"response": "Query cannot be empty."}, status=400)

            # 使用 OpenAI API 理解用户的意图和需求
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a product recommendation assistant. Analyze the user's query to extract semantic details, such as category, brand, price range, and preferences. Return the extracted details in JSON format."},
                        {"role": "user", "content": query},
                    ],
                    max_tokens=150
                )
                # 从 OpenAI 返回的内容中提取用户需求（假设返回 JSON 格式）
                user_intent = response['choices'][0]['message']['content'].strip()
                logger.info(f"OpenAI interpreted intent: {user_intent}")
                semantic_data = json.loads(user_intent)
            except json.JSONDecodeError:
                logger.error("OpenAI response is not valid JSON.")
                return JsonResponse({"response": "Error parsing OpenAI response."}, status=500)
            except Exception as e:
                logger.error(f"OpenAI API error: {e}")
                return JsonResponse({"response": "Error processing user intent with OpenAI."}, status=500)

            # 提取需求细节
            category = semantic_data.get("category", None)
            brand = semantic_data.get("brand", None)
            min_price = semantic_data.get("min_price", None)
            max_price = semantic_data.get("max_price", None)

            logger.info(f"Extracted details - Category: {category}, Brand: {brand}, Min Price: {min_price}, Max Price: {max_price}")

            # 构建数据库查询条件
            filters = {}
            if category:
                filters["title__icontains"] = category  # 模糊匹配商品类别
            if brand:
                filters["brand__icontains"] = brand  # 模糊匹配品牌名称
            if min_price is not None:
                filters["price__gte"] = min_price  # 最低价格
            if max_price is not None:
                filters["price__lte"] = max_price  # 最高价格

            try:
                # 查询数据库
                matching_products = Product.objects.filter(**filters)[:5]

                # 格式化查询结果
                recommendations = [
                    {
                        "title": product.title,
                        "brand": product.brand,
                        "price": str(product.price),
                        "image": product.image.url if product.image else None,
                        "description": product.description
                    }
                    for product in matching_products
                ]

                # 如果没有匹配商品
                if not recommendations:
                    recommendations.append({
                        "title": "No matching products found.",
                        "brand": "",
                        "price": "",
                        "image": "",
                        "description": ""
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
    else:
        return JsonResponse({"response": "Only POST requests are allowed."}, status=405)
