# Generated by Django 4.2.3 on 2023-07-28 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='number',
            name='balance',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='number',
            name='profit1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='number',
            name='profit2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='number',
            name='profit3',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='number',
            name='profit4',
            field=models.CharField(max_length=100),
        ),
    ]
