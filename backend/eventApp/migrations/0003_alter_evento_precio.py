# Generated by Django 5.0 on 2023-12-13 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventApp', '0002_alter_evento_fecha_alter_evento_titulo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10),
        ),
    ]
