# Generated by Django 2.2.11 on 2020-03-25 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0018_delete_flightuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookFlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('flight', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=20)),
            ],
        ),
    ]
