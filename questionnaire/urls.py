from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('', views.index, name='index'),
    path('main_page/', views.main_page, name='main_page'),
    path('questionnaire/<int:questionnaire_id>/', views.questionnaire_details, name='questionnaire_details'),
    path('submit_response/<int:questionnaire_id>/', views.submit_response, name='submit_response'),
]