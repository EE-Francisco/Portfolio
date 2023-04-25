from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm

def profile(request):
    return render(request, 'profile.html')