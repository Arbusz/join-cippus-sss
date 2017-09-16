# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    student_ID = models.CharField(max_length=9, null=True, blank=True, verbose_name='学号')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    name = models.CharField(max_length=100, verbose_name='姓名')
    email = models.EmailField(max_length=254, verbose_name='邮箱')

    class Meta(AbstractUser.Meta):
        pass
