# Generated by Django 4.0.2 on 2022-03-27 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_contentpage_show_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contentpagesections',
            old_name='section_body',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='contentpagesections',
            old_name='section_heading',
            new_name='heading',
        ),
    ]
