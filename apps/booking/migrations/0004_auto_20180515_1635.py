# Generated by Django 2.0.5 on 2018-05-15 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20180515_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='guest',
            new_name='guests',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='intensity',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='price',
        ),
    ]
