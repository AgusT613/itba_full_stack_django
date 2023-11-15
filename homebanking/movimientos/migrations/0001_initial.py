# Generated by Django 4.2.7 on 2023-11-14 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, null=True)),
                ('operation_type', models.CharField(blank=True, max_length=200, null=True)),
                ('movement_time', models.DateTimeField()),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuentas.cuenta')),
            ],
            options={
                'db_table': 'movimientos',
            },
        ),
    ]
