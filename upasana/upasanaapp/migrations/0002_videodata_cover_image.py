# Generated by Django 3.0.7 on 2020-07-25 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upasanaapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videodata',
            name='cover_image',
            field=models.ImageField(default='', upload_to='upasanaapp/images'),
        ),
    ]
