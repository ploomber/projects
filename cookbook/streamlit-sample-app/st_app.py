# %%
import streamlit as st
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
from ploomber.spec import DAGSpec
from pandas_profiling import ProfileReport

# %%
st.title('Ploomber pipeline visualizations')
dag = DAGSpec('pipeline.yaml').to_dag()

# %%
st.title('Raw data profiling')
raw_df = pd.read_csv(dag['get'].product['data'])
profile_raw = ProfileReport(raw_df, title="Raw Data Profiling Report")
st_profile_report(profile_raw)

# %%
st.title('Clean data profiling')
clean_df = pd.read_csv(dag['clean'].product['data'])
profile_clean = ProfileReport(clean_df, title="Clean Data Profiling Report")
st_profile_report(profile_clean)
