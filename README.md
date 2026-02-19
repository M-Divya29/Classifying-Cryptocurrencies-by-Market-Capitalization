# 📊 Classifying Cryptocurrencies by Market Capitalization

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://crypto-market-analysis-m-divya.streamlit.app/)

## 🔗 Live Dashboard
**Main Deployment Link:** [https://crypto-market-analysis-m-divya.streamlit.app/](https://crypto-market-analysis-m-divya.streamlit.app/)

---

## 📌 Project Overview
This project analyzes cryptocurrency market data from the January 2018 peak. It categorizes assets by market capitalization and evaluates short-term and weekly volatility to provide a structural overview of the market landscape.

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

## 📈 Analysis Highlights
1. **Market Capitalization**: Analysis of the top 10 coins and their total market dominance.
2. **24-Hour Volatility**: Identifies the biggest winners and losers in a single day.
3. **Weekly Volatility**: Reveals long-term trends over a 7-day period.
4. **Market Segmentation**: Categorizes coins into 'biggish' (>$300M), 'micro' ($50M-$300M), and 'nano' (<$50M) tiers.

## 🚀 Installation & Usage
```bash
git clone https://github.com/M-Divya29/Classifying-Cryptocurrencies-by-Market-Capitalization.git
p pip install -r requirements.txt
streamlit run app.py
```

---

## 👩‍💻 Author
**M. Divya Lalitha**
*   **GitHub**: [M-Divya29](https://github.com/M-Divya29)
*   **Project**: Cryptocurrency Market Analysis
