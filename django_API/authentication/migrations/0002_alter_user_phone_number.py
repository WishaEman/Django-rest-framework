# Generated by Django 4.2.2 on 2023-08-03 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(help_text='Enter 11 digits phone number'),
        ),
    ]