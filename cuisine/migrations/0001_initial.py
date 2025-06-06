# Generated by Django 5.2 on 2025-04-10 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Recette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite_necessaire', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.ingredient')),
                ('plat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuisine.plat')),
            ],
        ),
        migrations.AddField(
            model_name='plat',
            name='ingredients',
            field=models.ManyToManyField(through='cuisine.Recette', to='stock.ingredient'),
        ),
    ]
