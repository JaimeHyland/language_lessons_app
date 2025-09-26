from langleveltopics.models import Language, LangName

# Define human-readable names for each language
lang_names = {
    'de_DE': {'de_DE': 'Deutsch', 'en_GB': 'German', 'es_ES': 'Alemán', 'ga_IE': 'Gearmáinis', 'fr_FR': 'Allemand', 'eu': 'Alemana'},
    'en_GB': {'de_DE': 'Englisch', 'en_GB': 'English', 'es_ES': 'Inglés', 'ga_IE': 'Béarla', 'fr_FR': 'Anglais', 'eu': 'Inglesa'},
    'es_ES': {'de_DE': 'Spanisch', 'en_GB': 'Spanish', 'es_ES': 'Español', 'ga_IE': 'Spáinnis', 'fr_FR': 'Espagnol', 'eu': 'Espainiera'},
    'ga_IE': {'de_DE': 'Irisch', 'en_GB': 'Irish', 'es_ES': 'Irlandés', 'ga_IE': 'Gaeilge', 'fr_FR': 'Irlandais', 'eu': 'Irlandera'},
    'fr_FR': {'de_DE': 'Französisch', 'en_GB': 'French', 'es_ES': 'Francés', 'ga_IE': 'Fraincis', 'fr_FR': 'Français', 'eu': 'Frantsesa'},
    'eu':    {'de_DE': 'Baskisch', 'en_GB': 'Basque', 'es_ES': 'Vasco', 'ga_IE': 'Basca', 'fr_FR': 'Basque', 'eu': 'Euskara'},
}

# Fetch all Language objects and create a lookup dict
languages = {lang.iso_code: lang for lang in Language.objects.all()}

# Loop through each language and each translation
for lang_iso, translations in lang_names.items():
    lang_obj = languages[lang_iso]  # language being named
    for text_iso, name_text in translations.items():
        text_obj = languages[text_iso]  # language in which name is written
        # Create LangName record if it doesn't exist already
        LangName.objects.get_or_create(
            name_text=name_text,
            lang_iso=lang_obj,
            text_iso=text_obj
        )

print("LangName table populated successfully (duplicates skipped)!")
