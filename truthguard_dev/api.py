import csv
from flask import Flask, jsonify
from firebase_admin import credentials, firestore
import firebase_admin
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import text_treatment as tt
import allure_generale as ag
import source_verify as sv

app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("truthguard-firebase-adminsdk-a805b-055db633c1.json")
firebase_admin.initialize_app(cred)

# Connect to Firestore
db = firestore.client()

# Variable to keep track of whether data is already uploaded or not
data_uploaded = False


def csv_to_json(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data


articles_json = csv_to_json('clean_data.csv')


# Function to upload articles data to Firestore

def upload_articles_data(articles):
    global data_uploaded
    if not data_uploaded:

        # Upload each article as a document in the "articles" collection
        for article in articles:
            db.collection('articles').add(article)

        data_uploaded = True


def get_x_y():
    X = []  # List to store the "news" field
    Y = []  # List to store the "output" field

    # Query the Firestore collection to get all documents in the "articles" collection
    articles_ref = db.collection('articles')
    articles = articles_ref.stream()

    # Iterate through each article document and extract the "news" and "output" fields
    for article in articles:
        article_data = article.to_dict()
        X.append(article_data['news'])
        Y.append(article_data['output'])

    return X, Y


# Define a function to be executed before the first request
# @app.before_request
# def before_request():
#    upload_articles_data(articles_json)


@app.route('/verify', methods=['GET'])
def verify_article():
    url = input("enter the url you want to test :\n")
    article_csv = "C:/Users/esteb/OneDrive/Documents/Programming/Truthguard_true/TruthGuard/truthguard_dev/article_csv.csv"

    # ------     MODEL PREPARATION     ------

    # Diviser les données en ensemble d'entraînement et ensemble de test
    X, y = get_x_y()
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

    if int(predictions[0]) == 0:
        trueness = "article is fake"
    elif int(predictions[0]) == 1:
        trueness = 'article is true'
    else:
        trueness = 'cannot give prediction'

    # ------     ALLURE GENERALE     ------

    # Détecter la langue du texte
    lang = ag.detect_language(clean_data)

    # ------     VERIFY SOURCE     ------

    site, status = sv.get_site_status(url)

    return jsonify({
        'Prediction: ': trueness,
        'Detected language: ': lang,
        'The website ': site,
        'is ': status
    }, 200)


if __name__ == '__main__':
    app.run(debug=True)
