from django.db import models

# Create your models here.

class ReceivedItem(models.Model):
    item_type = models.CharField(max_length=200)
