# Generated by Django 2.0.6 on 2018-10-04 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20181003_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamodispositivo',
            name='cantidad',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='prestamodispositivo',
            name='detalle',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='prestamoip',
            name='cantidad',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='prestamoip',
            name='detalle',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='prestamosala',
            name='cantidad',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='prestamosala',
            name='detalle',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
