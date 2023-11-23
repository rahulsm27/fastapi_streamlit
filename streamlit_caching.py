
# ----------- CACHING IN STREAMLIT -----#
# Streamlit runs your script from top to bottom at every user interaction or code change. This execution model makes development super easy. But it comes with two major challenges:

# Long-running functions run again and again, which slows down your app.
# Objects get recreated again and again, which makes it hard to persist them across reruns or sessions.
# But don't worry! Streamlit lets you tackle both issues with its built-in caching mechanism. Caching stores the results of slow function calls, so they only need to run once. This makes your app much faster and helps with persisting objects across reruns.


# Two options
#st.cache_data is the recommended way to cache computations that return data: loading a DataFrame from CSV, transforming a NumPy array, querying an API, or any other function that returns a serializable data object (str, int, float, DataFrame, array, list, …). It creates a new copy of the data at each function call, making it safe against mutations and race conditions. The behavior of st.cache_data is what you want in most cases – so if you're unsure, start with st.cache_data and see if it works!

# st.cache_resource - is the recommended way to cache global resources like ML models or database connections – unserializable objects that you don't want to load multiple times


from time import sleep

import numpy as np
import pandas as pd
import streamlit as st
from transformers import pipeline

@st.cache_data#(ttl=)  us ttl time to live paramter..the objects remains in cache only for this time
def load_data(url:str) -> pd.DataFrame:
    return pd.read_csv(url)

df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")
# in first run it will load data.then it will 

@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

model = load_model()

text = st.text_input("type some text:")

if text:
    output = model(text)[0]
    st.write(output)


# max entries
@st.chache_data(max_entries=3) # only last 3 entries with differnet paramentes will be saved i
def get_data(inte:int) -> int :
    return inte*np.random.randn(1000)