# Generated by Django 4.2.8 on 2023-12-22 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PageLogin', '0003_usuario_apellido_usuario_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carduser',
            name='cvv',
            field=models.IntegerField(max_length=3),
        ),
    ]
