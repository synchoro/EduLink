# Generated by Django 5.1.4 on 2025-01-26 07:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grades', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=50, verbose_name='教師名')),
                ('phone_number', models.CharField(max_length=11, unique=True, verbose_name='電話番号')),
                ('gender', models.CharField(choices=[('M', '男性'), ('F', '女性')], max_length=1, verbose_name='性別')),
                ('birthday', models.DateField(help_text='例：2020-05-01', verbose_name='生年月日')),
                ('grade', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='grades.grade', verbose_name='担当クラス')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '教師情報',
                'verbose_name_plural': '教師情報',
                'db_table': 'teacher',
            },
        ),
    ]
