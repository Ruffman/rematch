# Generated by Django 4.0 on 2022-01-15 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insertions', '0003_alter_offer_user_alter_request_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='matches',
            new_name='offer_matches',
        ),
    ]