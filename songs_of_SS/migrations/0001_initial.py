# Generated by Django 4.1.7 on 2023-04-05 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('release_date', models.CharField(max_length=100)),
                ('number_of_songs', models.IntegerField()),
                ('photo', models.ImageField(null=True, upload_to='static/songs_of_SS/media')),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('artist', models.CharField(max_length=100)),
                ('mp3_file', models.FileField(upload_to='mp3_files')),
                ('text', models.TextField(blank=True)),
                ('release_date', models.DateField()),
                ('photo', models.ImageField(null=True, upload_to='static/songs_of_SS/media')),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='songs_of_SS.album')),
            ],
        ),
    ]
