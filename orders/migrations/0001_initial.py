# Generated by Django 5.0.6 on 2024-05-28 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('preparing', 'Preparing'), ('shipping', 'Shipping'), ('delivered', 'Delivered')], default='pending', max_length=10)),
                ('order_number', models.CharField(max_length=10, unique=True)),
                ('delivery_address', models.CharField(max_length=255)),
                ('payment_method', models.CharField(max_length=50)),
            ],
        ),
    ]
