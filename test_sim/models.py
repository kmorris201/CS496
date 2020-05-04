from django.db import models
from django.contrib.auth.models import User

class TestSim (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    loop_radius = models.FloatField()
    b_zero = models.FloatField()
    f = models.FloatField()
    r = models.FloatField()
    seconds = models.IntegerField()

    csv = models.FileField(upload_to='csv')

class TestSimResource (models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    res_type = models.CharField(max_length=100)
    resource = models.FileField(upload_to='resources')
