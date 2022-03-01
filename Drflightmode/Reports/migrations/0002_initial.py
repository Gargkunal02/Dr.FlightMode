# Generated by Django 4.0.2 on 2022-03-01 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TestDetails', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patienttestdetail',
            name='User',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='patienttestdetail',
            name='parameter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestDetails.testdetail'),
        ),
    ]