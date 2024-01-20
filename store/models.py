from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=300);
    product_rate = models.IntegerField();
    product_image = models.ImageField(upload_to='product');


class Popular(models.Model):
    popular_product_name = models.CharField(max_length=300);
    popular_product_rate = models.IntegerField();
    popular_product_image = models.ImageField(upload_to='popular');

class cart_item(models.Model):
    item=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    date=models.DateField(auto_now=True)
    quantity=models.IntegerField(null=True,default=1)
    price=models.FloatField(null=True)
    is_ordered=models.BooleanField(default=False,null=True)
    
    def subtotal(self):
        return self.quantity * self.price
    def __str__(self):
        return f"Item : {self.item.product_name}, Quantity :{self.quantity}, Price : {self.price}, Image :{self.item.product_image}"
    
class cart_Model(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    items=models.ManyToManyField(cart_item)