# Generated by Django 4.2.2 on 2023-06-30 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paiement',
            name='status',
            field=models.CharField(choices=[('Non traité', 'Non Traité')], default='Non traité', max_length=100),
        ),
    ]
