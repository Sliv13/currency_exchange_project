# Generated by Django 4.2.1 on 2024-11-25 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_currency_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'ordering': ('code',)},
        ),
    ]
