# Generated by Django 3.1.7 on 2021-05-15 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210515_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='boletos',
            name='subtotal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True),
        ),
    ]