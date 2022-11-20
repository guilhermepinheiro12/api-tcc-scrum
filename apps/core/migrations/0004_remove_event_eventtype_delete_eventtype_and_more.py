# Generated by Django 4.1.3 on 2022-11-20 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_task_requirement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='eventType',
        ),
        migrations.DeleteModel(
            name='EventType',
        ),
        migrations.AddField(
            model_name='event',
            name='eventtype',
            field=models.IntegerField(default=1, verbose_name='eventtype'),
            preserve_default=False,
        ),
    ]
