# Generated by Django 3.2.23 on 2023-11-29 13:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='content',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='content_az',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='content_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='country_az',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='country_en',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='major_az',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='major_en',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='name_az',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='name_en',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
