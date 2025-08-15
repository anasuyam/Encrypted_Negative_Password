# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class reg_tb(models.Model):
    name=models.CharField(max_length=2000)
    email=models.CharField(max_length=2000)
    address=models.CharField(max_length=2000)
    phone=models.CharField(max_length=2000)
    username=models.CharField(max_length=2000)
    password=models.CharField(max_length=2000)
    
