from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class QuestionnaireConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'questionnaire'

    class Meta:
        verbose_name = _('questionnaire')