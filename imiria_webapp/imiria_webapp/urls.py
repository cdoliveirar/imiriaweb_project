from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

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
    #auth
    url(r'^login/', 'authentication.views.login_user'),
    url(r'^join/signup/', 'authentication.views.login_user'),  # signup url de join para las redes sociales
    url(r'^join/register/', 'authentication.views.login_user'), # register join para imiria
    
    url(r'^password/reset/', 'authentication.views.reset_password'),
    
    #allauth
    (r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/', 'businessusers.views.view_profile'),
    
)

