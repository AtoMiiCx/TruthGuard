import pandas as pd
import manipulation as mp
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import text_treatment as tt

# https://www.kaggle.com/code/benroshan/fake-news-classifier-lstm/notebook

def main():

    clean_data = pd.read_csv('clean_data.csv')
    output_csv = "C:/Users/adrie/PycharmProjects/pythonProject/output_url.csv"
    url = "https://www.independent.co.uk/news/people/donald-trump-new-year-message-tweet-enemies-a7503346.html"
    article_csv = "C:/Users/adrie/PycharmProjects/pythonProject/article_brut.csv"

#------     MODEL PREPARATION     ------

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
    # Charger les nouvelles données à partir d'un fichier CSV
    # new_data = pd.read_csv('article_csv.csv', encoding='latin-1')

    # Prétraitement des nouvelles données
    new_data_clean = tt.clean_text(new_data)  # Utiliser la fonction clean_text du fichier text_treatment.py
    new_data_list = [new_data]  # Créer une liste contenant le texte du document
    new_data_vectorized = vectorizer.transform(new_data_list)  # Vectoriser la liste contenant le texte

    # Vectorisation des nouvelles données
    #new_data_vectorized = vectorizer.transform(new_data)

    # Prédiction de la véracité des nouvelles données
    predictions = model.predict(new_data_vectorized)
    print(predictions)


if __name__== "__main__":
    main()





