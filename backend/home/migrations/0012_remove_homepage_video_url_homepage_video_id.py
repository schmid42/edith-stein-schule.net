# Generated by Django 4.0.2 on 2022-04-02 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_homepage_options_homepage_video_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='video_url',
        ),
        migrations.AddField(
            model_name='homepage',
            name='video_id',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]