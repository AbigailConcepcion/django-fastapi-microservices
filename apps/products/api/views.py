from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.services.product_service import ProductService
from .serializers import ProductSerializer

class ProductListCreateAPI(APIView):

    def get(self, request):
        products = ProductService.list_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = ProductService.create_product(serializer.validated_data, request.user)
        return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
