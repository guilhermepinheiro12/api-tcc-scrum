# Generated by Django 4.1.3 on 2022-11-20 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='priority',
            field=models.IntegerField(verbose_name='priority'),
        ),
    ]
