import sqlite3
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def wordcloud(upstream, product, db_location, language):
    conn = sqlite3.connect(db_location)

    query = 'SELECT * FROM {}'.format(upstream.first)
    df = pd.read_sql(query, conn)
    df.set_index('word', inplace=True)
    top = df[~df.index.isin(stopwords.words(language))]['count'].sort_values(ascending=False)[:10]
    wc = WordCloud()
    im = wc.generate_from_frequencies(top.to_dict())

    plt.imshow(im, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(str(product))

    conn.close()
