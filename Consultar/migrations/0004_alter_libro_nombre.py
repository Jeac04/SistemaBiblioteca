# Generated by Django 4.1.6 on 2023-03-24 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Consultar', '0003_libro_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='Nombre',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
