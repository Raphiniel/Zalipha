# Generated by Django 2.2.5 on 2019-09-25 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaynowPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cellphone', models.CharField(blank=True, max_length=100, null=True)),
                ('reference', models.CharField(max_length=100)),
                ('paynow_reference', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('additionalinfo', models.CharField(blank=True, max_length=500)),
                ('authemail', models.CharField(blank=True, max_length=100)),
                ('init_status', models.CharField(blank=True, max_length=10)),
                ('pollurl', models.CharField(max_length=500)),
                ('browserurl', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=10)),
                ('paid', models.BooleanField(default=False)),
                ('confirmed_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
