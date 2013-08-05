from django import forms
from .models import EnterpriseBusiness
from .models import Country
from .models import AuthUser

class EnterpriseBusiness_form(forms.ModelForm):
    
    class Meta:
        model= EnterpriseBusiness
    
    def __init__(self,*args, **kwargs):
        super(EnterpriseBusiness_form,self).__init__(*args, **kwargs)
        #self.fields[""]
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["business_name"].required = True
        self.fields["logo"].required = True
        self.fields["about"].required = True
        self.fields["website"].required = True
        self.fields["created_at"].required = True
        self.fields["country_name"] = forms.ModelChoiceField(queryset=Country.objects.all())
      
         
    