# Generated by Django 3.2 on 2024-10-27 17:12

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Damkaapp', '0005_remove_activity_admin_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='Image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='event',
            name='Image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]
