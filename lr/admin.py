from django.contrib import admin

from .models import LabDraft, LabTemplate, Element

admin.site.register(LabDraft)
admin.site.register(LabTemplate)
admin.site.register(Element)
