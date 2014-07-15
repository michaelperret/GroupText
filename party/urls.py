from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'letsparty.views.home', name='home'),
    url(r'^sms/$', 'letsparty.views.sms'),
    url(r'^create/$', 'letsparty.views.create', name='create'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^address/$', 'letsparty.views.address', name='create_address'),
    # url(r'^ring/$', 'letsparty.views.ring'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^register/$', 'letsparty.views.register', name='register'),
    url(r'^admin/', include(admin.site.urls)),
)
