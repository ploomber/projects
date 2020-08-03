import pandas as pd
import numpy as np

# + tags=["parameters"]
upstream = ['raw']
product = {
    'nb': 'output/clean.ipynb',
    'df_graph': 'output/clean_df_graph.csv',
    'df_plot': 'output/clean_df_plot.csv'
}
# -

df = pd.read_csv(upstream['raw']['data'], skiprows=2, header=1)
df.head()

# Filter dataset according to top DGP countries
topGDP = [
    'United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom',
    'France', 'Italy', 'Brazil', 'Canada'
]

df_top = df[df['Country Name'].isin(topGDP)]

# Remove last 4 columns of dataset
df_top = df_top.iloc[:, :-4]

# Creare CO Emission values
index = df_top.columns[5:]
CO_values = df_top['1960']

for x in index:
    CO_values = pd.concat([CO_values, df_top[x]])

# Create graph dataframe
df_graph = pd.DataFrame({
    'Date': np.repeat(df_top.columns[4:], 10),
    'Country Name': np.tile(df_top['Country Name'], 57),
    'CO Emission': CO_values
})

df_graph.head()

# Preparing df_graph for plot
df_plot = df_graph.pivot(index="Date",
                         columns="Country Name",
                         values="CO Emission")

df_plot.head()

df_graph.to_csv(product['df_graph'], index=False)
df_plot.to_csv(product['df_plot'])
