# langleveltopics/migrations/0002_seed_initial_data.py
from django.db import migrations

def seed_initial_data(apps, schema_editor):
    Language = apps.get_model("langleveltopics", "Language")
    Level = apps.get_model("langleveltopics", "Level")
    Theme = apps.get_model("langleveltopics", "Theme")
    Topic = apps.get_model("langleveltopics", "Topic")
    Section = apps.get_model("langleveltopics", "Section")

    # --- Languages ---
    langs = {
        "de_DE": "Deutsch",
        "en_GB": "English",
        "es_ES": "Español",
        "ga_IE": "Gaeilge",
    }
    lang_objs = {}
    for iso, name in langs.items():
        lang_objs[iso] = Language.objects.create(iso_code=iso)

    # --- Levels ---
    levels = ["A1", "A2", "B1", "B2", "C1", "C2"]
    level_objs = {}
    for order, code in enumerate(levels, start=1):
        level_objs[code] = Level.objects.create(code=code, order=order)

    # --- Themes ---
    # Example: Adjectives and Adverbs theme in German
    theme = Theme.objects.create(
        language=lang_objs["de_DE"],
        key="adjectives_and_adverbs",
        native_name="Adjektive und Adverbien",
        foreign_names={"en_GB": "Adjectives and Adverbs", "es_ES": "Adjetivos y adverbios"}
    )

    # --- Topics ---
    topic1 = Topic.objects.create(
        theme=theme,
        level=level_objs["B1"],
        key="order_of_adjectives",
        native_name="Reihenfolge der Adjektive",
        foreign_names={"en_GB": "Order of adjectives", "es_ES": "Orden de los adjetivos"}
    )

    topic2 = Topic.objects.create(
        theme=theme,
        level=level_objs["B2"],
        key="order_of_less_common_adjectives",
        native_name="Reihenfolge seltenerer Adjektive",
        foreign_names={"en_GB": "Order of less common adjectives", "es_ES": "Orden de adjetivos menos comunes"}
    )

    # --- Sections ---
    Section.objects.create(
        topic=topic1,
        language=lang_objs["de_DE"],
        order=1,
        heading="Adjektive der Meinung, Größe, Farbe",
        text="Adjektive der Meinung, Größe und Farbe werden in folgender Reihenfolge geordnet: ..."
    )
    Section.objects.create(
        topic=topic1,
        language=lang_objs["en_GB"],
        order=2,
        heading=None,
        text="Adjectives of opinion, size, and color are ordered as follows: ..."
    )
    Section.objects.create(
        topic=topic2,
        language=lang_objs["de_DE"],
        order=1,
        heading="Seltenere Adjektive",
        text="Die Reihenfolge von seltenen Adjektiven folgt besonderen Regeln: ..."
    )

def unseed_initial_data(apps, schema_editor):
    Language = apps.get_model("langleveltopics", "Language")
    Level = apps.get_model("langleveltopics", "Level")
    Theme = apps.get_model("langleveltopics", "Theme")
    Topic = apps.get_model("langleveltopics", "Topic")
    Section = apps.get_model("langleveltopics", "Section")

    Section.objects.all().delete()
    Topic.objects.all().delete()
    Theme.objects.all().delete()
    Level.objects.all().delete()
    Language.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ("langleveltopics", "0002_make_heading_nullable"),
    ]

    operations = [
        migrations.RunPython(seed_initial_data, unseed_initial_data),
    ]
