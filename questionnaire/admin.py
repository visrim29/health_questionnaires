from django.contrib import admin
from django.apps import apps
from . import models
from .forms import forms, ResponseAdminForm

admin.site.register(models.Category)
admin.site.register(models.Questionnaire)
admin.site.register(models.Factors)
admin.site.register(models.Question)

from .models import Response


class ResponseAdminForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = '__all__'
        widgets = {
            'question': forms.widgets.Select(attrs={'required': False})
        }


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    exclude = ['question']
    form = ResponseAdminForm