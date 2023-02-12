# Generated by Django 4.1.2 on 2023-01-07 02:34

import Vision.models
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VisionMangasGenre",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "vision_mangas_genre",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Chapter",
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
                ("capitulo", models.CharField(blank=True, max_length=150)),
                ("order", models.PositiveIntegerField()),
                ("texto", models.TextField(blank=True)),
            ],
            options={
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="FormContato",
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
                ("nome", models.CharField(max_length=150, verbose_name="Nome")),
                ("email", models.CharField(max_length=150, verbose_name="E-mail")),
                ("assunto", models.CharField(max_length=100, verbose_name="Assunto")),
                ("mensagem", models.TextField(verbose_name="Mensagem")),
                (
                    "data_envio",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data do Envio"
                    ),
                ),
                (
                    "resolvido",
                    models.BooleanField(default=False, verbose_name="Resolvido"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="genres",
            fields=[
                (
                    "id_gender",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("genero", models.CharField(max_length=150, verbose_name="Generos")),
            ],
            options={
                "verbose_name": "Genero",
                "verbose_name_plural": "Generos",
            },
        ),
        migrations.CreateModel(
            name="Pagina",
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
                ("pg_name", models.CharField(blank=True, max_length=150)),
                ("order", models.PositiveIntegerField()),
                (
                    "imagem",
                    stdimage.models.StdImageField(
                        force_min_size=False,
                        upload_to=Vision.models.page_directory_path,
                        variations={},
                        verbose_name="Paginas",
                    ),
                ),
                (
                    "capitulo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Vision.chapter"
                    ),
                ),
            ],
            options={
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="mangas",
            fields=[
                (
                    "id_manga",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                (
                    "modified",
                    models.DateField(auto_now=True, verbose_name="Data de Atualização"),
                ),
                ("finished", models.BooleanField(verbose_name="Finalizado")),
                (
                    "in_launch",
                    models.BooleanField(default=True, verbose_name="Lançamento"),
                ),
                ("Abandoned", models.BooleanField(verbose_name="Abandonado")),
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="Nome do Manga"
                    ),
                ),
                (
                    "author",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="Autor do Manga"
                    ),
                ),
                (
                    "release_Year",
                    models.IntegerField(blank=True, verbose_name="Data de Lançamento"),
                ),
                (
                    "type_manga",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Manga", "Manga"),
                            ("Webtoon", "Webtoon"),
                            ("Manhwa", "Manhwa"),
                            ("Manhua", "Manhua"),
                            ("Novel", "Novel"),
                            ("Webcomic", "Webcomic"),
                        ],
                        max_length=8,
                        verbose_name="Tipo",
                    ),
                ),
                (
                    "responsible_Group",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="Nome do Grupo"
                    ),
                ),
                ("sinopse", models.TextField(blank=True, verbose_name="Sinopse")),
                (
                    "capa",
                    stdimage.models.StdImageField(
                        force_min_size=False,
                        upload_to=Vision.models.manga_directory_path,
                        variations={},
                        verbose_name="Capas dos Mangas",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=150, unique=True, verbose_name="Slug"
                    ),
                ),
                ("rank", models.PositiveIntegerField(default=0)),
                ("genre", models.ManyToManyField(to="Vision.genres")),
            ],
            options={
                "verbose_name": "Manga",
                "verbose_name_plural": "Mangas",
            },
        ),
        migrations.CreateModel(
            name="MangaRating",
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
                ("rating", models.PositiveSmallIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "manga",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Vision.mangas"
                    ),
                ),
            ],
            options={
                "ordering": ["rating"],
            },
        ),
        migrations.CreateModel(
            name="ClickManga",
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
                ("data", models.DateField(auto_now_add=True)),
                (
                    "manga",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Vision.mangas"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="chapter",
            name="manga",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Vision.mangas"
            ),
        ),
    ]
