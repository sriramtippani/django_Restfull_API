from django import forms
from application1.models import Hotel
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class HotelForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    class Meta:
        model = Hotel
        fields = '__all__'

