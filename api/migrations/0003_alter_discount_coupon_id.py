# Generated by Django 3.2.13 on 2023-02-12 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20230212_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='coupon_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='ID купона'),
        ),
    ]