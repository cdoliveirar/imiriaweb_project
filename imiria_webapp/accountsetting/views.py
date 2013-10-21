# Create your views here.

'''
@author: carlos oliveira
'''
from django.contrib.auth.decorators import login_required

from django.shortcuts import HttpResponseRedirect,render, render_to_response
from django.template import RequestContext
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import FormView
from .forms import OnwerProfileForm
from .forms import BusinessProfileForm
from .models import EnterpriseBusiness
from django.contrib.auth.models import User

#from .forms import BusinessProfile_form
#from .models import EnterpriseBusiness


#def account_setting(request):
#    return render_to_response('profile.html',"",context_instance=RequestContext(request))
'''
def ver_perfil(request):

    return render_to_response('profile.html',"",context_instance=RequestContext(request))

'''


@login_required()
def owner_profile(request):
    
    userObj= User.objects.get(id=request.user.id)
    
    business = EnterpriseBusiness()

    if request.method == 'POST':
        #form = BusinessProfileForm(request.POST,instance=request.user)
        form = OnwerProfileForm(request.POST)
        if form.is_valid():
            #form.save()
            #obj, created = EnterpriseBusiness.objects.get_or_create(user= userObj)
            instance = form.save(commit=False)
            instance = EnterpriseBusiness.objects.get(user = userObj)
            instance.first_name = request.POST['first_name']
            instance.last_name =  request.POST['last_name']
            instance.business_card = request.POST['business_card']
            instance.save()

            return HttpResponseRedirect('/settings/profile')
    else:
        
        obj, created = EnterpriseBusiness.objects.get_or_create(user= userObj)


        form = OnwerProfileForm(instance = obj)
        #form = BusinessProfileForm() 
    
    return render(request, 'profile.html', {'form': form})
    #return render_to_response('profile.html',{'form': form},context_instance=RequestContext(request))


@login_required()
def business_profile(request):

    userObj= User.objects.get(id=request.user.id)


    if request.method == 'POST':
        #form = BusinessProfileForm(request.POST,instance=request.user)
        form = BusinessProfileForm(request.POST)
        if form.is_valid():
            #form.save()
            #obj, created = EnterpriseBusiness.objects.get_or_create(user= userObj)
            instance = form.save(commit=False)
            instance = EnterpriseBusiness.objects.get(user = userObj)
            instance.business_type = request.POST['business_name']
            instance.business_name =  request.POST['business_type']
            instance.business_card = request.POST['business_card']
            instance.save()

            return HttpResponseRedirect('/settings/enterprice')
    else:
        obj, created = EnterpriseBusiness.objects.get_or_create(user= userObj)
        form = BusinessProfileForm(instance = obj)


    return render(request, 'profile_enterprice.html', {'form': form})
    #return render_to_response('profile_enterprice.html',{'form': form},context_instance=RequestContext(request))



'''
class EnterpriceBusinessView(CreateView):
    template_name = "profile.html"  
    form_class = EnterpriseBusiness_form 
    #model =  EnterpriseBusiness
    success_url="/settings"
'''    
'''
class EnterpriceBusinessViewDetail(DetailView):
    model = EnterpriseBusiness
    template_name = "profile_detail.html"
'''
    
'''
class BusinessProfile_view(FormView):
    form_class = BusinessProfile_form
    template_name = "profile.html"
    #success_url = '/'
   
    #option 1
    def form_valid(self, form):
        form.instance.first_name = self.request.first_name
        
        #frm = BusinessProfile_form(self.request.POST)
        return super(BusinessProfile_view,self).form_valid(form)
   
    #option 2
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            EnterpriseBusiness.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            business_name = request.POST['business_name'],
            logo =  request.POST['logo'],
            about = request.POST['about'],
            website = request.POST['website']
            )
            return HttpResponseRedirect('/settings')      
        return render(request, self.template_name, {'form': form})
    
    
    def is_valid(self, form):
        user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
        )
        return super(CreateUser, self).form_valid(form)
    '''    
        



    