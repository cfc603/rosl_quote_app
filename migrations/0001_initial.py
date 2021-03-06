# Generated by Django 3.0.7 on 2020-06-17 10:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('first_name', models.CharField(max_length=120, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=120, verbose_name='Last Name')),
                ('phone_number', models.CharField(help_text='eg. (386) 123-4567', max_length=14, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254)),
                ('street_1', models.CharField(max_length=250, verbose_name='Address Line')),
                ('street_2', models.CharField(blank=True, max_length=250, null=True, verbose_name='Address Line 2')),
                ('sent', models.BooleanField(default=False)),
                ('reviewed', models.BooleanField(default=False)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quote.City')),
                ('zip_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quote.ZIP', verbose_name='ZIP Code')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
