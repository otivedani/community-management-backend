# Generated by Django 3.1.2 on 2020-10-24 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manager',
            old_name='listing',
            new_name='community',
        ),
    ]
