from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, FormView
from braces.views import LoginRequiredMixin, GroupRequiredMixin
from .forms import LoginForm, UserEditForm

from .models import User
#from apps.users.models import User

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return redirect('/')
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

def LogOut(request):
	auth_logout(request)
	return redirect('/')

class PerfilView(LoginRequiredMixin, TemplateView):

    template_name = 'users/perfil_user.html'
    login_url = "/login/"

    def get_context_data(self, **kwargs):
        context = super(PerfilView, self).get_context_data(**kwargs)
        context['user'] = User.objects.get(pk = self.request.user.id)
        return context


class PerfilEditView(LoginRequiredMixin, FormView):

    template_name = 'users/editperfil_user.html'
    success_url = reverse_lazy('user_app:perfil')
    model = User
    form_class = UserEditForm
    login_url = "/login/"

    def get_context_data(self, **kwargs):
        context = super(PerfilEditView, self).get_context_data(**kwargs)
        context['user'] = User.objects.get(pk = self.request.user.id)
        return context

    def get_initial(self):
        data = {
            'username' : self.request.user.username,
            'nombre' : self.request.user.nombre,
            'apellido' : self.request.user.apellido,
            'email' : self.request.user.email,
        }
        return data
