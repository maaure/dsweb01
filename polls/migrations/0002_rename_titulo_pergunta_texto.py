# Generated by Django 4.2.1 on 2023-05-11 12:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pergunta",
            old_name="titulo",
            new_name="texto",
        ),
    ]
