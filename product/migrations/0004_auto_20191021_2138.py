# Generated by Django 2.2.6 on 2019-10-22 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='video_name',
            new_name='video_title',
        ),
    ]