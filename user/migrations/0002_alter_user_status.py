# Generated by Django 4.0.4 on 2022-07-15 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.BooleanField(choices=[('1', '1'), ('0', '0')], default='1', max_length=25, null=True),
        ),
    ]
