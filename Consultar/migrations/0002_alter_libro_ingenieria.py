# Generated by Django 4.1.6 on 2023-03-13 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Consultar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='Ingenieria',
            field=models.CharField(max_length=70, null=True),
        ),
    ]