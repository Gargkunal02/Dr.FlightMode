# Generated by Django 4.0.2 on 2022-03-01 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=530)),
                ('description', models.CharField(max_length=1050)),
                ('note', models.CharField(max_length=10000)),
                ('interpretation', models.CharField(max_length=1110)),
            ],
        ),
        migrations.CreateModel(
            name='TestDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testName', models.CharField(max_length=250)),
                ('units', models.CharField(max_length=50)),
                ('bio_ref_interval', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('testType', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='TestDetails.testtype')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=350)),
                ('price', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=350)),
                ('test', models.ManyToManyField(to='TestDetails.TestDetail')),
            ],
        ),
    ]
