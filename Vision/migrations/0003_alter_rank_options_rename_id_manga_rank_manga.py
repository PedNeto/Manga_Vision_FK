# Generated by Django 4.1.2 on 2023-02-08 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vision', '0002_remove_mangas_rank_rank'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rank',
            options={'verbose_name': 'Rank', 'verbose_name_plural': 'Ranks'},
        ),
        migrations.RenameField(
            model_name='rank',
            old_name='id_manga',
            new_name='manga',
        ),
    ]
