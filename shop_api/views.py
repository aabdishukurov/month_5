from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from shop_api.models import Product, Category, Review
from shop_api.serializers import ProductSerializers, CategorySerializers, ReviewSerializers


@api_view(["GET"])
def product_list_api_view(request):
    queryset = Product.objects.all()
    serializer = ProductSerializers(queryset, many=True)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(["GET"])
def product_detail_api_view(request, id):
    try:
        queryset = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializers(queryset)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(["GET"])
def category_list_api_view(request):
    queryset = Category.objects.all()
    serializer = CategorySerializers(queryset, many=True)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(["GET"])
def category_detail_api_view(request, id):
    try:
        queryset = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializers(queryset)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(["GET"])
def review_list_api_view(request):
    queryset = Review.objects.all()
    serializer = ReviewSerializers(queryset, many=True)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(["GET"])
def review_detail_api_view(request, id):
    try:
        queryset = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializers(queryset)
    return Response(serializer.data, status.HTTP_200_OK)
