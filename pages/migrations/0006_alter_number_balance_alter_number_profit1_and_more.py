# Generated by Django 4.2.3 on 2023-07-29 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_number_profit5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='number',
            name='balance',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='number',
            name='profit1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='number',
            name='profit2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='number',
            name='profit3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='number',
            name='profit4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='number',
            name='profit5',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
