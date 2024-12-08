from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Dm(models.Model):

    productname = models.TextField(max_length=100 , default="-")
    rate = models.TextField(max_length=100, default="-")
    price = models.TextField(max_length=100, default="-")
    
    # number

    number = models.TextField(max_length=100 , default=0 )

    def __str(self):
        return self.name + "|" + str(self.pk)