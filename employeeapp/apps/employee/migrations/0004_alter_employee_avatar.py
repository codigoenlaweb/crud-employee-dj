# Generated by Django 4.0.3 on 2022-03-22 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_alter_employee_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='avatar',
            field=models.ImageField(blank=True, null='True', upload_to='', verbose_name='employee image'),
        ),
    ]
