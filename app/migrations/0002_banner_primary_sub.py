# Generated by Django 5.0 on 2023-12-08 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='primary_sub',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]