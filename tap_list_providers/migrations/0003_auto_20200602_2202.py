# Generated by Django 3.0.4 on 2020-06-02 22:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tap_list_providers", "0002_apiratelimittimestamp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apiratelimittimestamp",
            name="api_type",
            field=models.CharField(
                choices=[
                    ("untappd", "Untappd"),
                    ("digitalpour", "DigitalPour"),
                    ("taphunter", "TapHunter"),
                    ("manual", "Chalkboard/Whiteboard"),
                    ("", "Unknown"),
                    ("test", "TEST LOCAL PROVIDER"),
                    ("stemandstein", "The Stem & Stein's HTML"),
                    ("taplist.io", "taplist.io"),
                    ("beermenus", "BeerMenus"),
                ],
                max_length=50,
                unique=True,
            ),
        ),
    ]
