# Generated by Django 5.0 on 2023-12-14 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_mobile_contact_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('cus_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('addr', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=15)),
                ('zip', models.CharField(max_length=10)),
                ('number', models.CharField(max_length=15)),
            ],
        ),
    ]
