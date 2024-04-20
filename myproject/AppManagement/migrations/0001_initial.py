# Generated by Django 5.0.3 on 2024-04-19 19:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Curso",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("codigo", models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Profesor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("apellido", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Alumno",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("apellido", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "cursos",
                    models.ManyToManyField(
                        related_name="alumnos", to="AppManagement.curso"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="curso",
            name="profesor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cursos",
                to="AppManagement.profesor",
            ),
        ),
    ]
