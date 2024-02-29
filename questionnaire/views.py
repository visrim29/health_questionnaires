from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import UserProfile, Questionnaire, Question, Response
from django.contrib.auth import login
from .forms import ResponseForm, RegistrationForm, LoginForm

def main_page(request):
    questionnaires = Questionnaire.objects.all()
    return render(request, 'main_page.html', {'questionnaires': questionnaires})

def complete_questionnaire(request, questionnaire_id):
    questionnaire = Questionnaire.objects.get(pk=questionnaire_id)
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.questionnaire = questionnaire
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
            return redirect('main_page')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def questionnaire_details(request, questionnaire_id):
    questionnaire = Questionnaire.objects.get(pk=questionnaire_id)
    questions = questionnaire.question_set.all()  # Retrieve all questions for the questionnaire
    return render(request, 'questionnaire_details.html', {'questionnaire': questionnaire, 'questions': questions})

def submit_response(request, questionnaire_id):
    if request.method == 'POST':
        questionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id)
        for question in questionnaire.questions.all():
            response_id = request.POST.get(f'responses_{question.id}')
            if response_id:
                response = get_object_or_404(Response, pk=response_id)
                response.users.add(request.user)
        return redirect('main_page')
    return redirect('questionnaire_details', questionnaire_id=questionnaire_id)