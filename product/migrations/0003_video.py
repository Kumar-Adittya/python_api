# Generated by Django 2.2.6 on 2019-10-22 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_centers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=100)),
                ('video_article', models.TextField()),
                ('video_link', models.URLField()),
                ('video_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Category', to_field='category_name')),
            ],
        ),
    ]
