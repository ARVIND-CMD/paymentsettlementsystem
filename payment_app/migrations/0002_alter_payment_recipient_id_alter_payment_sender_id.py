# Generated by Django 4.2.5 on 2023-09-21 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='recipient_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='payment',
            name='sender_id',
            field=models.CharField(max_length=100),
        ),
    ]
