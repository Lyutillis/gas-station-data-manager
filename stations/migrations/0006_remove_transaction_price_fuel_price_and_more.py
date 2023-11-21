# Generated by Django 4.0.2 on 2023-11-16 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0005_alter_transaction_options_discount_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='price',
        ),
        migrations.AddField(
            model_name='fuel',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='total',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]