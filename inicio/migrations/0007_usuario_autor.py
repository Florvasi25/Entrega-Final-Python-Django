# Generated by Django 4.2.2 on 2023-07-12 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0006_delete_productos'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='autor',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
