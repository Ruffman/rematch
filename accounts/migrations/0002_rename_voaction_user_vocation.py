# Generated by Django 4.0 on 2022-02-25 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='voaction',
            new_name='vocation',
        ),
    ]