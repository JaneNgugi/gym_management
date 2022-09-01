from django import forms
from django.forms import ModelForm
from .models import Contact
class ContactForm(ModelForm):
    class Meta:
        model=Contact
        # fields='__all__'
        fields = ('first_name','email','message')
        labels = {'first_name':' Your Name',
                    'email':'Your Email' ,
                    'message':'Message'}
        Widget = {'first_name': forms.TextInput(attrs={'class':'form-control'}),
                    'email': forms.TextInput(attrs={'class':'form-control' }),
                    'message': forms.Textarea(attrs={'class': 'form-control'})}
 