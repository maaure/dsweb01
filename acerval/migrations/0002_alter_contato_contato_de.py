# Generated by Django 4.2.1 on 2023-07-03 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("acerval", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contato",
            name="contato_de",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="acerval.usuario"
            ),
        ),
    ]
