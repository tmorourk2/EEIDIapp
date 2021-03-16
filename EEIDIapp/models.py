from django.conf import settings
from django.db import models
from django.utils import timezone


##used by all lookup tables
class LkupCommonInfo(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    sortOrder = models.IntegerField(default=0)
    archive = models.BooleanField(default=False)
    class Meta:
        abstract=True

### training models
class Role(LkupCommonInfo):
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["sortOrder"]
        verbose_name_plural = "lkupRole"