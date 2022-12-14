# Generated by Django 4.1.2 on 2022-10-26 15:10

import crowdy.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='file',
            field=models.FileField(upload_to=crowdy.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='company',
            name='picture',
            field=models.ImageField(upload_to=crowdy.models.user_directory_path),
        ),
    ]
