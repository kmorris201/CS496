from django import forms
from .models import LabDraft

class NewDraftForm(forms.Form):
    title = forms.CharField(label='Lab Report Title')

class NewHeaderForm(forms.Form):
    header_text = forms.CharField(label='Section Header')

class NewTextForm(forms.Form):
    text_text = forms.CharField(label='Text', widget=forms.Textarea(attrs={"rows":3, "cols":22}))

class NewBlankForm(forms.Form):
    inches_blank = forms.FloatField(label='Number of Blank Inches')

class ToTemplateForm(forms.Form):
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={"rows":3, "cols":22}))

class DraftInstanceForm(forms.Form):

    def __init__(self, *args, user=None, **kwargs):
        super(DraftInstanceForm,self).__init__(*args, **kwargs)
        self.fields['selection'] = forms.ModelChoiceField(queryset=LabDraft.objects.filter(user=user))

