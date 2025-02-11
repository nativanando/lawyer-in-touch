# Generated by Django 2.2 on 2019-04-20 20:54

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
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contact_message', models.TextField()),
            ],
            options={
                'db_table': 'contract',
            },
        ),
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cna', models.TextField(blank=True)),
                ('phone', models.TextField()),
                ('is_facebook_auth', models.BooleanField(default=False)),
                ('is_google_auth', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lawyer', to='api.Contract')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lawyer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'lawyer',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.TextField()),
                ('is_facebook_auth', models.BooleanField(default=False)),
                ('is_google_auth', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='api.Contract')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
