from rest_framework.decorators import api_view
from rest_framework.response import Response

# Example: In a real app, fetch from DB
PRODUCTS = [
    {
        "id": 1,
        "name": "Smartphone",
        "price": 499,
        "description": "Latest model smartphone.",
    },
    {
        "id": 2,
        "name": "Sneakers",
        "price": 99,
        "description": "Comfortable running shoes.",
    },
    {
        "id": 3,
        "name": "Coffee Maker",
        "price": 79,
        "description": "Brew the perfect cup every time.",
    },
]


@api_view(["GET"])
def hello(request):
    return Response({"message": "Hello from Django!"})


@api_view(["GET"])
def product_detail(request, pk):
    product = next((p for p in PRODUCTS if p["id"] == pk), None)
    if product:
        return Response(product)
    return Response({"detail": "Not found."}, status=404)
