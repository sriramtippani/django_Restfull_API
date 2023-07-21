from django import forms
from testapplication1.models import modelForm1

# class formpAge(forms.Form):
#     name = forms.CharField()
#     number = forms.IntegerField()

class formpAge(forms.ModelForm):
    class Meta:
        model = modelForm1
        fields = ('name', 'number')