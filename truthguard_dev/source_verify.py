import pandas as pd


def get_complete_link(site_link):
    if site_link.startswith('http://') or site_link.startswith('https://'):
        return site_link
    else:
        return 'https://' + site_link


def get_site_status(url):
    # Charger le fichier CSV
    df = pd.read_csv('df_website.csv')

    url = get_complete_link(url)

    # Rechercher le statut du site correspondant au lien
    for _, row in df.iterrows():
        if pd.notna(row['Lien']) and url.startswith(row['Lien']):
            return row['Nom'], row['Status']

    # Si le site n'est pas trouvé dans la base de données
    return 'Unknown', 'Not found'


bdd_source = {
    'www.abcnews.go.com': {
        'nom': 'ABCnews',
        'fiable': True,
        'pays': 'USA'
    },
    'www.theage.com.au': {
        'nom': 'the Age',
        'fiable': True,
        'pays': 'Australie'
    },
    'www.afp.com': {
        'nom': 'Agence France Presse',
        'fiable': True,
        'pays': 'France'
    },
    'www.aljazeera.net': {
        'nom': 'Al Jazeera',
        'fiable': True,
        'pays': 'Quatar'
    },
    'www.amnesty.fr': {
        'nom': 'Amnesty International',
        'fiable': True,
        'pays': 'United Kingdom'
    },
    'www.adl.org': {
        'nom': 'Anti Defamation League',
        'fiable': True,
        'pays': 'USA'
    },
    'www.aon.com': {
        'nom': 'Aon',
        'fiable': True,
        'pays': 'United Kingdom'
    },
    'www.arstechnica.com': {
        'nom': 'ARS technica',
        'fiable': True,
        'pays': 'USA'
    },
    'www.apnews.com': {
        'nom': 'Associated Press',
        'fiable': True,
        'pays': 'USA'
    },
    'www.theatlantic.com': {
        'nom': 'The Atlantic',
        'fiable': True,
        'pays': 'USA'
    },
    'www.theaustralian.com': {
        'nom': 'The australian',
        'fiable': True,
        'pays': 'Australie'
    },
    'www.avclub.com': {
        'nom': 'The AV club',
        'fiable': True,
        'pays': 'USA'
    },
    'www.axios.com': {
        'nom': 'Axios',
        'fiable': True,
        'pays': 'USA'
    },
    'www.bbc.com': {
        'nom': 'BBC',
        'fiable': True,
        'pays': 'USA'
    },
    'www.bellingcat.com': {
        'nom': 'Bellingcat',
        'fiable': True,
        'pays': 'international'
    },
    'www.bloomberg.com': {
        'nom': 'Bloomberg',
        'fiable': True,
        'pays': 'USA'
    },
    'www.buzzfeednews.com': {
        'nom': 'BuzzFeed News',
        'fiable': True,
        'pays': 'USA'
    },
    'www.csmonitor.com': {
        'nom': 'Christian science monitor',
        'fiable': True,
        'pays': 'USA'
    },
    'www.climatefeedback.org': {
        'nom': 'Climate Feedback',
        'fiable': True,
        'pays': 'France'
    },
    'www.cnet.com': {
        'nom': 'CNET',
        'fiable': True,
        'pays': 'USA'
    },
    'www.cnn.com': {
        'nom': 'CNN',
        'fiable': True,
        'pays': 'USA'
    },
    'www.codamedia.com': {
        'nom': 'Coda Media',
        'fiable': True,
        'pays': 'USA'
    },
    'www.commonsensemedia.org': {
        'nom': 'Common sense media',
        'fiable': True,
        'pays': 'USA'
    },
    'www.theconversation.com': {
        'nom': 'The conversation',
        'fiable': True,
        'pays': 'Australie'
    },
    'www.telegraph.co.uk.com': {
        'nom': 'The daily telegraph',
        'fiable': True,
        'pays': 'United Kingdom'
    },
    'www.deadline.com': {
        'nom': 'Deadline Hollywood',
        'fiable': True,
        'pays': 'USA'
    },
    'www.deseret.com': {
        'nom': 'Deseret News',
        'fiable': True,
        'pays': 'USA'
    },
    'www.dw.com': {
        'nom': 'Deutsche Welle',
        'fiable': True,
        'pays': 'Allemagne'
    },
    'www.digitalspy.com': {
        'nom': 'Digital spy',
        'fiable': True,
        'pays': 'United Kingdom'
    },
    'www.economist.com': {
        'nom': 'The economist',
        'fiable': True,
        'pays': 'United Kingdom'
    },
    'www.iranicaonline.org': {
        'nom': 'encyclopedia iranica',
        'fiable': True,
        'pays': 'iran'
    },
    'www.engadget.com': {
        'nom': 'engadget',
        'fiable': True,
        'pays': 'international'
    },
    'www.ew.com': {
        'nom': 'entertainment weekly',
        'fiable': True,
        'pays': 'USA'
    },
    'www.ft.com': {
        'nom': 'Financial Times',
        'fiable': True,
        'pays': 'United Kingdom'
    },
    'www.forbes.com': {
        'nom': 'Forbes',
        'fiable': True,
        'pays': 'USA'
    },
    'www.foreignaffairs.com': {
        'nom': 'Foreign affairs',
        'fiable': True,
        'pays': 'USA'
    },
    'www.gamedeveloper.com': {
        'nom': 'Game developer',
        'fiable': True,
        'pays': 'USA'
    },
    'www.gameinformer.com': {
        'nom': 'Game informer',
        'fiable': True,
        'pays': 'USA'
    },
    'www.gizmodo.com': {
        'nom': 'gizmodo',
        'fiable': True,
        'pays': 'USA'
    },
    'www.theglobeandmail.com': {
        'nom': 'The Globe and mail',
        'fiable': True,
        'pays': 'Canada'
    },
    'www.theguardian.com': {
        'nom': 'The guardian',
        'fiable': True,
        'pays': 'United Kingdom'
    },
    'www.haaretz.com': {
        'nom': 'haaretz',
        'fiable': True,
        'pays': 'Israel'
    },
    'www.thehill.com': {
        'nom': 'The hill',
        'fiable': True,
        'pays': 'USA'
    },
    'www.thehindu.com': {
        'nom': 'The hindu',
        'fiable': True,
        'pays': 'India'
    },
    'www.hollywoodreporter.com': {
        'nom': 'The hollywood reporter',
        'fiable': True,
        'pays': 'USA'
    },
    'www.huffingtonpost.com': {
        'nom': 'The huffingtonpost',
        'fiable': True,
        'pays': 'USA'
    },
    'www.idolator.com': {
        'nom': 'The idolator',
        'fiable': True,
        'pays': 'USA'
    },
    'www.ign.com': {
        'nom': 'IGN',
        'fiable': True,
        'pays': 'USA'
    },
    'www.independant.co.uk': {
        'nom': 'The independent',
        'fiable': True,
        'pays': 'United Kingdom'
    },
    'www.indianexpress.com': {
        'nom': 'The indian express',
        'fiable': True,
        'pays': 'India'
    },
    'www.ipsnews.net': {
        'nom': 'Inter press service',
        'fiable': True,
        'pays': 'international'
    },
    'www.theintercept.com': {
        'nom': 'The intercept',
        'fiable': True,
        'pays': 'USA'
    },
    'www.jacobin.com': {
        'nom': 'jacobin',
        'fiable': True,
        'pays': 'USA'
    },
    'www.jamanetwork.com': {
        'nom': 'Jama network',
        'fiable': True,
        'pays': 'USA'
    },
    'www.thejc.com': {
        'nom': 'The jewish chronicle',
        'fiable': True,
        'pays': 'United Kingdom'
    },
    'www.kirkusreviews.com': {
        'nom': 'The kirkus reviews',
        'fiable': True,
        'pays': 'USA'
    },
    'www.latimes.com': {
        'nom': 'The Los Angeles Times',
        'fiable': True,
        'pays': 'USA'
    },
    'www.mg.co.za': {
        'nom': 'Mail and Guardian',
        'fiable': True,
        'pays': 'South Africa'
    },
    'www.themarysue.com': {
        'nom': 'The Mary Sue',
        'fiable': True,
        'pays': 'USA'
    },
    'www.metacritic.com': {
        'nom': 'The metacritic',
        'fiable': True,
        'pays': 'USA'
    },
    'www.monde-diplomatique.fr': {
        'nom': 'Le monde diplomatique',
        'fiable': True,
        'pays': 'France'
    },
    'www.motherjones.com': {
        'nom': 'Mother Jones',
        'fiable': True,
        'pays': 'USA'
    },
    'www.msnbc.com': {
        'nom': 'MSNBC',
        'fiable': True,
        'pays': 'USA'
    },
    'www.thenation.com': {
        'nom': 'The nation',
        'fiable': True,
        'pays': 'USA'
    },
    'www.nationalgeographic.com': {
        'nom': 'National Geographic',
        'fiable': True,
        'pays': 'USA'
    },
    'www.nbcnews.com': {
        'nom': 'NBC news',
        'fiable': True,
        'pays': 'USA'
    },
    'www.newrepublic.com': {
        'nom': 'The new republic',
        'fiable': True,
        'pays': 'USA'
    },
    'www.nymag.com': {
        'nom': 'The new york magazine',
        'fiable': True,
        'pays': 'USA'
    },
    'www.nydailynews.com': {
        'nom': 'New York daily news',
        'fiable': True,
        'pays': 'USA'
    },
    'www.nytimes.com': {
        'nom': 'The new york times',
        'fiable': True,
        'pays': 'USA'
    },
    'www.nzherald.co.nz': {
        'nom': 'New zealand herald',
        'fiable': True,
        'pays': 'New zealand'
    },
    'www.newslaundry.com': {
        'nom': 'newslaundry',
        'fiable': True,
        'pays': 'India'
    },
    'www.newsweek.com': {
        'nom': 'newsweek',
        'fiable': True,
        'pays': 'USA'
    },
    'www.purepeople.com': {
        'nom': 'people',
        'fiable': True,
        'pays': 'USA'
    },
    'www.playboy.com': {
        'nom': 'Playboy',
        'fiable': True,
        'pays': 'USA'
    },
    'www.politico.com': {
        'nom': 'politico',
        'fiable': True,
        'pays': 'USA'
    },
    'www.politifact.com': {
        'nom': 'politifact',
        'fiable': True,
        'pays': 'USA'
    },
    'www.polygon.com': {
        'nom': 'polygon',
        'fiable': True,
        'pays': 'USA'
    },
    'www.propublica.org': {
        'nom': 'propublica',
        'fiable': True,
        'pays': 'USA'
    },
    'www.qs.com': {
        'nom': 'quartz',
        'fiable': True,
        'pays': 'USA'
    },
    'www.rappler.com': {
        'nom': 'rappler',
        'fiable': True,
        'pays': 'Philipines'
    },
    'www.reason.com': {
        'nom': 'reason',
        'fiable': True,
        'pays': 'USA'
    },
    'www.theregister.com': {
        'nom': 'theregister',
        'fiable': True,
        'pays': 'United Kingdom'
    },
    'www.reuters.com': {
        'nom': 'reuters',
        'fiable': True,
        'pays': 'United Kingdom'
    },
    'www.rollingstone.com': {
        'nom': 'rolling stone',
        'fiable': True,
        'pays': 'USA'
    },
    'www.scientificamerican.com': {
        'nom': 'scientific american',
        'fiable': True,
        'pays': 'USA'
    },
    'www.scotusblog.com': {
        'nom': 'scotus blog',
        'fiable': True,
        'pays': 'USA'
    },
    'www.news.sky.com': {
        'nom': 'sky news',
        'fiable': True,
        'pays': 'United Kingdom'
    },
    'www.space.com': {
        'nom': 'space',
        'fiable': True,
        'pays': 'USA'
    },
    'www.spiegel.de': {
        'nom': 'der spiegel',
        'fiable': True,
        'pays': 'Germany'
    },
    'www.smh.com.au': {
        'nom': 'sydney morning herald',
        'fiable': True,
        'pays': 'australia'
    },
    'www.thewrap.com': {
        'nom': 'the wrap',
        'fiable': True,
        'pays': 'USA'
    },
    'www.time.com': {
        'nom': 'time',
        'fiable': True,
        'pays': 'USA'
    },
    'www.thetimes.co.uk': {
        'nom': 'the times',
        'fiable': True,
        'pays': 'United Kingdom'
    },
    'www.torrentfreak.com': {
        'nom': 'torrent freak',
        'fiable': True,
        'pays': 'USA'
    },
    'www.usnews.com': {
        'nom': 'usnews',
        'fiable': True,
        'pays': 'USA'
    },
    'www.usatoday.com': {
        'nom': 'USA today',
        'fiable': True,
        'pays': 'USA'
    },
    'www.vanityfair.com': {
        'nom': 'vanity fair',
        'fiable': True,
        'pays': 'USA'
    },
    'www.venturebeat.com': {
        'nom': 'venture beat',
        'fiable': True,
        'pays': 'USA'
    },
    'www.theverge.com': {
        'nom': 'the verge',
        'fiable': True,
        'pays': 'USA'
    },
    'www.vogue.com': {
        'nom': 'vogue',
        'fiable': True,
        'pays': 'USA'
    },
    'www.washingtonpost.com': {
        'nom': 'washington post',
        'fiable': True,
        'pays': 'USA'
    },
    'www.thewire.in': {
        'nom': 'the wire',
        'fiable': True,
        'pays': 'India'
    },
    'www.wired.co.uk': {
        'nom': 'wired',
        'fiable': True,
        'pays': 'United kingdom'
    },
    'www.news.yahoo.com': {
        'nom': 'yahoo news',
        'fiable': True,
        'pays': 'USA'
    },
    'www.zdnet.com': {
        'nom': 'zdnet',
        'fiable': True,
        'pays': 'USA'
    },

}
