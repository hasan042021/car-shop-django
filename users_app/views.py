from django.shortcuts import render, redirect
from .forms import RegistrationForm, ChangeUserForm
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.auth.models import User


# Create your views here.
class user_login(LoginView):
    template_name = "auth.html"

    def get_success_url(self):
        return reverse_lazy("profile")

    def form_valid(self, form):
        messages.success(self.request, "Logged in Successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Logged in information incorrect")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Login"
        return context


def user_signup(request):
    if request.method == "POST":
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Account Created Successfully")
            return redirect("signup")
    else:
        register_form = RegistrationForm()
    return render(request, "auth.html", {"form": register_form, "type": "Sign Up"})


@method_decorator(login_required, name="dispatch")
class profile(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context


@method_decorator(login_required, name="dispatch")
class edit_profile(UpdateView):
    form_class = ChangeUserForm
    template_name = "edit_profile.html"

    def get_success_url(self):
        return reverse_lazy("profile")

    def get_object(self):
        return self.request.user


@login_required
def user_logout(request):
    logout(request)
    return redirect("login")


def pass_change(request):
    if request.method == "POST":
        form = SetPasswordForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password Updated Successfully")
            update_session_auth_hash(request, form.user)
            return redirect("profile")
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, "auth.html", {"form": form})
