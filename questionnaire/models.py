from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE, 
        verbose_name=_("owner"), 
        related_name='categories',
        default=1,
    )

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ['id']
    
    def __str__(self):
        return self.name


class Questionnaires(models.Model):
    category = models.ForeignKey(
        Category, default=1, on_delete=models.DO_NOTHING
    )
    owner = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE, 
        verbose_name=_("owner"), 
        related_name='questionnaires',
        default=1,
    )
    title = models.CharField(max_length=255, default=_('new questionnaire'), verbose_name=_('questionnaire title'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('questionnaire')
        verbose_name_plural = _('questionnaires')
        ordering = ['id']

    def __str__(self):
        return self.title


class Factors(models.Model):
    questionnaire = models.ForeignKey(
        Questionnaires, default=1, on_delete=models.DO_NOTHING
    )
    title = models.CharField(max_length=255, default=_('new factor'), verbose_name=_('factor title'))

    class Meta:
        verbose_name = _('factor')
        verbose_name_plural = _('factors')
        ordering = ['id']

    def __str__(self):
        return self.title

class Question(models.Model):
    questionnaire = models.ForeignKey(
        Questionnaires, default=1, on_delete=models.DO_NOTHING
    )
    factor = models.ForeignKey(
        Factors, default=1, on_delete=models.DO_NOTHING
    )
    title = models.CharField(max_length=255, verbose_name=_('question title'))

    class Meta:
        verbose_name = _('question')
        verbose_name_plural = _('questions')
        ordering = ['id']

    def __str__(self):
        return self.title


class Questionnaire(models.Model):
    title = models.CharField(max_length=100)

class Response(models.Model):
    question = models.ForeignKey(
        Question, default=1, on_delete=models.DO_NOTHING
    )
    response = models.CharField(max_length=255, default=_('new response'), verbose_name=_('response'))
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _('response')
        verbose_name_plural = _('responses')
        ordering = ['id']

    def __str__(self):
        return self.response
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username