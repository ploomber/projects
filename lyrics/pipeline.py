from ploomber import DAG, with_env
from ploomber.tasks import DownloadFromURL
from ploomber.products import File


@with_env
def make(env):
    dag = DAG()

    t = DownloadFromURL(env.source.lyrics,
                        File(env.path.data / 'lyrics.db'),
                        dag, name='raw_db')

    t2 = DownloadFromURL(env.source.metadata,
                         File(env.path.data / 'metadata.db'),
                         dag, name='raw_metadata_db')

    t3 = DownloadFromURL(env.source.artist_tags,
                         File(env.path.data / 'artist_tags.db'),
                         dag, name='raw_artist_tags_db')

    return dag


dag = make()
dag.build()


import sqlite3
import pandas as pd

conn = sqlite3.connect(str(dag['raw_metadata_db']))

conn.execute("attach database '{}' as artist_tag".format(str(dag['raw_artist_tags_db'])))
conn.execute("attach database '{}' as metadata".format(str(dag['raw_metadata_db'])))
conn.execute("attach database '{}' as lyrics".format(str(dag['raw_db'])))


query = """
select meta.track_id, term.* from artist_tag.artist_term term
join metadata.songs meta
using (artist_id)
limit 10;
"""

query = """
select meta.year, term.term, count(*)
from artist_tag.artist_term term
join metadata.songs meta
using (artist_id)
group by term.term
"""

query = """
with max_duration as (
select year, max(duration) as duration
from metadata.songs
group by year
)
select * from metadata.songs
join max_duration
using(year, duration)

"""

query = """
with track as (
    select * from metadata.songs
    where artist_name = 'Luis Miguel'
)

select *
from lyrics.lyrics
join track
using (track_id)
"""
df = pd.read_sql(query, conn)


import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
nltk.download('stopwords')


counts = df.groupby('word')['count'].sum()

top = counts[~counts.index.isin(stopwords.words('spanish'))].sort_values(ascending=False)[:10]

wc = WordCloud()
im = wc.generate_from_frequencies(top.to_dict())


import matplotlib.pyplot as plt
plt.imshow(im, interpolation='bilinear')
plt.axis("off")
plt.show()


df = df[df.year > 0]


df[df.year == 2008].sort_values(by='count(*)')
