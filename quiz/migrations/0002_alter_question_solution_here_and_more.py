# Generated by Django 5.0 on 2024-02-08 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='solution_here',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='soloquestion',
            name='solution_here',
            field=models.TextField(blank=True, null=True),
        ),
    ]
