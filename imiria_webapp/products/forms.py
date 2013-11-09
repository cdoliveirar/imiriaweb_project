from django.forms import ModelForm
from .models import ImiriaCategory

class CategoryForm(ModelForm):
    class Meta:
        model = ImiriaCategory
        fields = ['category_name']


class ProductForm1(forms.Form):
    class Meta:
    	



