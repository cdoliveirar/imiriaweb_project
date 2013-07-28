'''
@author: carlos oliveira
'''

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext


def imiria_home(request):
    return render_to_response('home.html',"",context_instance=RequestContext(request))
    