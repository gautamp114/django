# Generated by Django 3.0.3 on 2020-03-20 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200319_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerlogin',
            name='address',
            field=models.CharField(default='', max_length=15),
        ),
    ]
