# 📊 Classifying Cryptocurrencies by Market Capitalization

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://classifying-cryptocurrencies-by-market-capitalization-bjyn9rn4.streamlit.app/)

## 🔗 Live Dashboard
**Main Deployment:** [Interactive Crypto Analysis Dashboard](https://classifying-cryptocurrencies-by-market-capitalization-bjyn9rn4.streamlit.app/)

---

## 🎯 Project Objectives
*   **Wealth Distribution**: Quantify the market dominance of the top 10 cryptocurrencies.
*   **Volatility Profiling**: Compare short-term (24h) and mid-term (7d) price fluctuations to identify market risk.
*   **Asset Tiering**: Segment assets into scale-based categories (Biggish, Micro, Nano) for structural analysis.
*   **Data Visualization**: Transform raw historical data into actionable visual insights using Matplotlib and Streamlit.

## 🛠️ Technology Stack & Tools

| Category | Technologies |
| :--- | :--- |
| **Core Language** | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) |
| **Data Analysis** | ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) |
| **Visualization** | ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) |
| **Deployment** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white) |

## 📂 Project Structure
```text
.
├── app.py                      # Interactive Streamlit dashboard
├── analysis.py                 # Standalone Python analysis script
├── coinmarketcap_06012018.csv  # Historical dataset (Jan 2018)
├── requirements.txt            # Project dependencies
├── README.md                   # Documentation
└── images/                     # Generated analysis plots
    ├── fig1_marketcap.png
    ├── fig2_24h.png
    ├── fig3_weekly.png
    └── fig4_classification.png
```

## 📈 Analysis Insights

### 1️⃣ Market Capitalization Dominance
![Market Cap](images/fig1_marketcap.png)

### 2️⃣ Short-Term & Weekly Volatility
![24h Volatility](images/fig2_24h.png)

### 3️⃣ Market Segmentation
![Classification](images/fig4_classification.png)

## 🚀 Setup & Execution
```bash
git clone https://github.com/M-Divya29/Classifying-Cryptocurrencies-by-Market-Capitalization.git
pip install -r requirements.txt
streamlit run app.py
```

## 📌 Conclusion
This analysis of the January 2018 market peak reveals a highly concentrated ecosystem where a handful of 'Biggish' coins hold the majority of wealth, while hundreds of 'Nano' coins contribute to extreme market volatility. The project demonstrates the power of Python for financial data cleaning, categorization, and interactive reporting.

---

## 👩‍💻 Author
**M. Divya Lalitha**
*   **GitHub**: [M-Divya29](https://github.com/M-Divya29)
