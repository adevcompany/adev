from django.db import models
from multiselectfield import MultiSelectField
from django.conf import settings

# Create your models here.
# variables 
COLOR=(
        ('#800080','PURPLE'),
        ('#ff0000','RED'),
        ('#008000','GREEN'),
        ('#000000','BLACK'),
        ('#f2f2f2','WHITE')

    )

SIZE=(
        ('S','SMALL'),
        ('M','MEDIUM'),
        ('L','LARGE'),
        ('XL','XLARGE')
    )

class Item(models.Model):
  

    title=models.CharField(max_length=50)
    price=models.IntegerField()
    previous_price=models.IntegerField(blank=True,null=True)
    description=models.TextField()
    image_core=models.ImageField(default=False)
    color_disponnible=MultiSelectField(max_length=100,choices=COLOR)
    size_disponnible=MultiSelectField(max_length=10,choices=SIZE)

    objects=models.Manager()
    def __str__(self):
        return self.title


class Imagedetail(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField(default=False)
    color=models.CharField(max_length=100,choices=COLOR)
    
    
    objects=models.Manager()


class OrderItem(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    size=models.CharField(max_length=10)
    color=models.CharField(max_length=100)
    quantity=models.IntegerField(default=1)

    def __str__(self):
        return self.item.title
    