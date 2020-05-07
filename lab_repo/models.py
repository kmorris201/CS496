from django.db import models
from django.contrib.auth.models import User

class Element (models.Model):
    ELEMENT_TYPE_CHOICES = [
            ('header', 'Header'),
            ('text', 'Text'),
            ('blank', 'Blank'),
    ]
    element_type=models.CharField(max_length=100,choices=ELEMENT_TYPE_CHOICES, null="True")
    inches_blank = models.FloatField(null="True")
    text = models.CharField(max_length=10000, null = "True")
    next_element = models.OneToOneField('self', on_delete=models.CASCADE, null = "True")

class LabDraft (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 1000)
    draft = models.FileField(upload_to='lab_repo_drafts')
    next_element = models.OneToOneField(Element, on_delete=models.CASCADE, null="True")
    current = models.BooleanField(default="False")

class LabTemplate (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 1000)
    description = models.CharField(max_length = 10000, null = "True")
    template = models.FileField(upload_to='lab_repo_template')
