# Generated by Django 4.0.5 on 2022-06-26 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_alter_onedelivery_destinataire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onedelivery',
            name='status',
            field=models.CharField(choices=[('livré', 'livré'), ('en cours', 'en cours'), ('retourné', 'retourné')], default='en cours', max_length=128, null=True, verbose_name='status de la livraisons'),
        ),
        migrations.AlterField(
            model_name='onedelivery',
            name='type_de_paiment',
            field=models.CharField(choices=[('chèque', 'chèque'), ('espéce', 'espéce'), ('compte', 'compte'), ('autre', 'autre')], max_length=128, null=True, verbose_name='Type de Paiment'),
        ),
    ]
