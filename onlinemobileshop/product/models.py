from django.db import models

class Brand(models.Model):
    brand_name=models.CharField(max_length=120,unique=True)
    def __str__(self):
        return self.brand_name

class Mobile(models.Model):
    name=models.CharField(max_length=130,unique=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    ram=models.CharField(max_length=120)
    price=models.IntegerField()
    camera=models.CharField(max_length=120)
    os=models.CharField(max_length=120)
    image=models.ImageField(upload_to='images')
    def __str__(self):
        return self.name

class Order(models.Model):
    personname=models.CharField(max_length=123)
    address = models.CharField(max_length=223)
    pin = models.CharField(max_length=123)
    phone = models.CharField(max_length=123)
    email = models.EmailField(max_length=123)
    productid=models.IntegerField()
    choices=(
        ('orderrecieved','orderrecieved'),
        ('dispatched','dispatched'),
        ('deliverd','deliverd'),


    )
    status=models.CharField(max_length=120,choices=choices,default='orderrecieved')
    user=models.CharField(max_length=150)
    active_status=models.IntegerField(default=1)
    def __str__(self):
        return self.personname