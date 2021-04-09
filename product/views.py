from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from .models import ProductDetail,ProductImage
from .serializers import ProductSerializer ,ProductDetailSerializer
from rest_framework.response import Response
import json
from rest_framework import status ,mixins
from rest_framework.permissions import IsAuthenticated ,AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import MultiPartParser, FormParser

#Product view
class ProductCreateApi(APIView):
    # queryset = ProductDetail.objects.all()
    # serializer_class = ProductSerializer
    #permission_classes = (IsSuperUser,)
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    # def get(self,request,id=None):
    #     return self.list(request)
    def post(self,request):


        file_serializer = ProductSerializer(data=request.data)
        files = request.FILES.getlist('images')

        if file_serializer.is_valid():
            data = file_serializer.save()
            print(data.id)
            for f in files:
                ProductImage.objects.create(product=data, image=f)
        return Response(status=status.HTTP_201_CREATED)

    # def delete(self,request):
    #     id=self.request.query_params.get('id')
    #     ProductDetail.objects.get(id=id).delete()
    #     return Response({"message":"Success"})
#
# class ProductCreateApi(generics.CreateAPIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     queryset = ProductDetail.objects.all()
#     serializer_class = ProductSerializer

class ProductApi(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer
    #permission_classes = [IsAuthenticated,]             # <-- And here


class ProductUpdateApi(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ProductDetail.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = [IsAuthenticated,] 

class ProductDeleteApi(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self,request):
        id=self.request.query_params.get('id')
        ProductDetail.objects.get(id=id).delete()
        return Response({"message":"Success"})
