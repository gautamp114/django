# Generated by Django 3.0.3 on 2020-02-26 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_productimage_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('title', 'slug')},
        ),
    ]
