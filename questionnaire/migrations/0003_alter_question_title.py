# Generated by Django 5.0.2 on 2024-02-27 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_alter_category_options_alter_factors_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=255, verbose_name='question title'),
        ),
    ]
