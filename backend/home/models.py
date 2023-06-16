from django.conf import settings
from django.db import models
class Mithilesh(models.Model):
    'Generated Model'
    studio = models.BigIntegerField()
    data = models.ForeignKey("home.Mithilesh",on_delete=models.CASCADE,null=True,blank=True,related_name="mithilesh_data",)
