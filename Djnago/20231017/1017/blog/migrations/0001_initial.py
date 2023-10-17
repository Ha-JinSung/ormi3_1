# Generated by Django 4.2.6 on 2023-10-17 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('head_image', models.ImageField(blank=True, upload_to='blog/images/%Y/%m/%d/')),
                ('file_upload', models.FileField(blank=True, upload_to='blog/files/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]