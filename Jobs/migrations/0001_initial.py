# Generated by Django 5.0 on 2023-12-24 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 12, 24, 14, 28, 58, 627951), verbose_name='created_at')),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100, verbose_name='tipo')),
                ('valor', models.CharField(max_length=255, verbose_name='valor')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 12, 24, 14, 28, 58, 626950), verbose_name='created_at')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('descricao', models.TextField(verbose_name='descricao')),
                ('status', models.BooleanField(default=True, verbose_name='status')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 12, 24, 14, 28, 58, 602950), verbose_name='created_at')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(verbose_name='descricao')),
                ('beneficio', models.TextField(verbose_name='beneficio')),
                ('titulo', models.CharField(max_length=100, verbose_name='titulo')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 12, 24, 14, 28, 58, 627951), verbose_name='created_at')),
            ],
        ),
    ]