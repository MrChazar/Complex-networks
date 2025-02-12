import numpy as np
import pandas as pd
import networkx as nx
from wykop import WykopAPI
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string
import time
import spacy
import io

api = WykopAPI("w55988974f3d3194b7dd98c7ab2c6765c2", "05f093e009943e9e9b911f2a8a9f1a00")
api.authenticate()


def generate_text_for_wordcloud(tag_name, number_of_pages):
    wpisy = []
    entries = api.make_request(f"tags/{tag_name}/stream?page=1&limit=25&sort=all&type=entry&multimedia=false'")
    entries = entries['data']
    a = 2
    # pobieranie tekstu
    while entries != []:
        for entry in entries:
            wpis = [entry['id'], entry['author']['username'], entry['content'], entry['tags']]
            wpisy.append(wpis)
            time.sleep(1)
            try:
                comments = api.make_request(f"entries/{entry['id']}/comments?page=1&limit=25")
            except:
                continue
            comments = comments['data']
            i = 2
            while comments != []:
                for comment in comments:
                    wpisy.append([comment['id'], comment['author']['username'], comment['content'], comment['tags']])
                try:
                    comments = api.make_request(f"entries/{entry['id']}/comments?page={i}&limit=25")
                except:
                    print("Przerwanie komentarzy")
                    break
                comments = comments['data']
                i += 1

        time.sleep(1)
        try:
            entries = api.make_request(f"tags/przegryw/stream?page={a}&limit=25&sort=all&type=entry&multimedia=false'")
            entries = entries['data']
        except:
            continue
        a += 1

        if a >= number_of_pages:
            break

    # przetwarzanie tekstu
    text = ""
    for a in wpisy:
        try:
            text += " " + a[2]
        except:
            continue
    text = text.replace("\n", " ")
    nlp = spacy.load("pl_core_news_sm")
    doc = nlp(text)
    cleaned_tokens = [token.lemma_.lower() for token in doc if
                      not token.is_stop and not token.is_punct and token.pos_ not in ["VERB", "AUX", "PRON"]]
    text = " ".join(cleaned_tokens)

    """
    Próba zapisu
         buffer = io.BytesIO()
        plt.savefig(buffer, format='png', dpi=300, bbox_inches='tight')
        buffer.seek(0)
        files = {'file': ('wykres.png', buffer, 'image/png')}
    """


    return {"text": text}



