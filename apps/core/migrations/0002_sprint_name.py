# Generated by Django 4.1.3 on 2022-11-14 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='name',
            field=models.CharField(default='Semana 1', max_length=90, verbose_name='name'),
            preserve_default=False,
        ),
    ]
