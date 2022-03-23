# Generated by Django 4.0.3 on 2022-03-22 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='anulate',
        ),
        migrations.AddField(
            model_name='department',
            name='active',
            field=models.BooleanField(default=True, verbose_name='department in operation'),
        ),
    ]