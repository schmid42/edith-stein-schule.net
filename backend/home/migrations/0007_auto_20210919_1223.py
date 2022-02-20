# Generated by Django 3.2.7 on 2021-09-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210703_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='show_actual',
            new_name='show_welcome',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='actual',
        ),
        migrations.AddField(
            model_name='homepage',
            name='welcome',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]