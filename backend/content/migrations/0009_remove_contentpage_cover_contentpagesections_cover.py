# Generated by Django 4.0.2 on 2022-03-27 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('content', '0008_remove_contentpage_show_subheading_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentpage',
            name='cover',
        ),
        migrations.AddField(
            model_name='contentpagesections',
            name='cover',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
