# Generated by Django 3.2.13 on 2023-09-06 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contratacoesDoVasco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('posicao', models.CharField(choices=[('G', 'goleiro'), ('Z', 'zagueiro'), ('L', 'lateral'), ('M', 'meio-campo'), ('A', 'atacante')], max_length=1)),
                ('deOndeVeio', models.CharField(max_length=80)),
                ('valor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='craquesDoVasco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('posicao', models.CharField(choices=[('G', 'goleiro'), ('Z', 'zagueiro'), ('L', 'lateral'), ('M', 'meio-campo'), ('A', 'atacante')], max_length=1)),
                ('nGols', models.IntegerField()),
                ('tpDeContrato', models.CharField(choices=[('E', 'empréstimo'), ('T', 'tranferência')], max_length=1)),
            ],
        ),
    ]
