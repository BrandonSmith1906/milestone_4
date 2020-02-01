from _pydecimal import Decimal

from django.db import models
from django.shortcuts import render

# Create your models here.
from django.db import models


class my_artifact(models.Model):
    # objects = None
    artifact_name = models.CharField(max_length=200)
    artifact_images = models.FileField(default='')
    artifact_description = models.CharField(max_length=400)
    #artifact_price = models.CharField(max_length=10)
    #artifact_price = models.CharField(max_length=10)
    artifact_price = models.DecimalField(max_digits=10,
                                        decimal_places=2,
                                        verbose_name='Price',
                                        blank=True,
                                        default=0)
    #artifact_price = models.CharField(max_length=10)


    def __str__(self):
        return self.artifact_name


# Create your models here.
