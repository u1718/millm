# Generated by Django 3.2.10 on 2021-12-28 12:08

from django.db import migrations, models
import django.db.models.deletion
import photologue.models


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0011_auto_20190223_2138'),
        ('photologue_custom', '0004_galleryextended_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoExtended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, upload_to=photologue.models.get_storage_path, verbose_name='image')),
                ('photo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extended', to='photologue.photo')),
            ],
            options={
                'verbose_name': 'Extra fields',
                'verbose_name_plural': 'Extra fields',
            },
        ),
    ]