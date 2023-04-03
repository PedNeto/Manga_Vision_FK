# Generated by Django 4.1.6 on 2023-02-21 20:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Vision", "0003_alter_rank_options_rename_id_manga_rank_manga"),
    ]

    operations = [
        migrations.CreateModel(
            name="store",
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
                ("titulo", models.CharField(max_length=100, verbose_name="Título")),
                (
                    "valor",
                    models.DecimalField(
                        decimal_places=2, max_digits=8, verbose_name="Valor"
                    ),
                ),
                (
                    "link_img",
                    models.CharField(max_length=255, verbose_name="Link da Imagem"),
                ),
                (
                    "link_vitrine",
                    models.CharField(max_length=255, verbose_name="Link do Produto"),
                ),
            ],
        ),
    ]
