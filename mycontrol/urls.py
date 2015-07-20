from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mycontrol.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('apps.mycontrol.urls', namespace="mycontrol_app")),
    url(r'^admin/', include(admin.site.urls)),
)
