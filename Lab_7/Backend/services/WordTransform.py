from wykop import WykopAPI
import time
import spacy
import services.WykopHandler as wh
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import spacy
import io
import base64



def generate_text_for_wordcloud(tag_name, number_of_pages, wpisy=None):
    if wpisy == None:
        wpisy = wh.get_posts_and_comments(tag_name, number_of_pages)
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

    wordcloud = WordCloud(width=300, height=200, background_color='#3A506B').generate(text)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    image_bytes = buf.getvalue()
    buf.close()
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')

    return image_base64



