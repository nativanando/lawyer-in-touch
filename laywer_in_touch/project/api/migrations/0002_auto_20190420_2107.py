# Generated by Django 2.2 on 2019-04-20 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='contact_message',
            new_name='contract_message',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='contract',
        ),
        migrations.RemoveField(
            model_name='lawyer',
            name='contract',
        ),
        migrations.AddField(
            model_name='contract',
            name='customer',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='customer_contract', to='api.Customer'),
        ),
        migrations.AddField(
            model_name='contract',
            name='lawyer',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='lawyer_contract', to='api.Lawyer'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='cna',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='phone',
            field=models.TextField(blank=True),
        ),
    ]