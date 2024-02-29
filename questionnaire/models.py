from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name="owner", 
        related_name='categories',
        default=1,
    )

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['id']
    
    def __str__(self):
        return self.name


class Questionnaire(models.Model):
    category = models.ForeignKey(
        Category, 
        default=1, 
        on_delete=models.DO_NOTHING
    )
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name="owner", 
        related_name='questionnaires',
        default=1,
    )
    title = models.CharField(
        max_length=255, 
        default='new questionnaire', 
        verbose_name='questionnaire title'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'questionnaire'
        verbose_name_plural = 'questionnaires'
        ordering = ['id']

    def __str__(self):
        return self.title


class Factors(models.Model):
    questionnaire = models.ForeignKey(
        Questionnaire, 
        default=1, 
        on_delete=models.DO_NOTHING
    )
    title = models.CharField(
        max_length=255, 
        default='new factor', 
        verbose_name='factor title'
    )

    class Meta:
        verbose_name = 'factor'
        verbose_name_plural = 'factors'
        ordering = ['id']

    def __str__(self):
        return self.title

class Question(models.Model):
    questionnaire = models.ForeignKey(
        Questionnaire, 
        default=1, 
        on_delete=models.DO_NOTHING
    )
    factor = models.ForeignKey(
        Factors, 
        default=1, 
        on_delete=models.DO_NOTHING
    )
    title = models.CharField(
        max_length=255, 
        verbose_name='question title'
    )
    responses = models.CharField(
        default=1,
        max_length=255, 
        verbose_name='possible responses', 
        help_text='Enter possible responses separated by commas'
    )

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'questions'
        ordering = ['id']

    def __str__(self):
        return self.title


class Response(models.Model):
    question = models.ForeignKey(
        Question, 
        default=1, 
        on_delete=models.DO_NOTHING
    )
    response = models.CharField(
        max_length=255, 
        default='new response', 
        verbose_name='response'
    )
    questionnaire = models.ForeignKey(
        Questionnaire, 
        default=1,
        on_delete=models.CASCADE
    )
    
    class Meta:
        verbose_name = 'response'
        verbose_name_plural = 'responses'
        ordering = ['id']

    def __str__(self):
        return self.response


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user.username