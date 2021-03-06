# Generated by Django 2.2.11 on 2020-03-23 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0008_auto_20200323_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='famous',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.City'),
        ),
        migrations.AlterField(
            model_name='flights',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.City'),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.City'),
        ),
    ]
