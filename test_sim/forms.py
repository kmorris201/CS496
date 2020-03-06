from django import forms

class InputForm(forms.Form):

    loop_radius = forms.FloatField(label='Loop Radius (cm)')
    b_zero = forms.FloatField(label='B Zero')
    f = forms.FloatField(label='Frequency')
    r = forms.FloatField(label='Resistence')
    seconds = forms.IntegerField(label='Number of Seconds')
