#from django.shortcuts import render

# Create your views here.
# accounts/views.py

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")  # Redirect to login page upon success
    template_name = "registration/signup.html"  # Template to render the form
