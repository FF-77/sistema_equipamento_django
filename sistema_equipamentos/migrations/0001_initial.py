# Generated by Django 3.1.7 on 2021-03-19 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('responsavel', models.CharField(max_length=120)),
                ('equipamento', models.CharField(max_length=100)),
                ('setor', models.CharField(choices=[('TI', 'Tecnológia Informação '), ('RH', 'Recursos Humanos'), ('GE', 'Gerência'), ('ES', 'Escritório'), ('PR', 'Produção')], max_length=2)),
                ('descricao', models.TextField()),
            ],
            options={
                'verbose_name': 'Cadastro',
            },
        ),
    ]
