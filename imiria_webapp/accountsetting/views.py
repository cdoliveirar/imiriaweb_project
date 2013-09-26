# Create your views here.

'''
@author: carlos oliveira
'''

from django.shortcuts import HttpResponseRedirect, render, render_to_response
from django.template import RequestContext
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import FormView
from .forms import BusinessProfile_form
from .models import EnterpriseBusiness



def profile_view(request):
    enterpriseBusinessList = EnterpriseBusiness.objects.all()
    print enterpriseBusinessList
    return render_to_response('settings_profile.html',{"enterpriseBusinessList" : enterpriseBusinessList},context_instance=(request))

#def account_setting(request):
#    return render_to_response('profile.html',"",context_instance=RequestContext(request))

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
    
class BusinessProfile_view(FormView):
    form_class = BusinessProfile_form
    template_name = "profile.html"
    #success_url = '/'
    '''
    def form_valid(self, form):
        form.instance.first_name = self.request.first_name
        
        #frm = BusinessProfile_form(self.request.POST)
        return super(BusinessProfile_view,self).form_valid(form)
    '''
    
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
    
    '''
    def is_valid(self, form):
        user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
        )
        return super(CreateUser, self).form_valid(form)
    '''    
        

        

    