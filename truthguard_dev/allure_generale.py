import csv
from langdetect import detect
from spellchecker import SpellChecker

lang_dico = {
    "fr": "French",
    "en": "English",
    "de": "German",
    "it": "Italian",
    "es": "Spanish",
    "ru": "Russian",
    "ja": "Japanese",
}


def load_text_from_csv(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        text = next(reader)[0]
    return text


def detect_language(text):
    lang = detect(text)
    return lang_dico[lang]


def spellcheck_text(text, language):
    spell = SpellChecker(language=language)
    words = text.split()
    misspelled = spell.unknown(words)
    return misspelled
