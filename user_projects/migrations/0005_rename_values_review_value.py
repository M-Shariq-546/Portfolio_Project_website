# Generated by Django 4.2.3 on 2023-12-01 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_projects', '0004_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='values',
            new_name='value',
        ),
    ]