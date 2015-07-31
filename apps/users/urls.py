from django.conf.urls import patterns, include, url

from .views import LoginView, PerfilView, ChangePassView

urlpatterns = patterns('',
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^salir/$', 'apps.mycontrol.views.LogOut', name='logout'),
    #url(r'^perfil/(?P<pk>\d+)$', PerfilView.as_view(), name='perfil'),
    url(r'^perfil/$', PerfilView.as_view(), name='perfil'),
    url(r'^cambiar-pass/(?P<pk>\d+)$', ChangePassView.as_view(), name='ChangePass'),
)
