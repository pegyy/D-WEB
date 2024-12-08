from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Twt(models.Model):

    name = models.TextField(max_length=100 , default="-")
    
    def __str(self):
        return self.name + "|" + str(self.pk)