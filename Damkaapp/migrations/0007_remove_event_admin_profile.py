# Generated by Django 4.2 on 2024-11-03 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Damkaapp', '0006_auto_20241027_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='admin_profile',
        ),
    ]