# Generated by Django 2.2 on 2019-04-20 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20190420_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='api.Customer'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='lawyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='api.Lawyer'),
        ),
    ]
