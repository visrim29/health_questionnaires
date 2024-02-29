# Generated by Django 5.0.2 on 2024-02-29 06:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0013_submittedresponse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructions_text', models.CharField(default='input your instructions', max_length=255, verbose_name='instructions text')),
                ('questionnaire', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='questionnaire.questionnaire')),
            ],
            options={
                'verbose_name': 'instruction',
                'verbose_name_plural': 'instructions',
                'ordering': ['id'],
            },
        ),
    ]