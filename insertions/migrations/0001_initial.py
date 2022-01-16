# Generated by Django 4.0 on 2022-01-15 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Object_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=127)),
                ('short_description', models.CharField(max_length=255)),
                ('zip_code', models.IntegerField()),
                ('city_name', models.CharField(max_length=255)),
                ('street_name', models.CharField(max_length=255)),
                ('street_number', models.IntegerField()),
                ('living_area', models.IntegerField()),
                ('monthly_rent_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('buy_price', models.DecimalField(decimal_places=2, max_digits=17)),
                ('object_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='insertions.object_type', verbose_name='object type')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='request')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=127)),
                ('short_description', models.CharField(max_length=255)),
                ('zip_code', models.IntegerField()),
                ('city_name', models.CharField(max_length=255)),
                ('street_name', models.CharField(max_length=255)),
                ('street_number', models.IntegerField()),
                ('living_area', models.IntegerField()),
                ('monthly_rent_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('buy_price', models.DecimalField(decimal_places=2, max_digits=17)),
                ('object_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='insertions.object_type', verbose_name='object type')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='offer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]