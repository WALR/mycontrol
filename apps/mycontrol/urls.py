from django.conf.urls import patterns, include, url

from .views import MainView, LoginView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mycontrol.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', MainView.as_view(), name='main'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    # url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^salir/$', 'apps.mycontrol.views.LogOut', name='logout'),
)
