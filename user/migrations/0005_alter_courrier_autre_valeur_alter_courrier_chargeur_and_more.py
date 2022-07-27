# Generated by Django 4.0.4 on 2022-07-22 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_courrier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courrier',
            name='autre_valeur',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='chargeur',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='cout_assurance',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='cout_des_articles',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='cout_toal',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='destinataire',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='eestination_finale',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='emmision_du_besc',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='monaie',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='navire_et_numeroVoyage',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='notifier',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='operation',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='police_de_cargaison',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='port_Chargement',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='port_Dechargement',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='tarif',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='transitaire',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='transporteur',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='valeur_Fob',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='valeur_marchandise',
            field=models.FloatField(null=True),
        ),
    ]