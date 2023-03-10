# Generated by Django 4.1.7 on 2023-02-24 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0002_joke_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke',
            name='slug',
            field=models.SlugField(default=1, editable=False, unique=True),
            preserve_default=False,
        ),
    ]
