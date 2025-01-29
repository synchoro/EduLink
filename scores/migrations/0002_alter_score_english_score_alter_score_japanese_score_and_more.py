# Generated by Django 5.1.4 on 2025-01-26 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='english_score',
            field=models.DecimalField(decimal_places=0, help_text='score/英語の点数', max_digits=5, verbose_name='英語の点数'),
        ),
        migrations.AlterField(
            model_name='score',
            name='japanese_score',
            field=models.DecimalField(decimal_places=0, help_text='score/国語の点数', max_digits=5, verbose_name='国語の点数'),
        ),
        migrations.AlterField(
            model_name='score',
            name='math_score',
            field=models.DecimalField(decimal_places=0, help_text='score/数学の点数', max_digits=5, verbose_name='数学の点数'),
        ),
    ]
