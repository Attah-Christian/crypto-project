# Generated by Django 4.2.3 on 2023-07-25 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btc_wallet', models.CharField(max_length=100)),
                ('eth_wallet', models.CharField(max_length=100)),
                ('usdterc20_wallet', models.CharField(max_length=100)),
                ('usdttrc20_wallet', models.CharField(max_length=100)),
            ],
        ),
    ]
