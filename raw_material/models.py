from django.db import models

# Create your models here.
from django.db.models import CASCADE

from chenglei_server.models import BaseModel
from product.models import Standard


class PTA(BaseModel):
    level = models.CharField(default='A', max_length=6, verbose_name="等级")
    standard = models.ForeignKey(Standard, on_delete=CASCADE)
    weight = models.FloatField(null=False, blank=False, verbose_name="净重")
    rough_weight = models.FloatField(null=False, blank=False, verbose_name="毛重")
