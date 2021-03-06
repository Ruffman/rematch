# Generated by Django 4.0 on 2022-02-01 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('insertions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='True_Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insertions.offer')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insertions.request')),
            ],
        ),
        migrations.CreateModel(
            name='Request_Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_like_from_offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receivedLikeFrom', to='insertions.offer')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insertions.request')),
                ('sent_like_to_offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sentLikeTo', to='insertions.offer')),
            ],
        ),
        migrations.CreateModel(
            name='Proposed_Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insertions.offer')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insertions.request')),
            ],
        ),
        migrations.CreateModel(
            name='Offer_Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insertions.offer')),
                ('received_like_from_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receivedLikeFrom', to='insertions.request')),
                ('sent_like_to_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sentLikeTo', to='insertions.request')),
            ],
        ),
    ]
