# Generated by Django 3.2.13 on 2023-02-13 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_item_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='coupon_id',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='ID купона'),
        ),
        migrations.AlterField(
            model_name='tax',
            name='tax_id',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='ID такса'),
        ),
    ]
