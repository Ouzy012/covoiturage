# Generated by Django 3.1.1 on 2020-09-01 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=60)),
                ('nom', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Trajet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart', models.CharField(max_length=100)),
                ('arrivee', models.CharField(max_length=100)),
                ('prix', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.passager')),
                ('trajet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.trajet')),
            ],
        ),
        migrations.AddField(
            model_name='passager',
            name='passager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.personne'),
        ),
        migrations.CreateModel(
            name='Conducteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbre_place', models.IntegerField()),
                ('image_vehicule', models.CharField(max_length=100)),
                ('conducteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.personne')),
                ('trajet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.trajet')),
            ],
        ),
    ]
