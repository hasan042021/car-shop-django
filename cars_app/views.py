from django.shortcuts import render
from django.views.generic import DetailView
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
from . import models
from . import forms


class car_details(DetailView):
    model = models.Car
    pk_url_kwarg = "id"
    template_name = "car_details.html"

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = forms.CommentForm()

        context["comments"] = comments
        context["comment_form"] = comment_form
        return context
