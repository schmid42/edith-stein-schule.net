# Generated by Django 4.0.2 on 2022-04-07 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_homepage_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='collection',
        ),
    ]
