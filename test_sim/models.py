from django.db import models
from django.contrib.auth.models import User

class TestSim (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    inputs = models.CharField(max_length=1000, null="False")
    csv = models.FileField(upload_to='csv')
