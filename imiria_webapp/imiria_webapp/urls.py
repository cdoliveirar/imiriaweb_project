from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
# wizard part
from django.conf.urls import patterns
from wizard.forms import ContactForm1, ContactForm2
from wizard.views import ContactWizard


#from accountsetting.views import BusinessProfile_view


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'imiria_webapp.views.home', name='home'),
    # url(r'^imiria_webapp/', include('imiria_webapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #index
    url(r'^$', 'indexpackage.views.imiria_index'),
    url(r'^home/$', 'imihome.views.imiria_home'),
    #auth
    url(r'^login/', 'authentication.views.login_user'),
    url(r'^join/signup/', 'authentication.views.login_user'),  # signup url de join para las redes sociales
    url(r'^join/register/', 'authentication.views.login_user'), # register join para imiria
    
    url(r'^password/reset/', 'authentication.views.reset_password'),
    
    #allauth
    (r'^accounts/', include('allauth.urls')),
    #setting account
    #url(r'^settings/', EnterpriceBusinessView.as_view()),
    #url(r'^settings/', BusinessProfile_view.as_view()),
    #ver profile
    (r'^settings/', include('accountsetting.urls')),

    (r'^posting_product/', 'products.views.posting_product'),

)

