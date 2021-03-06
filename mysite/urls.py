from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin


admin.autodiscover()

#LOGIN_REDIRECT_URL = '/'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'', include('blog.urls')),

# Registration URLs
 	url(r'^accounts/register/$', 'blog.views.register', name='register'),
    url(r'^accounts/register/registration_complete/$', 'blog.views.registration_complete', name='registration_complete'),

# Auth-related URLs:
    url(r'^accounts/loggedin/$', 'blog.views.loggedin', name='loggedin'),

    url(r'^$', 'blog.views.index'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
