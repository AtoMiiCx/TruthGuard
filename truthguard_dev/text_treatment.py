import requests
import re
import nltk
from bs4 import BeautifulSoup
import csv

nltk.download('stopwords')

from nltk.corpus import stopwords

def nettoyer_url(url, fichier_csv):
    # Récupérer le contenu HTML de l'URL
    response = requests.get(url, headers={'Accept-Encoding': 'utf-8'})
    html = response.text

    # Initialiser le parser BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Trouver toutes les balises <p> dans le contenu HTML
    balises_p = soup.find_all('p')

    # Extraire le texte de chaque balise <p>
    contenu_nettoye = ''.join(balise.get_text(strip=True) + ' ' for balise in balises_p).rstrip()

    # tranform contenu_nettoye en csv
    with open(fichier_csv, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([contenu_nettoye])
    # contenu_nettoye = 'Behind Democrats email leak, U.S. experts see Russian subplotWASHINGTON (Reuters) - If Russian government behind theft release embarrassing emails Democratic Party, U.S. officials suggested, may reflect less love Donald Trump enmity Hillary Clinton desire discredit U.S. political system. A U.S. official taking part investigation said intelligence collected hacking Democratic National Committee (DNC) emails released Wikileaks Friday “indicates beyond reasonable doubt originated Russia.” The timing eve Clinton’s formal nomination week Nov. 8 presidential election raised questions whether Russia may trying hurt her, help Trump, Republican rival, fan populist sentiment establishment politicians sought across Europe recent years. “Certainly Russia become master manipulating information strategic goals: Witness information bubble created threatening behavior Crimea, Ukraine elsewhere,” said former CIA National Security Agency director Michael Hayden. “A step like this, however, would really upping game.” The emails showed DNC officials explored ways undermine U.S. Senator Bernie Sanders’ presidential campaign Clinton raised questions whether Sanders, Jewish, really atheist. The disclosures confirmed Sanders’ frequent charge party played favorites clouded party convention Clinton hoped would signal unity, division. Two U.S. intelligence officials, speaking condition anonymity, said hack could part broader campaign Russian President Vladimir Putin push back thinks effort European Union NATO, military alliance European North American democracies, encircle weaken Russia. One officials called fear “a hangover” Putin’s service KGB, Soviet intelligence agency. “Time again, we’re seeing Russia push back Putin considers Russia’s mortal enemies,” said official. “He’s actively attacking U.S.-backed rebels Syria, buzzing ships planes Black Sea Baltic, mention invading Ukraine seizing Crimea. This fits pattern.” Despite Clinton’s short-lived attempt secretary state “reset” U.S.-Russian relations U.S. President Barack Obama took office 2009, leaked emails could damage candidate Kremlin may consider hostile benefit opponent, friendlier. Putin accused Clinton stirring protests rule December 2011 Russian parliamentary election marred allegations fraud, saying encouraged “mercenary” Kremlin foes criticizing vote. “She set tone opposition activists, gave signal, heard signal started active work,” Putin told supporters. Asked claims Russian intelligence hacked DNC obtain emails, Wikileaks founder Julian Assange told NBC News’ Richard Engel “there proof whatsoever” said “this diversion” pushed Clinton campaign. TRUMP’S WARMER TONEAnalysts said Russia’s goal may much broader simply meddling U.S. presidential election. “It’s gross oversimplification suggest Russian government all-in Donald Trump,” said Andrew Weiss, Russia analyst Carnegie Endowment International Peace, Washington-based think tank. “It’s Russia’s interest ... portray United States riven popular discontent, xenophobia high-level political corruption,” Weiss said. “It fits nicely Kremlin’s standard narrative ... White House rushes criticize others without getting house order.” The Russian leader may well encouraged Trump’s comments The New York Times last week White House, NATO might automatically defend Baltic states part Russian-led Soviet Union. Despite public Trump-Putin exchanges praise, Eugene Rumer, former national intelligence officer Russia Eurasia, warned reaching quick conclusions Putin’s view Trump. “We say degree confidence don’t like Hillary,” Rumer said. “It’s less clear like Trump, although years Russians said prefer deal Republicans – (that) kind hard-line deals.” A diplomat experience working Russia said Kremlin also might betting Clinton win sending shot across bow. “Messing like puts notice tough guys she’s got really careful with,” said diplomat, spoke condition anonymity. A U.S. intelligence official reviewing emails part investigation origin said emails describing privileges Democratic National Committee showers wealthiest donors bolster Russian narrative American political system rigged wealthy riddled corruption. “In addition countering U.S. narrative Russian government corrupt oligarchy, leaking emails fits rather conveniently Trump’s charges rigged system ‘crooked Hillary’,” said official, spoke condition anonymity discuss domestic politics.'
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
