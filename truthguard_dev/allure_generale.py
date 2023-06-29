import csv
from spellchecker import SpellChecker
from langdetect import detect
import pandas as pd

# Charger le fichier CSV
with open("article_csv.csv", "r") as file:
    reader = csv.reader(file)
    text = next(reader)[0]

# Détecter la langue du texte
lang = detect(text)

# Afficher la langue détectée
print("Langue détectée :", lang)

# Créer une instance de SpellChecker pour l'anglais
spell = SpellChecker(language=lang)

# Diviser le texte en mots
words = text.split()

# Vérifier l'orthographe de chaque mot
misspelled = spell.unknown(words)

# Afficher les mots mal orthographiés
for word in misspelled:
    print("Mot mal orthographié :", word)

"""def count_exclamation_points(text):
    count = 0
    for char in text:
        if char == '!':
            count += 1
    return count

exclamation_point = count_exclamation_points(text)
print(exclamation_point)"""
