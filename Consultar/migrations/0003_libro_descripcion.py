# Generated by Django 4.1.6 on 2023-03-13 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Consultar', '0002_alter_libro_ingenieria'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='Descripcion',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
