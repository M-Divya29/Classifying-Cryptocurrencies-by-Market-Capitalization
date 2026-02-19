import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('│ Classifying Cryptocurrencies')
df = pd.read_csv('coinmarketcap_06012018.csv')
st.write('### Data Preview', df.head())

st.sidebar.title('Navigation')
if st.sidebar.checkbox('Show Market Cap Plot'):
    fig, ax = plt.subplots()
    df.head(10).set_index('id')['market_cap_usd'].plot.bar(ax=ax)
    st.pyplot(fig)