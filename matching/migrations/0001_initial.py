# Generated by Django 4.0 on 2022-01-17 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('insertions', '0005_remove_request_offer_matches'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrueMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insertions.offer')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insertions.request')),
            ],
        ),
        migrations.CreateModel(
            name='RequestLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_like_from_offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receivedLikeFrom', to='insertions.offer')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insertions.request')),
                ('sent_like_to_offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sentLikeTo', to='insertions.offer')),
            ],
        ),
        migrations.CreateModel(
            name='ProposedMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insertions.offer')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insertions.request')),
            ],
        ),
        migrations.CreateModel(
            name='OfferLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insertions.offer')),
                ('received_like_from_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receivedLikeFrom', to='insertions.request')),
                ('sent_like_to_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sentLikeTo', to='insertions.request')),
            ],
        ),
    ]
