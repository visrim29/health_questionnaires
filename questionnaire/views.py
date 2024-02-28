from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from . import models
from .forms import UserRegistrationForm

def main_page(request):
    registration_form = UserRegistrationForm()  # Create an instance of the registration form
    return render(request, 'main_page.html', {'registration_form': registration_form})

def index(request: HttpRequest) -> HttpResponse:
    context = {
        'categories_count': models.Category.objects.count(),
        'questionnaires_count': models.Questionnaires.objects.count(),
        'users_count': models.get_user_model().objects.count(),
    }
    return render(request, 'questionnaires/index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Optionally, create and save UserProfile
            # UserProfile.objects.create(user=user)
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})