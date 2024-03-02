# Generated by Django 5.0.2 on 2024-03-02 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_highlightsevent_link_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='highlightsevent',
            name='date_from',
            field=models.DateField(blank=True, null=True, verbose_name='End ng date'),
        ),
        migrations.AlterField(
            model_name='highlightsevent',
            name='date_to',
            field=models.DateField(blank=True, null=True, verbose_name='Start ng date'),
        ),
        migrations.AlterField(
            model_name='highlightsevent',
            name='link_desc',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
