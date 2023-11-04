# Generated by Django 4.2 on 2023-10-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('descricao', models.TextField(blank=True, max_length=200, null=True)),
                ('avaliacao', models.DecimalField(decimal_places=2, default=80.23, max_digits=5)),
            ],
        ),
    ]