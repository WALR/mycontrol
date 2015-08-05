from django.conf.urls import patterns, include, url

from .views import LoginView, PerfilView, PerfilEditView

urlpatterns = patterns('',
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^salir/$', 'apps.mycontrol.views.LogOut', name='logout'),
    #url(r'^perfil/(?P<pk>\d+)$', PerfilView.as_view(), name='perfil'),
    url(r'^perfil/$', PerfilView.as_view(), name='perfil'),
    url(r'^perfil-editar/$', PerfilEditView.as_view(), name='perfileditar'),
    # url(r'^perfil-editar/(?P<pk>\d+)$', PerfilEditView.as_view(), name='perfileditar'),
)
