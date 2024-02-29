# Generated by Django 5.0.2 on 2024-02-29 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0008_responsetemplate_question_common_responses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='common_responses',
        ),
        migrations.AddField(
            model_name='question',
            name='responses',
            field=models.CharField(default=1, help_text='Enter possible responses separated by commas', max_length=255, verbose_name='possible responses'),
        ),
        migrations.DeleteModel(
            name='ResponseTemplate',
        ),
    ]