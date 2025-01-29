# Generated by Django 5.1.4 on 2025-01-27 05:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_birthday_alter_student_contact_number_and_more'),
        ('teachers', '0002_alter_teacher_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='head_teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='teachers.teacher', verbose_name='担任先生'),
        ),
        migrations.AddField(
            model_name='student',
            name='parent_names',
            field=models.TextField(blank=True, verbose_name='保護者名一覧'),
        ),
    ]
