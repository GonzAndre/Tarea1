# Generated by Django 2.0.4 on 2018-04-21 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Basketball', '0002_auto_20180420_0247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='photo',
            new_name='logo',
        ),
    ]