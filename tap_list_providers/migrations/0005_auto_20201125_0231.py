# Generated by Django 3.1.2 on 2020-11-25 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tap_list_providers", "0004_auto_20201115_1459"),
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
                    ("arryved_embedded_menu", "Arryved Embedded Menu"),
                    ("arryved_pos_menu", "Arryved Point of Sale Menu"),
                ],
                max_length=50,
                unique=True,
            ),
        ),
    ]
