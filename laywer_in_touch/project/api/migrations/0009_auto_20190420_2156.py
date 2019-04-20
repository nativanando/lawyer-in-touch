# Generated by Django 2.2 on 2019-04-20 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_contract_lawyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='lawyer',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='contract', to='api.Lawyer'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='customer',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='contract', to='api.Customer'),
        ),
    ]