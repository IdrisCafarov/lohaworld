# Generated by Django 3.2.21 on 2023-10-19 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(editable=False, null=True, verbose_name='Slug'),
        ),
    ]
