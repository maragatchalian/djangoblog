from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

#LOGIN_REDIRECT_URL = '/'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'', include('blog.urls')),

# Registration URLs
    url(r'^accounts/register/$', 'mysite.views.register', name='register'),
    url(r'^accounts/register/complete/$', 'mysite.views.registration_complete', name='registration_complete'),

# Auth-related URLs:
    url(r'^accounts/loggedin/$', 'mysite.views.loggedin', name='loggedin'),
]
