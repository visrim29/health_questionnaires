from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .models import Questionnaire, SubmittedResponse
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
    questionnaire = Questionnaire.objects.get(id=questionnaire_id)
    questions = questionnaire.questions.all()
    questions_with_responses = []
    for question in questions:
        responses = question.responses.all()
        questions_with_responses.append({'question': question, 'responses': responses})
    return render(request, 'questionnaire_details.html', {'questionnaire': questionnaire, 'questions_with_responses': questions_with_responses})

def submit_response(request, questionnaire_id):
    if request.method == 'POST':
        questionnaire = Questionnaire.objects.get(id=questionnaire_id)
        for question in questionnaire.questions.all():
            response_id = request.POST.get(f'response_{question.id}')
            if response_id:
                response = question.responses.get(id=response_id)
                SubmittedResponse.objects.create(
                    user=request.user,
                    questionnaire=questionnaire,
                    question=question,
                    response=response
                )
    return redirect('main_page')