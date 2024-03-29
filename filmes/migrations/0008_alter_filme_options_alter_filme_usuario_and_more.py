# Generated by Django 4.2 on 2023-11-04 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('filmes', '0007_filme_usuario_alter_filme_atores_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filme',
            options={'ordering': ['titulo']},
        ),
        migrations.AlterField(
            model_name='filme',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$yEA2y4TSrJ8WlOf5ciwP2S$Ub3mROi05/LgpovNJ8JSR9mnQjAxAkVb2bwS+wegoCg=', max_length=128),
        ),
    ]
