# Generated by Django 4.0.2 on 2022-03-01 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestDetails', '0001_initial'),
        ('UserDetails', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='plan',
        ),
        migrations.AddField(
            model_name='lab',
            name='plan',
            field=models.ManyToManyField(to='TestDetails.Plan'),
        ),
    ]