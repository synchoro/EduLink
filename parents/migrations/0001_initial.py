# Generated by Django 5.1.4 on 2025-01-26 14:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0002_alter_student_birthday_alter_student_contact_number_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_name', models.CharField(max_length=50, verbose_name='保護者名')),
                ('phone_number', models.CharField(max_length=11, unique=True, verbose_name='電話番号')),
                ('children', models.ManyToManyField(related_name='parents', to='students.student', verbose_name='子供たち')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='parent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
