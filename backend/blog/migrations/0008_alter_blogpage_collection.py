# Generated by Django 4.0.2 on 2022-04-07 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogpage_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='collection',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]