from rest_framework import serializers
from .models import ProductDetail , ProductImage

#Product serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductDetail
        fields='__all__'

#Product serializer
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImage
        fields=('image',)


class ProductDetailSerializer(serializers.ModelSerializer):
    product =ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = ProductDetail
        fields = ('id','product_name','product')

