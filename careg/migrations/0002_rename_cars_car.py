# Generated by Django 3.2.13 on 2022-05-06 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('careg', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cars',
            new_name='Car',
        ),
    ]