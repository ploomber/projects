# +
from math import ceil
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import moviepy.editor as mpy

# + tags=["parameters"]
upstream = ['clean']
product = {
    'nb': 'output/plot.ipynb',
    'images': 'output/plot-images',
    'gif': 'output/final.gif'
}
# -

df_graph = pd.read_csv(upstream['clean']['df_graph'])
df_graph['Country Name'] = df_graph['Country Name'].astype('category')
df_graph['CO Emission'] = df_graph['CO Emission'].astype('float')
df_graph['Date'] = pd.to_datetime(df_graph['Date'], format="%Y")

df_graph.head()

df_plot = pd.read_csv(upstream['clean']['df_plot']).set_index('Date')

df_plot.head()

# Get legends order
leg_order = df_graph.sort_values(by=['Date', 'CO Emission'],
                                 ascending=[True, False],
                                 na_position='last')

# +
# Reset index
leg_order = leg_order.reset_index(drop=True)

# Replace countries name by order number
leg_order = leg_order.replace('Brazil', 0)
leg_order = leg_order.replace('Canada', 1)
leg_order = leg_order.replace('China', 2)
leg_order = leg_order.replace('France', 3)
leg_order = leg_order.replace('Germany', 4)
leg_order = leg_order.replace('India', 5)
leg_order = leg_order.replace('Italy', 6)
leg_order = leg_order.replace('Japan', 7)
leg_order = leg_order.replace('United Kingdom', 8)
leg_order = leg_order.replace('United States', 9)

# Set plot style
plt.style.use('fivethirtyeight')

# Auxiliar variables
k = 0
j = 10

Path(product['images']).mkdir(exist_ok=True)

footer = 'Source: World Bank\nMade with Ploomber (ploomber.io)'

# Plot png figures
for i in range(1, len(df_plot.index)):
    sub = df_plot.iloc[:i]
    ax = sub.plot(figsize=(10, 7),
                  color=[
                      '#173F5F', '#20639B', '#2CAEA3', '#F6D55C', '#ED553B',
                      '#EE1414', '#827498', '#420420', '#01A900', '#FF618C'
                  ],
                  linewidth=3)

    if len(sub.index) <= 10:
        ax.xaxis.set_ticks(sub.index)
    else:
        step = int(ceil(len(sub.index) / 10))
        ax.xaxis.set_ticks(sub.index[::step])

    ax.set_title("CO2 emissions (metric tons per capita) over time",
                 fontsize=18),
    ax.yaxis.set_label_position("right"),
    ax.yaxis.tick_right(),
    ax.set_xlabel('')

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(list(handles[l] for l in leg_order['Country Name'][k:j]),
              list(labels[l] for l in leg_order['Country Name'][k:j]),
              loc='upper left'),
    k = k + 10
    j = j + 10
    fig = ax.get_figure()
    fig.text(0.10, 0.04, footer, ha='left')
    fig.subplots_adjust(left=0.1, right=0.9, bottom=0.15, top=0.9)
    fig.savefig(str(Path(product['images'], f'{i}.png')), dpi=200)
# -

# Get files path
file_ord = []
for i in range(1, (len(df_plot) - 1)):
    file_ord.append(str(Path(product['images'], f'{i}.png')))

# +
# Create gif file
clip = mpy.ImageSequenceClip(file_ord, fps=4)
clip.write_gif(product['gif'])
