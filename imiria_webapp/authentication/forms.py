'''
Created on 20/04/2013

@author: realize
'''

from django import forms

class emailResetForm(forms.Form):
    email = forms.EmailField(required=True)
