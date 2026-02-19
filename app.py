import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='Crypto Dashboard', layout='wide')

@st.cache_data
def load_data():
    df = pd.read_csv('coinmarketcap_06012018.csv')
    cap = df.query('market_cap_usd > 0')
    return df, cap

try:
    df, cap = load_data()
    st.title('ፃ Crypto Market Analysis')
    st.write('### Data Overview', df.head())
    
    # Market Cap Plot
    st.subheader('Top 10 Market Cap')
    cap10 = cap.head(10).set_index('id')
    fig, ax = plt.subplots()
    cap10['market_cap_usd'].plot.bar(ax=ax)
    st.pyplot(fig)
except Exception as e:
    st.error(f'Error: {e}')
