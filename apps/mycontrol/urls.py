from django.conf.urls import patterns, include, url

from .views import main

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mycontrol.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', main.as_view(), name='main'),
)
