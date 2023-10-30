# Generated by Django 2.2 on 2019-04-09 01:46

from django.db import migrations


class Migration(migrations.Migration):
    replaces = [
        ("beers", "0025_auto_20190409_0145"),
        ("beers", "0026_auto_20190409_0146"),
    ]

    dependencies = [
        ("beers", "0024_populate_styles"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="beerstylecategory",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="beer",
            name="style",
        ),
        migrations.DeleteModel(
            name="BeerStyle",
        ),
        migrations.DeleteModel(
            name="BeerStyleCategory",
        ),
        migrations.DeleteModel(
            name="BeerStyleTag",
        ),
        migrations.RenameField(
            model_name="beer",
            old_name="new_style",
            new_name="style",
        ),
    ]
