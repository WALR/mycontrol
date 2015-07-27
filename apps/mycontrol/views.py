from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters

from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse
#from django.contrib.auth import authenticate, logout
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, FormView
from braces.views import LoginRequiredMixin, GroupRequiredMixin
from .forms import LoginForm



class MainView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = "/login/"


# class LoginView(TemplateView):

# 	template_name = 'login.html'
#     #form_class = LoginForm
# 	success_url = reverse_lazy('main')
# 	# form_class = LoginForm
# 	# success_url = reverse_lazy('home')
#     def post(self, request, *args, **kwargs):
#         request.POST['email'], request.POST['password']

#         user = authenticate(username=request.POST['email'], password='secret')
#         if user is not None:
#             # the password verified for the user
#             if user.is_active:
#                 print("User is valid, active and authenticated")
#             else:
#                 print("The password is valid, but the account has been disabled!")
#         else:
#             # the authentication system was unable to verify the username and password
#             print("The username and password were incorrect.")

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return redirect('/')
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    # @method_decorator(sensitive_post_parameters('password'))
    # def dispatch(self, request, *args, **kwargs):
    #     request.session.set_test_cookie()
    #     return super(LoginView, self).dispatch(request, *args, **kwargs)

    # def get(self, request):
    #     if not self.request.user.is_authenticated:
    #         return super(LoginView, self).get(self, request)
    #     else:
    #         print self.request.user
    #         return redirect("/")
# class LogoutView(View):
#     def get(self, request, *args, **kwargs):
#         auth_logout(request)
#         return redirect('/')
def LogOut(request):
	auth_logout(request)
	return redirect('/')

# from django.conf import settings
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login as auth_login, logout as auth_logout
# from django.http import HttpResponseRedirect
# from django.utils.decorators import method_decorator
# from django.views.decorators.debug import sensitive_post_parameters
# from django.views import FormView, View
#
# class Login(FormView):
#     form_class = AuthenticationForm
#
#     def form_valid(self, form):
#         redirect_to = settings.LOGIN_REDIRECT_URL
#         auth_login(self.request, form.get_user())
#         if self.request.session.test_cookie_worked():
#             self.request.session.delete_test_cookie()
#         return HttpResponseRedirect(redirect_to)
#
#     def form_invalid(self, form):
#         return self.render_to_response(self.get_context_data(form=form))
#
#     @method_decorator(sensitive_post_parameters('password'))
#     def dispatch(self, request, *args, **kwargs):
#         request.session.set_test_cookie()
#         return super(Login, self).dispatch(request, *args, **kwargs)
#
# class Logout(View):
#     def get(self, request, *args, **kwargs):
#         auth_logout(request)
#         return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)
