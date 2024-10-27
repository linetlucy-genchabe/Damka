# Generated by Django 3.2 on 2024-10-27 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Damkaapp', '0003_remove_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='Description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='Image',
            field=models.ImageField(upload_to='', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='event',
            name='Description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='Image',
            field=models.ImageField(upload_to='', verbose_name='image'),
        ),
    ]
