from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length = 50, default = "")
    subcategory = models.CharField(max_length = 50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length = 300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")    

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    subject = models.CharField(max_length=100, default="")
    desc = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name

class Order_place(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True ) 
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    delivery_user = models.CharField(max_length=100, default="Will be Updated Soon")
    order_place_date = models.DateField(default=timezone.now())
    status = models.CharField(max_length=100, default="Order Confirmed")


    def __str__(self):
        return self.name

class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.email

'''class  Order_Track(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True ) 
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)'''