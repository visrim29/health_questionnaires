# Generated by Django 5.0.2 on 2024-02-29 02:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0011_alter_response_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='questionnaire.question'),
        ),
    ]
