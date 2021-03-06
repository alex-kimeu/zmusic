# Generated by Django 2.2.6 on 2019-11-05 06:04

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=25)),
                ('artist', models.CharField(max_length=25)),
                ('cover', models.ImageField(upload_to='')),
                ('genre', models.CharField(choices=[('hiphop', 'HIP HOP'), ('rhumba', 'RHUMBA'), ('trap', 'TRAP'), ('pop', 'POP')], default='Unknown', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=25)),
                ('audio', models.FileField(upload_to='')),
                ('lyrics', models.TextField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.Album')),
            ],
        ),
    ]
