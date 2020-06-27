from django.db import models


# Create your models here.

class user_information(models.Model):
    name = models.CharField('用户名', max_length=20, primary_key=True)
    password = models.CharField('密码', max_length=20)
    level = models.CharField('权限等级', max_length=10)
