# Generated by Django 2.2 on 2019-04-20 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20190420_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contract', to='api.Customer'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='lawyer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contract', to='api.Lawyer'),
        ),
    ]