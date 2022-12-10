from django import forms
from django.core.validators import FileExtensionValidator
from .models import Image
from django.contrib.auth.models import User

class ImgUploadForm(forms.ModelForm):
    name = forms.CharField(label='Name')
    image = forms.FileField(label='Image',
                            widget=forms.widgets.FileInput(),
                            validators=[FileExtensionValidator(
                                allowed_extensions=('png', 'jpg'),
                                # message='Please upload file with png jpg extension',
                                # allow_empty_file = True
                                code='invalid_extension')],
                            )
    desc = forms.CharField(widget=forms.Textarea(), label='Description')

    class Meta:
        model = Image
        fields = ('name', 'image', 'desc')
        error_messages = {
            'image': {
                'invalid_extension': 'Please upload file with png or jpg extension',
                'invalid': 'missing enctype argument',
                'empty': 'empty file',
                'invalid_image': 'Image in wrong extension or image is invalid'
            }
        }
