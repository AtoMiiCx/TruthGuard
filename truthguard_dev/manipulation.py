import pandas as pd
from dateutil import parser

import re
import string
import nltk

# processing and cleaning

def display_shape(fake_news, true_news):
    # display the shape of fake_news
    print("The shape of the data is (row, column):", fake_news.shape)
    print(fake_news.info())
    print("\n --------------------------------------- \n")
    # display the shape of true_news
    print("The shape of the data is (row, column):", true_news.shape)
    print(true_news.info())


def shape_fake(fake_news):
    fake_news['output'] = 0
    fake_news['news'] = fake_news['title'] + fake_news['text']
    fake_news = fake_news.drop(['title', 'text'], axis=1)
    fake_news = fake_news[['subject', 'date', 'news', 'output']]
    return fake_news


def shape_true(true_news):
    true_news['output'] = 1
    true_news['news'] = true_news['title'] + true_news['text']
    true_news = true_news.drop(['title', 'text'], axis=1)
    true_news = true_news[['subject', 'date', 'news', 'output']]
    return true_news


def clear_date(fake_news, true_news):
    fake_news=fake_news[fake_news.date.str.contains("Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec")]
    fake_news.loc[:, 'date'] = fake_news['date'].apply(parser.parse)
    true_news.loc[:, 'date'] = true_news['date'].apply(parser.parse)
    return fake_news, true_news


def append(fake_news, true_news):
    frames = [fake_news, true_news]
    news_dataset = pd.concat(frames)
    return news_dataset


# test processing

def copy_data(news_dataset):
    clean_news = news_dataset.copy()
    return clean_news


def review_cleaning(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text


def clean(clean_news):
    clean_news['news'] = clean_news['news'].apply(review_cleaning)
    return clean_news


def stop_word(clean_news):
    stop = nltk.corpus.stopwords.words("english")
    clean_news['news'] = clean_news['news'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop]))
    return clean_news


def export_to_csv(clean_news, new_csv):
    clean_news.to_csv(new_csv, index=False)

