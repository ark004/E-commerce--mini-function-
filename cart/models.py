from django.db import models
from home.models import *

# Create your models here.
class cartlists(models.Model):
    cart_id=models.CharField(max_length=120,unique=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class items(models.Model):
    pdt=models.ForeignKey(prod,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlists,on_delete=models.CASCADE)
    quts=models.IntegerField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.pdt
