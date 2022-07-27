# Generated by Django 4.0.4 on 2022-07-22 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_courrier_autre_valeur_alter_courrier_chargeur_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courrier',
            old_name='eestination_finale',
            new_name='estination_finale',
        ),
        migrations.AlterField(
            model_name='courrier',
            name='cout_assurance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='cout_des_articles',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='cout_toal',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='emmision_du_besc',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='valeur_Fob',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='valeur_marchandise',
            field=models.FloatField(blank=True, null=True),
        ),
    ]