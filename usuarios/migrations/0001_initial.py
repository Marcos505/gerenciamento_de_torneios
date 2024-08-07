# Generated by Django 5.0.7 on 2024-07-22 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('usu_id', models.AutoField(primary_key=True, serialize=False)),
                ('usu_nome', models.TextField(max_length=150)),
                ('usu_sobrenome', models.TextField(max_length=150)),
                ('usu_data_nascimento', models.DateField()),
                ('usu_celular', models.TextField(max_length=20)),
                ('usu_email', models.TextField(max_length=150)),
                ('usu_senha', models.TextField(max_length=150)),
            ],
        ),
    ]
