# Generated by Django 5.0.2 on 2024-04-04 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_marca"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cor",
            options={"verbose_name": "Cor", "verbose_name_plural": "Cores"},
        ),
        migrations.RenameField(
            model_name="cor",
            old_name="descricao",
            new_name="nome",
        ),
    ]
