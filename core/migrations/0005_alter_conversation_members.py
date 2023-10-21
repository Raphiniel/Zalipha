# Generated by Django 4.1.6 on 2023-03-07 20:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='members',
            field=models.ManyToManyField(related_name='conversations', to=settings.AUTH_USER_MODEL),
        ),
    ]