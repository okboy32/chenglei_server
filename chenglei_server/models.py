from datetime import datetime

from django.db import models

class BaseModel(models.Model):

    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建世界")
    is_delete = models.IntegerField(default=1, verbose_name="状态")

    class Meta:
        abstract = True