from captcha.fields import CaptchaField
from django import forms
from django.core.exceptions import ValidationError

from .models import Bb
from django import forms
from bboard.models import Rubric


class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=20, label="Some Text")
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(), label='Rubric')


class CommentForm(forms.Form):
    captcha = CaptchaField(label='Text from picture', error_messages={'invalid': 'Wrong answer'})


class BbForm(forms.ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric', 'kind')

        # def clean_kind(self):
        #     """Field validation level"""
        #     data = self.cleaned_data['kind']
        #     if 'yourdomain@gmail.com' not in data:
        #         raise ValidationError('Invalid')
        #     return data
        #
        # def clean_price(self):
        #     """Field validation level"""
        #     data = self.cleaned_data.get('price')
        #     if data > 1:
        #         raise ValidationError('Should be lower than 1')
        #
        # def clean(self):
        """Form validation level"""
    #     cleaned_data = super(BbForm, self).clean()
    #
    #     kind_passed = cleaned_data.get('kind')
    #     kind_req = 'Fred'
    #
    #     price_passed = cleaned_data.get('price')
    #     price_req = 1000
    #     if price_req == 1000:
    #         raise ValidationError('Not equal 1000')
    #     if not kind_req in kind_passed:
    #         raise ValidationError('Not a valid kind')
    #     return cleaned_data
