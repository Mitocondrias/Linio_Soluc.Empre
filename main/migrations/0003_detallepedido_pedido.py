# Generated by Django 3.2.3 on 2021-06-04 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaCreacion', models.DateField()),
                ('estado', models.TextField()),
                ('fechaEntrega', models.DateField()),
                ('direccionEntrega', models.TextField()),
                ('tarifa', models.FloatField(default=0)),
                ('ubicacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.localizacion')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.FloatField()),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.pedido')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.producto')),
            ],
        ),
    ]
