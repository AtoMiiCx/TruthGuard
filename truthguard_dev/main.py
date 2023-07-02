import pandas as pd
import numpy as np
import manipulation as mp
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import text_treatment as tt
import allure_generale as ag
import source_verify as sv


def main():
    clean_data = pd.read_csv('clean_data.csv')
    output_csv = "C:/Users/adrie/PycharmProjects/pythonProject/output_url.csv"
    url = input("enter the url you want to test :\n")
    article_csv = "C:/Users/adrie\PycharmProjects\pythonProject\TruthGuard/truthguard_dev/article_csv.csv"

    # ------     MODEL PREPARATION     ------

    # Diviser les données en ensemble d'entraînement et ensemble de test
    X = clean_data['news']
    y = clean_data['output']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    # Vectorisation du texte avec TF-IDF
    vectorizer = TfidfVectorizer()
    X_train_vectorized = vectorizer.fit_transform(X_train)
    X_test_vectorized = vectorizer.transform(X_test)

    # Entraînement du modèle de régression logistique
    model = LogisticRegression()
    model.fit(X_train_vectorized, y_train)

    # Évaluation du modèle
    accuracy = model.score(X_test_vectorized, y_test)

    # -----    TEXT TREATMENT     -----

    new_data = tt.nettoyer_url(url, article_csv)

    # Prétraitement des nouvelles données

    clean_data = tt.clean_text(new_data)
    new_data_list = [clean_data]  # Créer une liste contenant le texte du document)
    new_data_vectorized = vectorizer.transform(new_data_list)

    # Prédiction de la véracité des nouvelles données
    predictions = model.predict(new_data_vectorized)

    if np.array_equal(predictions, [0]):
        print("article is fake")
    elif np.array_equal(predictions, [1]):
        print('article is true')
    else:
        print('cannot give prediction')

    # ------     ALLURE GENERALE     ------

    # Détecter la langue du texte
    lang = ag.detect_language(clean_data)

    # Afficher la langue détectée
    print("Detected language :", lang)

    # ------     VERIFY SOURCE     ------

    site, status = sv.get_site_status(url)
    print('the website ', site, ' is ', status)


if __name__ == "__main__":
    main()
