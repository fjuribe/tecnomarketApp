# Generated by Django 3.0.5 on 2020-12-06 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_clientes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='tipo_consulta',
            field=models.IntegerField(choices=[(0, 'consulta'), (1, 'reclamo'), (2, 'sugerencia'), (3, 'felicitaciones')]),
        ),
    ]