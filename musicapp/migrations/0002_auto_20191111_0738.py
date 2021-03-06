# Generated by Django 2.2.6 on 2019-11-11 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[('unknown', 'UNKNOWN'), ('hiphop', 'HIP HOP'), ('rhumba', 'RHUMBA'), ('trap', 'TRAP'), ('pop', 'POP')], default='Unknown', max_length=25),
        ),
    ]
