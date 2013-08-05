# Create your views here.

'''
@author: carlos oliveira
'''

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import CreateView
from .forms import EnterpriseBusiness_form

#def account_setting(request):
#    return render_to_response('profile.html',"",context_instance=RequestContext(request))

class EnterpriceBusinessView(CreateView):
    template_name = "profile.html"
    form_class = EnterpriseBusiness_form
    
    

    
    




