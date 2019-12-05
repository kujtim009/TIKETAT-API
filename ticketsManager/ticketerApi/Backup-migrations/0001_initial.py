# Generated by Django 2.2.5 on 2019-10-07 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Regjionet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emri', models.CharField(db_index=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reshtat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emri', models.CharField(db_index=True, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Ulset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ulsa', models.CharField(max_length=10)),
                ('statusi', models.BooleanField(default=False)),
                ('regjioni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketerApi.Regjionet')),
                ('reshti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketerApi.Reshtat')),
            ],
        ),
        migrations.CreateModel(
            name='Cmimet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmimi', models.DecimalField(db_index=True, decimal_places=2, max_digits=6)),
                ('regjioni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketerApi.Regjionet')),
                ('reshti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketerApi.Reshtat')),
            ],
        ),
    ]
