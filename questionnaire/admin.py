from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.Questionnaire)
admin.site.register(models.Factors)
admin.site.register(models.Question)
admin.site.register(models.Response)