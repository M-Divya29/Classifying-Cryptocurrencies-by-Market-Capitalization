import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='Crypto Market Analysis', layout='wide')

@st.cache_data
def load_data():
    df = pd.read_csv('coinmarketcap_06012018.csv')
    cap = df.query('market_cap_usd > 0')
    return df, cap

try:
    dec6, cap = load_data()
    st.title('ፃ Crypto Market Analysis Dashboard')

    st.sidebar.header('Navigation')
    view = st.sidebar.selectbox('Choose Analysis', ['Data Overview', 'Market Capitalization', '24h Volatility', 'Weekly Volatility', 'Market Cap Classification'])

    if view == 'Data Overview':
        st.header('Project Data Overview')
        st.markdown('''
        1. **Data Source**: This dataset is a snapshot from CoinMarketCap taken on January 6, 2018, representing the market state during a historical peak.
        2. **Market Variables**: It contains key financial metrics including market cap, price, and 24h volume to measure liquidity and asset size.
        3. **Performance Metrics**: Percentage changes for both 24-hour and 7-day windows are provided for volatility comparisons.
        4. **Data Integrity**: The cleaning process identifies and removes entries with zero or missing market caps, ensuring accurate visualizations.
        5. **Categorization**: The data segments coins into tiers (biggish, micro, nano) based on specific USD thresholds for market fragmentation analysis.
        ''')
        st.dataframe(dec6.head(20))

    elif view == 'Market Capitalization':
        st.subheader('Top 10 market capitalization')
        cap10 = cap.head(10).set_index('id')
        cap10 = cap10.assign(market_cap_perc=lambda x: (x.market_cap_usd / cap.market_cap_usd.sum()) * 100)
        fig, ax = plt.subplots()
        cap10.market_cap_perc.plot.bar(ax=ax, color='orange')
        ax.set_ylabel('% of total cap')
        st.pyplot(fig)
        st.info('**Explanation**: This figure illustrates the concentration of market value, showing that the top 10 cryptocurrencies (led by Bitcoin) often represent a massive portion of the total market, highlighting the dominance of a few major players.')

    elif view == '24h Volatility':
        st.subheader('24 Hours top losers and winners')
        volatility = dec6[['id', 'percent_change_24h']].set_index('id').dropna().sort_values('percent_change_24h')
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
        volatility.percent_change_24h[:10].plot.bar(color='darkred', ax=axes[0], title='Top Losers')
        volatility.percent_change_24h[-10:].plot.bar(color='darkblue', ax=axes[1], title='Top Winners')
        st.pyplot(fig)
        st.info('**Explanation**: This chart identifies extreme short-term fluctuations, distinguishing between Top Winners and Top Losers to showcase the high-risk, high-reward nature of the crypto market in a single day.')

    elif view == 'Weekly Volatility':
        st.subheader('Weekly top losers and winners')
        volatility7d = dec6[['id', 'percent_change_7d']].set_index('id').dropna().sort_values('percent_change_7d')
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
        volatility7d.percent_change_7d[:10].plot.bar(color='darkred', ax=axes[0], title='Top Losers')
        volatility7d.percent_change_7d[-10:].plot.bar(color='darkblue', ax=axes[1], title='Top Winners')
        st.pyplot(fig)
        st.info('**Explanation**: By looking at a 7-day window, this figure filters out minor daily noise to reveal sustained price trends, helping identify growth momentum versus steady decline.')

    elif view == 'Market Cap Classification':
        st.subheader('Classification of coins by market cap')
        def capcount(q): return cap.query(q).count().id
        labels = ['biggish', 'micro', 'nano']
        values = [capcount('market_cap_usd > 300000000'), 
                  capcount('market_cap_usd > 50000000 and market_cap_usd < 300000000'),
                  capcount('market_cap_usd < 50000000')]
        fig, ax = plt.subplots()
        ax.bar(labels, values, color=['blue', 'green', 'red'])
        ax.set_ylabel('Number of coins')
        st.pyplot(fig)
        st.info('**Explanation**: This bar chart segments the market into tiers like biggish, micro, and nano, providing a structural overview of how many projects are established large-caps versus smaller, speculative ventures.')

except Exception as e:
    st.error(f'Error loading data: {e}')
