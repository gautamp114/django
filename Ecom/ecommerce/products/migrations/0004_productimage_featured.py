# Generated by Django 3.0.3 on 2020-02-26 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
