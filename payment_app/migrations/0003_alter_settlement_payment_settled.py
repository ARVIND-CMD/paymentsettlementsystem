# Generated by Django 4.2.5 on 2023-09-25 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_app', '0002_alter_payment_recipient_id_alter_payment_sender_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settlement',
            name='payment_settled',
            field=models.BooleanField(default=True),
        ),
    ]