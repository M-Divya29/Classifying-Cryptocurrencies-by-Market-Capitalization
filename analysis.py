import pandas as pd
import matplotlib.pyplot as plt

def run_analysis():
    df = pd.read_csv('coinmarketcap_06012018.csv')
    cap = df.query('market_cap_usd > 0')
    print('Data Loaded Successfully.')
    
    cap10 = cap.head(10).set_index('id')
    cap10['market_cap_usd'].plot.bar(title='Top 10 Market Cap')
    plt.ylabel('USD')
    plt.show()

if __name__ == '__main__':
    run_analysis()
