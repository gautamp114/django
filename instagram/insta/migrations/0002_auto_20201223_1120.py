# Generated by Django 3.1.3 on 2020-12-23 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pics',
            field=models.ImageField(upload_to='profile_pics/'),
        ),
    ]
