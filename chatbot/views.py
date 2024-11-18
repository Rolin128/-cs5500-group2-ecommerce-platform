import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from store.models import Product  # 假设商品信息在 store 应用中

# 配置 OpenAI API 密钥
openai.api_key = "your-openai-api-key"

@csrf_exempt
def chatbot_recommendations(request):
    if request.method == "POST":
        data = json.loads(request.body)
        query = data.get("query", "")

        # 使用 OpenAI 理解用户意图
        try:
            openai_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a product recommendation assistant for an e-commerce platform."},
                    {"role": "user", "content": query}
                ],
                max_tokens=100
            )
            user_intent = openai_response["choices"][0]["message"]["content"]

            # 查询数据库中匹配的商品
            matching_products = Product.objects.filter(title__icontains=query)[:5]
            recommendations = [
                {
                    "title": product.title,
                    "brand": product.brand,
                    "price": str(product.price),
                    "image": product.image
                }
                for product in matching_products
            ]

            if not recommendations:
                recommendations.append({"title": "No matching products found.", "brand": "", "price": "", "image": ""})

            return JsonResponse({"response": recommendations})
        except Exception as e:
            return JsonResponse({"response": "An error occurred while processing your request."})
