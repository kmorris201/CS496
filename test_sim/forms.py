from django import forms
from .models import TestSim

class InputForm(forms.Form):

    loop_radius = forms.FloatField(label='Loop Radius (cm)')
    b_zero = forms.FloatField(label='B Zero')
    f = forms.FloatField(label='Frequency')
    r = forms.FloatField(label='Resistence')
    seconds = forms.IntegerField(label='Number of Seconds')

class InstanceForm(forms.Form):

    def __init__(self, *args, user = None, **kwargs):
        super(InstanceForm,self).__init__(*args, **kwargs)
        self.fields['selection'] = forms.ModelChoiceField(queryset=TestSim.objects.filter(user=user))

class ResourceTypeForm(forms.Form):

    # When more resource types can be created, they should be added as 
    # a choice in this form
    choices = [
            ('line','Line')
        ]

    res_type = forms.ChoiceField(label='Resource Type To Generate', choices = choices)
    pk = forms.IntegerField(widget = forms.HiddenInput())

