# Generated by Django 3.2.21 on 2023-10-31 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='facebook',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='linkedin',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='twitter',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
