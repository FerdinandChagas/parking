# Generated by Django 4.2.3 on 2024-10-25 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_cliente_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='cpf',
        ),
    ]
