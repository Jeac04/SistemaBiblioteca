# Generated by Django 4.1.6 on 2023-03-11 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='carrera',
            field=models.CharField(choices=[('IS', 'Ingeniería de Software'), ('ISA', 'Ingenieía en Sistemas Automotrices'), ('IF', 'Ingenieía Financiera'), ('IN', 'Ingenieria en Nanotecnología'), ('ITA', 'Ingenieía en Tecnología Ambiental'), ('ILT', 'Ingeniería en Logistica y Transporte'), ('IM', 'Ingenieía en Mecatronica'), ('IAEV', 'Ingenieía en Animación y Efectos Visuales'), ('IAI', 'Ingenieía Agroindustrial'), ('IE', 'Ingenieía en Energía')], max_length=70),
        ),
    ]
