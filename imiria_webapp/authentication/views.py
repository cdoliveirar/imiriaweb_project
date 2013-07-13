# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.http import HttpResponseRedirect

from django.core.mail import send_mail

from .forms import emailResetForm




def login_user(request):
    state = "Please log in!"
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return HttpResponseRedirect("/")
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    
    #context_instance to help with the csrf_token        
    return render_to_response('auth.html',{'state':state, 'username': username,'password':password},context_instance=RequestContext(request))


def reset_password(request):
    if request.method == 'POST':
        form = emailResetForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                      cd['subject'],
                      cd['message'],
                      cd.get('email', 'noreply@example.com'),
                      ['siteowner@example.com'],
                      )
            return HttpResponseRedirect('/reset/complete/')
    else:
        form = emailResetForm(
                              initial={'email': 'Email Address'}
                               )
    return render_to_response('password_reset_form.html', {'form': form},context_instance=RequestContext(request))

