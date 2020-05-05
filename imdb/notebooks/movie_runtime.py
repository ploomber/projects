# +
import pandas as pd

# https://matplotlib.org/tutorials/introductory/customizing.html
from imdb_project import pipeline
import matplotlib.pyplot as plt
import matplotlib as mpl
# -

plt.style.use('ggplot')
mpl.rcParams['figure.figsize'] = (14, 8)

dag = pipeline.make()

df = pd.read_parquet(str(dag['clean_title_basics']))

df.head()

df = df[(df.titleType == 'movie') & (~df.runtimeMinutes.isna())]

genres = [c for c in df if c.startswith('genre_')]
genres = ['genre_Romance', 'genre_Action']

# +
ax = plt.gca()

sub = df[(df.startYear >= 1920) & (df.startYear < 2020)]

g = sub.groupby('startYear').runtimeMinutes
means = g.mean()
stds = g.std()

means.plot()

legends = ['All']

for genre in genres:
    sub[sub[genre]].groupby('startYear').runtimeMinutes.mean().plot(ax=ax)
    legends.append(genre)

# means.plot(yerr=stds, ax=ax, capsize=2)


ax.legend(legends)


# +
ax = plt.gca()

sub = df[(df.startYear >= 1920) & (df.startYear < 2020)]

g = sub.groupby('startYear').size()
g.plot()

sub[sub['Romance']].groupby('startYear').size().plot(ax=ax)
sub[sub['Musical']].groupby('startYear').size().plot(ax=ax)
# -

sub2 = sub[sub['Romance'] | sub['Crime'] | sub['Action']][['Crime', 'Romance', 'startYear', 'Action']]
g = sub2.groupby('startYear').sum()
g.plot.area(stacked=False)

g.sum(axis='columns')


