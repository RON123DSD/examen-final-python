# Generated by Django 4.1.3 on 2022-12-06 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='nombre_catalogo',
            new_name='nombre_cliente',
        ),
    ]
