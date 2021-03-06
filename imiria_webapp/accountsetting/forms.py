from django import forms
from django.contrib.admindocs.tests import fields
from .models import EnterpriseBusiness
from .models import Country
#from .models import AuthUser
#from django.forms.widgetsm import Widget
from django.forms import ModelForm


class OnwerProfileForm(ModelForm):
    class Meta:
        model = EnterpriseBusiness
        fields = ['first_name','last_name','business_card']

class BusinessProfileForm(ModelForm):
    class Meta:
        model = EnterpriseBusiness
        fields = ['business_name','logo','about','website','business_type','country']


'''
class BusinessProfile_form(forms.ModelForm):
    
    class Meta:
        model= EnterpriseBusiness

    def __init__(self,*args, **kwargs):
        super(BusinessProfile_form,self).__init__(*args, **kwargs)
        #self.fields[""]
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["business_name"].required = True
        self.fields["logo"].required = True
        self.fields["about"].required = True
        self.fields["website"].required = True
        self.fields["created_at"].required = True
        self.fields["country_name"] = forms.ModelChoiceField(queryset=Country.objects.all())

'''
# insert con este form!!

'''
class BusinessProfile_form(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    business_name = forms.CharField(max_length=50)
    logo = forms.ImageField()
    about = forms.CharField(widget=forms.Textarea)
    website = forms.CharField(max_length=50)
'''
