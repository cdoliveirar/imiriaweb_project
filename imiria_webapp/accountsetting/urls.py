from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^profile/$','accountsetting.views.owner_profile'),
    url(r'^enterprice/$', 'accountsetting.views.business_profile'),

)

