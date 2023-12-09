# Generated by Django 5.0 on 2023-12-08 14:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('student_number', models.CharField(max_length=11, null=True, unique=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('front_library_card', models.ImageField(null=True, upload_to='images/', verbose_name='Front side of your library card:')),
                ('back_library_card', models.ImageField(null=True, upload_to='images/', verbose_name='Back side of your library card:')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
