import sqlite3
from ploomber import DAG, with_env, SourceLoader
from ploomber.tasks import DownloadFromURL, SQLScript, PythonCallable
from ploomber.products import File, SQLiteRelation
from ploomber.clients import DBAPIClient
from ploomber.executors import Serial

from ploomber_lyrics import tasks


@with_env
def make(env, artist_name, language):
    artist_name_ = artist_name.lower().replace(' ', '_')

    dag = DAG(executor=Serial(False))

    loader = SourceLoader(path='sql', module='ploomber_lyrics')

    db_location = env.path.data / 'clean.db'

    client = DBAPIClient(sqlite3.connect,
                         {'database': db_location},
                         split_source=True)
    dag.clients[SQLScript] = client
    dag.clients[SQLiteRelation] = client

    t = DownloadFromURL(env.source.lyrics,
                        File(env.path.data / 'lyrics.db'),
                        dag, name='raw_db')

    t2 = DownloadFromURL(env.source.metadata,
                         File(env.path.data / 'metadata.db'),
                         dag, name='raw_metadata_db')

    t3 = DownloadFromURL(env.source.artist_tags,
                         File(env.path.data / 'artist_tags.db'),
                         dag, name='raw_artist_tags_db')

    top = SQLScript(loader['get_top_words.sql'],
                    SQLiteRelation(('top_words_{{artist_name_}}', 'table')),
                    dag,
                    params={'artist_name': artist_name,
                            'artist_name_': artist_name_})

    wc = PythonCallable(tasks.wordcloud,
                        File(env.path.data / (artist_name_ + '.png')),
                        dag,
                        params={'db_location': db_location,
                                'language': language})

    (t + t2 + t3) >> top >> wc

    return dag


if __name__ == '__main__':
    dag = make(artist_name='Pink Floyd', language=None)
    dag.build()
