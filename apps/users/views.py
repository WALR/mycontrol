from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, FormView
from braces.views import LoginRequiredMixin, GroupRequiredMixin
from .forms import LoginForm

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

class PerfilView(LoginRequiredMixin, DetailView):
    
    template_name = 'users/perfil_user.html'
    model = User
    login_url = "/login/"
