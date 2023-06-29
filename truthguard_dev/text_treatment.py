import requests
import re
import string
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import csv
import json
import random
import time

"""def get_article_content(url, output_csv):
    response = requests.get(url)
    content = response.text
    df = pd.DataFrame({'content': [content]})
    df.to_csv(output_csv, index=False)"""



"""def clean_html_in_csv(output_csv, article_csv):
    # Charger le fichier CSV
    df = pd.read_csv(output_csv)

    # Nettoyer le contenu HTML
    df['content'] = df['content'].apply(lambda x: BeautifulSoup(x, 'html.parser').get_text(separator=' '))

    # Enregistrer le DataFrame nettoyé dans un nouveau fichier CSV
    df.to_csv(article_csv, index=False)"""

def nettoyer_url(url, fichier_csv):
    # Récupérer le contenu HTML de l'URL
    response = requests.get(url, headers={'Accept-Encoding': 'utf-8'})
    html = response.text

    # Initialiser le parser BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Trouver toutes les balises <p> dans le contenu HTML
    balises_p = soup.find_all('p')

    # Extraire le texte de chaque balise <p>
    contenu_nettoye = ''.join(balise.get_text(strip = True) + ' ' for balise in balises_p).rstrip()

    contenu_nettoye = "McConnell says U.S. government shutdown DACA 'ridiculous'WASHINGTON (Reuters) - U.S. Senate Republican leader Mitch McConnell said Sunday would “ridiculous” fight Democrats immigration issues result standoff year-end spending bill prompt shutdown federal government. “There’s going government shutdown,” McConnell told ABC’s “This Week” program. “It’s going happen.” As tensions rise two parties spending bill, McConnell called Democrats’ position “untenable,” saying Congress March address status so-called Dreamers, young immigrants brought United States illegally children. With funding federal government due run Friday, Republican leaders need put together votes spending bill. But Democrats said insist protections Dreamers price support spending bill, setting stage potential showdown. “That’s ridiculous position,” McConnell told ABC. Although Republicans control chambers U.S. Congress, least Democratic votes needed pass spending bill. In September, Trump ended Deferred Action Childhood Arrivals, DACA, program, shields young illegal immigrants deportation. He gave Congress six months find solution. “I don’t think Democrats would smart say want shut government non-emergency address anytime March,” McConnell said. “That’s untenable position.” Trump Republican leaders want measures strengthening border enforcement accompany relief Dreamers, stance Democrats reject. McConnell said also optimistic House Senate Republicans could agree unified tax legislation send President Donald Trump Senate approved bill Saturday."

    return contenu_nettoye

    """
    # Écrire le contenu nettoyé dans un fichier CSV
    with open(fichier_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(contenu_nettoye)
    """
def review_cleaning(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

def stop_word(content):
    stop = stopwords.words("english")
    content = ' '.join([word for word in content.split() if word not in stop])
    return content

def clean_text(texts):
    cleaned_texts = []
    for text in texts:
        text = review_cleaning(text)
        text = stop_word(text)
        cleaned_texts.append(text)
    return cleaned_texts



