# Generated by Django 2.1 on 2018-08-15 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CostBasedOnHour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_hour', models.TimeField(unique=True)),
                ('end_hour', models.TimeField()),
                ('border_value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('cost_below', models.DecimalField(decimal_places=2, max_digits=15)),
                ('cost_above', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
    ]
