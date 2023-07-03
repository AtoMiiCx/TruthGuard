import requests
import re
import nltk
from bs4 import BeautifulSoup
import csv

nltk.download('stopwords')

from nltk.corpus import stopwords

def nettoyer_url(url):
    # Récupérer le contenu HTML de l'URL
    response = requests.get(url, headers={'Accept-Encoding': 'utf-8'})
    html = response.text

    # Initialiser le parser BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Trouver toutes les balises <p> dans le contenu HTML
    balises_p = soup.find_all('p')

    # Extraire le texte de chaque balise <p>
    contenu_nettoye = ''.join(balise.get_text(strip=True) + ' ' for balise in balises_p).rstrip()

    return contenu_nettoye


def review_cleaning(text):
    punctuation_pattern = r'[,!"#$%&()*+,./:;<=>?@[\\]^_`{|}~]'
    return re.sub(punctuation_pattern, "", text)


def stop_word(content):
    stop = stopwords.words("english")
    content = ' '.join([word for word in content.split() if word not in stop])
    return content


def clean_text(texts):
    text = review_cleaning(texts)
    cleaned_text = stop_word(text)
    return cleaned_text
