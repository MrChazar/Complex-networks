from wykop import WykopAPI
import time
import spacy
import services.WykopHandler as wh



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

    """
    Próba zapisu
         buffer = io.BytesIO()
        plt.savefig(buffer, format='png', dpi=300, bbox_inches='tight')
        buffer.seek(0)
        files = {'file': ('wykres.png', buffer, 'image/png')}
    """
    return text



