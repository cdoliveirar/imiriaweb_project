from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

@login_required()
def posting_product(request):
    return  render_to_response('posting_product.html',"",context_instance=RequestContext(request))
