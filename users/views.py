from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from users.forms import SignupForm

class SignupView(FormView):
    """ Users sign up view. """
    template_name = 'users/register.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:registerok')

    def form_valid(self, form):
        """ Save form data. """
        form.save()
        return super().form_valid(form)

class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    template_name = 'users/logged_out.html'
