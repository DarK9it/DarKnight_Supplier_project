# Generated by Django 4.2.2 on 2023-06-30 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0010_alter_detailcommande_prix_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='statut',
            field=models.CharField(choices=[('En précommande', 'En Précommande')], default='En Précommande', max_length=20),
        ),
    ]
