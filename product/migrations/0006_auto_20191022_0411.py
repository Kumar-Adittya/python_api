# Generated by Django 2.2.6 on 2019-10-22 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20191022_0327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='centers',
            name='center_lat',
        ),
        migrations.RemoveField(
            model_name='centers',
            name='center_long',
        ),
    ]