# ፃ Classifying Cryptocurrencies by Market Capitalization

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://crypto-market-analysis-m-divya.streamlit.app/)

## ጓ Live Dashboard
**Access the live interactive analysis here:** [https://crypto-market-analysis-m-divya.streamlit.app/](https://crypto-market-analysis-m-divya.streamlit.app/)

---

## ጁ Project Overview
This project analyzes cryptocurrency market data from the January 2018 peak. It categorizes assets by market capitalization and evaluates short-term and weekly volatility to provide a structural overview of the market landscape.

## ጥ Data Overview
1. **Data Source**: A snapshot from CoinMarketCap (Jan 6, 2018) representing a historical market peak.
2. **Market Variables**: Includes market cap, price, and 24h volume to measure liquidity and size.
3. **Performance Metrics**: 24-hour and 7-day percentage changes for volatility comparison.
4. **Data Integrity**: Rows with missing or zero market capitalization are filtered out for accuracy.
5. **Categorization**: Segments coins into 'biggish', 'micro', and 'nano' tiers based on USD thresholds.

## ፃ Analysis Highlights

### 1. Market Capitalization Dominance
Illustrates the concentration of market value. The top 10 cryptocurrencies (led by Bitcoin) often represent a massive portion of the total market, highlighting the dominance of a few major players.

### 2. 24-Hour Volatility
Identifies extreme short-term fluctuations. Distinguishes between Top Winners and Top Losers to showcase the high-risk, high-reward nature of the crypto market in a single day.

### 3. Weekly Volatility Analysis
Filters out minor daily noise to reveal sustained price trends. This helps identify assets with growth momentum versus those in a steady decline over a 7-day window.

### 4. Market Cap Classification
Segments the market into tiers (biggish, micro, nano). This provides a structural overview of how many projects are established large-caps versus smaller, speculative ventures.

## ጒ Setup and Installation
```bash
git clone https://github.com/M-Divya29/Classifying-Cryptocurrencies-by-Market-Capitalization.git
pip install -r requirements.txt
streamlit run app.py
```
