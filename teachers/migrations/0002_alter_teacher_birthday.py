# Generated by Django 5.1.4 on 2025-01-26 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='birthday',
            field=models.DateField(help_text='例：1996-06-02', verbose_name='生年月日'),
        ),
    ]
