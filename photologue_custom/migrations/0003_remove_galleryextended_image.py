# Generated by Django 3.2.10 on 2021-12-24 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue_custom', '0002_galleryextended_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryextended',
            name='image',
        ),
    ]
