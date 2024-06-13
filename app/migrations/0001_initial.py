# Generated by Django 5.0.6 on 2024-06-12 16:27

import app.models
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='This video is a short title!', max_length=150, unique=True)),
                ('description', models.TextField(blank=True, help_text='Description for the video!')),
                ('video_content', models.FileField(help_text='Please upload *.mp4, *.mov, *.avi, *.mkv, *.flv, *.wmv and *.webm format files.', upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'avi', 'mkv', 'flv', 'wmv', 'webm'], message='File format is wrong!'), app.models.validate_file_size])),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
                ('category', models.ForeignKey(help_text='What category does this video belong to?', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.category')),
            ],
        ),
    ]