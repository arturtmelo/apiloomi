# Generated by Django 4.2 on 2023-10-30 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0002_genero_filme_atores_filme_comentarios_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filme',
            name='avaliacao',
        ),
        migrations.AlterField(
            model_name='filme',
            name='estrelas',
            field=models.FloatField(blank=True, null=True),
        ),
    ]