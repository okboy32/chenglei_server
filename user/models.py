from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from chenglei_server.models import BaseModel


class UserProfile(AbstractUser, BaseModel):

    mobile = models.CharField(max_length=11, verbose_name="手机号")
    level = models.IntegerField(default=0)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name


class VerifyCode(BaseModel):

    code = models.CharField(max_length=4, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="手机号")

    class Meta:
        verbose_name = "验证码"
        verbose_name_plural = verbose_name