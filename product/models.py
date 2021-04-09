from django.db import models
from cloudinary.models import CloudinaryField
from datetime import date
#Product detail model
class ProductDetail(models.Model):
    product_name=models.CharField(max_length=100,blank=True)
    product_image_name=models.CharField(max_length=100,blank=True)
    product_image=CloudinaryField('image' ,blank=True)
    last_update=models.DateField(default=date.today)
    def __str__(self):
        return self.product_name

class ProductImage(models.Model):
    product = models.ForeignKey(ProductDetail,on_delete=models.CASCADE ,related_name='product')
    image =  CloudinaryField('image' ,blank=True)
