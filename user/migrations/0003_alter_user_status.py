# Generated by Django 4.0.4 on 2022-07-15 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.BooleanField(choices=[('ACTIF', 'ACTIF'), ('INACTIF', 'INACTIF')], default='1', max_length=25, null=True),
        ),
    ]
