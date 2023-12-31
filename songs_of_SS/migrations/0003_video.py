# Generated by Django 4.1.7 on 2023-04-05 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs_of_SS', '0002_alter_album_release_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('mp4_file', models.FileField(upload_to='mp4_files')),
                ('song', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='songs_of_SS.song')),
            ],
        ),
    ]
