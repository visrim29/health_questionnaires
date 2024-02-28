from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import UserProfile, Questionnaire
from django.contrib.auth import login
from .forms import ResponseForm, RegistrationForm, LoginForm

@login_required
def main_page(request):
    questionnaires = Questionnaire.objects.all()
    return render(request, 'main_page.html', {'questionnaires': questionnaires})

@login_required
def complete_questionnaire(request, questionnaire_id):
    questionnaire = Questionnaire.objects.get(pk=questionnaire_id)
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.user = request.user
            response.questionnaire = questionnaire
            # Mark the questionnaire as completed for the user
            response.completed = True
            response.save()
            return redirect('main_page')
    else:
        form = ResponseForm()
    return render(request, 'complete_questionnaire.html', {'form': form, 'questionnaire': questionnaire})

def index(request):
    registration_form = RegistrationForm()
    login_form = LoginForm()
    return render(request, 'index.html', {'registration_form': registration_form, 'login_form': login_form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_page')  # Redirect to the main_page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def index(request):
    return render(request, 'index.html')