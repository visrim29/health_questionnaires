from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . import models

def index(request: HttpRequest) -> HttpResponse:
    context = {
        'categories_count': models.Category.objects.count(),
        'questionnaires_count': models.Questionnaires.objects.count(),
        'users_count': models.get_user_model().objects.count(),
    }
    return render(request, 'questionnaires/index.html', context)