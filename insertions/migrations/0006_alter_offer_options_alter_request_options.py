# Generated by Django 4.0 on 2022-01-19 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insertions', '0005_remove_request_offer_matches'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offer',
            options={'verbose_name': 'Offer'},
        ),
        migrations.AlterModelOptions(
            name='request',
            options={'verbose_name': 'Request'},
        ),
    ]