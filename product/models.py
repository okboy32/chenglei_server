from django.db import models

# Create your models here.
from django.db.models import CASCADE

from chenglei_server.models import BaseModel

class Standard(BaseModel):

    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "规格"
        verbose_name_plural = verbose_name

class Product(BaseModel):

    level = models.CharField(default='A', max_length=6, verbose_name="等级")
    count = models.IntegerField(default=6, verbose_name="只数")
    standard = models.ForeignKey(Standard, on_delete=CASCADE)
    heap = models.IntegerField(null=True, blank=True, verbose_name="堆号")
    weight = models.FloatField(null=False, blank=False, verbose_name="净重")
    rough_weight = models.FloatField(null=False, blank=False, verbose_name="毛重")
    box_weight = models.FloatField(null=False, blank=False, verbose_name="箱重")
    pipe_weight = models.FloatField(null=False, blank=False, verbose_name="管重")
    color = models.CharField(max_length=10, verbose_name="颜色")
    outbound_id = models.CharField(max_length=64, verbose_name="出货编号")

    class Meta:
        verbose_name = "货物"
        verbose_name_plural = verbose_name

