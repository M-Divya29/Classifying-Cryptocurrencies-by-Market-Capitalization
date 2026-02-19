# 📊 Classifying Cryptocurrencies by Market Capitalization

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://crypto-market-analysis-m-divya.streamlit.app/)

## 🔗 Live Dashboard
**Access the live interactive analysis here:** [https://crypto-market-analysis-m-divya.streamlit.app/](https://crypto-market-analysis-m-divya.streamlit.app/)

---

## 📌 Overview
This project provides an in-depth analysis of cryptocurrency market data from the early 2018 peak. It focuses on market capitalization dominance, volatility, and tiered classification of digital assets.

## 🎯 Key Objectives
*   **Market Concentration**: Analyze the dominance of the top 10 assets.
*   **Volatility Analysis**: Evaluate price fluctuations over 24-hour and 7-day windows.
*   **Market Segmentation**: Categorize coins into 'biggish', 'micro', and 'nano' tiers based on market cap.
*   **Interactive Visualization**: Provide a Streamlit-based dashboard for real-time data exploration.

## 🛠️ Technology Stack
*   **Language**: Python
*   **Libraries**: Pandas, Matplotlib, Streamlit
*   **Deployment**: Streamlit Community Cloud

## 📂 Project Structure
```text
.
├── app.py                      # Streamlit dashboard script
├── analysis.py                 # Core analysis script (standalone)
├── coinmarketcap_06012018.csv  # Historical market data
├── requirements.txt            # Dependency list
└── README.md                   # Project documentation
```

## 📈 Analysis Details
### 1. Market Capitalization
We visualize the concentration of wealth in the top 10 coins, primarily led by Bitcoin, to understand market dominance.

### 2. Price Volatility
We analyze the 'Top Winners' and 'Top Losers' for both 24-hour and 7-day periods to highlight the high-risk nature of the crypto ecosystem.

### 3. Coin Classification
Assets are segmented into:
*   **Biggish**: > $300M USD
*   **Micro**: $50M - $300M USD
*   **Nano**: < $50M USD

## 🚀 Installation & Usage
1. **Clone the repo**:
   ```bash
   git clone https://github.com/M-Divya29/Classifying-Cryptocurrencies-by-Market-Capitalization.git
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app**:
   ```bash
   streamlit run app.py
   ```
