# Generated by Django 4.0.4 on 2022-07-23 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_rename_eestination_finale_courrier_estination_finale_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courrier',
            name='date_arrivee',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='date_depart',
            field=models.DateField(blank=True, null=True),
        ),
    ]