from django.contrib import admin
from .models import ProductDetail,ProductImage
# Register your models here.
#we need to register model to show those model(table) in admin template
admin.site.register(ProductDetail)
admin.site.register(ProductImage)
