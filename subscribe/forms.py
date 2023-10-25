from django import forms
from django.utils.translation import gettext_lazy as _

from subscribe.models import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields='__all__'
        # exclude=('first_name',)
        labels={
            'first_name':_('Enter first name'),
            'last_name':_('Enter last name'),
            'email':_('Enter email')
        }
        # help_texts={'first_name':_('Enter characters only')}
        error_messages={
            'first_name':{
                'required':_('You cannot move forward without first name')
            }
        }

        # fields = ['first_name',_'last_name', 'email']

# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Input First Name'}))# help_text='Enter Character Only')
#     last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Input Last Name'}), validators=[validate_comma])
#     email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Input Email'}))

#Custom Validaters
    # def clean_first_name(self):
    #     data = self.cleaned_data['first_name']
    #     if "," in data:
    #         raise forms.ValidationError('Invalid First Name')
    #     return data

