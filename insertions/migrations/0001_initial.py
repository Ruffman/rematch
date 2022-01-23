# Generated by Django 4.0 on 2022-01-23 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finance_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Object_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.IntegerField(default=0)),
                ('city_name', models.CharField(default='Default City', max_length=255)),
                ('street_name', models.CharField(default='Default Street Name', max_length=255)),
                ('street_number', models.IntegerField(default=0)),
            ],
        ),
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
                ('title', models.CharField(default='Default Title', max_length=127, verbose_name='Titel')),
                ('short_description', models.CharField(default='Default Short Description', max_length=255, verbose_name='Kurzbeschreibung')),
                ('number_adults', models.IntegerField(blank=True, null=True)),
                ('number_couples', models.IntegerField(blank=True, null=True)),
                ('number_children', models.IntegerField(blank=True, null=True)),
                ('number_pets', models.IntegerField(blank=True, null=True)),
                ('number_cars', models.IntegerField(blank=True, null=True)),
                ('number_homeoffice', models.IntegerField(blank=True, null=True)),
                ('number_kitchens', models.IntegerField(blank=True, null=True)),
                ('number_bathrooms', models.IntegerField(blank=True, null=True)),
                ('number_bedrooms', models.IntegerField(blank=True, null=True)),
                ('living_area', models.IntegerField(blank=True, null=True)),
                ('location_is_sunny', models.BooleanField(blank=True, default=False)),
                ('location_is_calm', models.BooleanField(blank=True, default=False)),
                ('location_at_hillside', models.BooleanField(blank=True, default=False)),
                ('location_near_public_transport', models.BooleanField(blank=True, default=False)),
                ('location_near_freeway', models.BooleanField(blank=True, default=False)),
                ('location_near_stores', models.BooleanField(blank=True, default=False)),
                ('location_near_recreation', models.BooleanField(blank=True, default=False)),
                ('location_near_education', models.BooleanField(blank=True, default=False)),
                ('location_has_nice_view', models.BooleanField(blank=True, default=False)),
                ('is_modern', models.BooleanField(blank=True, default=False)),
                ('is_built_sustainable', models.BooleanField(blank=True, default=False)),
                ('monthly_income', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('available_cash', models.DecimalField(blank=True, decimal_places=2, max_digits=17, null=True)),
                ('finance_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='insertions.finance_type', verbose_name='Wohnart')),
                ('object_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='insertions.object_address', verbose_name='Objektadresse')),
                ('object_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='insertions.object_type', verbose_name='Objektart')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
            options={
                'verbose_name': 'Request',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default='Default Title', max_length=127, verbose_name='Titel')),
                ('short_description', models.CharField(default='Default Short Description', max_length=255, verbose_name='Kurzbeschreibung')),
                ('number_adults', models.IntegerField(blank=True, null=True)),
                ('number_couples', models.IntegerField(blank=True, null=True)),
                ('number_children', models.IntegerField(blank=True, null=True)),
                ('number_pets', models.IntegerField(blank=True, null=True)),
                ('number_cars', models.IntegerField(blank=True, null=True)),
                ('number_homeoffice', models.IntegerField(blank=True, null=True)),
                ('number_kitchens', models.IntegerField(blank=True, null=True)),
                ('number_bathrooms', models.IntegerField(blank=True, null=True)),
                ('number_bedrooms', models.IntegerField(blank=True, null=True)),
                ('living_area', models.IntegerField(blank=True, null=True)),
                ('location_is_sunny', models.BooleanField(blank=True, default=False)),
                ('location_is_calm', models.BooleanField(blank=True, default=False)),
                ('location_at_hillside', models.BooleanField(blank=True, default=False)),
                ('location_near_public_transport', models.BooleanField(blank=True, default=False)),
                ('location_near_freeway', models.BooleanField(blank=True, default=False)),
                ('location_near_stores', models.BooleanField(blank=True, default=False)),
                ('location_near_recreation', models.BooleanField(blank=True, default=False)),
                ('location_near_education', models.BooleanField(blank=True, default=False)),
                ('location_has_nice_view', models.BooleanField(blank=True, default=False)),
                ('is_modern', models.BooleanField(blank=True, default=False)),
                ('is_built_sustainable', models.BooleanField(blank=True, default=False)),
                ('monthly_rent_price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('buy_price', models.DecimalField(blank=True, decimal_places=2, max_digits=17, null=True)),
                ('finance_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='insertions.finance_type', verbose_name='Wohnart')),
                ('object_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='insertions.object_address', verbose_name='Objektadresse')),
                ('object_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='insertions.object_type', verbose_name='Objektart')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
            options={
                'verbose_name': 'Offer',
            },
        ),
        migrations.CreateModel(
            name='Object_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('related_offer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='insertions.offer')),
                ('related_request', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='insertions.request')),
            ],
        ),
        migrations.CreateModel(
            name='Important_Address',
            fields=[
                ('object_address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='insertions.object_address')),
                ('related_offer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='insertions.offer')),
                ('related_request', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='insertions.request')),
            ],
            bases=('insertions.object_address',),
        ),
    ]
