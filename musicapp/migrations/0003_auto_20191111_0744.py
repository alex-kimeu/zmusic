# Generated by Django 2.2.6 on 2019-11-11 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_auto_20191111_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(upload_to=''),
        ),
    ]
