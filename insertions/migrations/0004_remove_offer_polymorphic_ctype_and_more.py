# Generated by Django 4.0 on 2022-02-03 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insertions', '0003_alter_object_address_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='polymorphic_ctype',
        ),
        migrations.RemoveField(
            model_name='request',
            name='polymorphic_ctype',
        ),
    ]
