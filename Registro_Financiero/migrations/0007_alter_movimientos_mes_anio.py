# Generated by Django 4.2.8 on 2024-02-06 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro_Financiero', '0006_alter_movimientos_mes_anio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimientos',
            name='mes_anio',
            field=models.CharField(max_length=7),
        ),
    ]
