# Generated by Django 4.2 on 2023-10-30 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('filmes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='filme',
            name='atores',
            field=models.ManyToManyField(blank=True, related_name='filmes_atuados', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='filme',
            name='comentarios',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='filme',
            name='data_de_lancamento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='filme',
            name='diretores',
            field=models.ManyToManyField(blank=True, related_name='filmes_dirigidos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='filme',
            name='estrelas',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='filme',
            name='favorito',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='filme',
            name='link_imagem',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='filme',
            name='roteiristas',
            field=models.ManyToManyField(blank=True, related_name='filmes_escritos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='filme',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='filme',
            name='descricao',
            field=models.TextField(blank=True, max_length=1200, null=True),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('imagem_perfil', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='filme',
            name='generos',
            field=models.ManyToManyField(blank=True, related_name='filmes', to='filmes.genero'),
        ),
    ]
