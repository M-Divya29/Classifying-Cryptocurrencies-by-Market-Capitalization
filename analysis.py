# Reading datasets/coinmarketcap_06122017.csv into pandas
import pandas as pd
from matplotlib import pyplot as plt

dec6 = pd.read_csv('coinmarketcap_06012018.csv')
market_cap_raw = dec6[['id', 'market_cap_usd']]
print(market_cap_raw.count())

cap = market_cap_raw.query('market_cap_usd > 0')
print(cap.count())

TOP_CAP_TITLE = 'Top 10 market capitalization'
TOP_CAP_YLABEL = '% of total cap'
cap10 = cap.head(10).set_index('id')
cap10 = cap10.assign(market_cap_perc=lambda x: (x.market_cap_usd / cap.market_cap_usd.sum()) * 100)

ax = cap10.market_cap_perc.head(10).plot.bar(title=TOP_CAP_TITLE)
ax.set_ylabel(TOP_CAP_YLABEL)
plt.show()

COLORS = ['orange', 'green', 'orange', 'cyan', 'cyan', 'blue', 'silver', 'orange', 'red', 'green']
ax = cap10.market_cap_perc.head(10).plot.bar(title=TOP_CAP_TITLE, logy=True)
ax.set_ylabel('USD')
ax.set_xlabel('')
plt.show()

volatility = dec6[['id', 'percent_change_24h', 'percent_change_7d']]
volatility = volatility.set_index('id').dropna()
volatility = volatility.sort_values(['percent_change_24h'], ascending=True)
print(volatility.head())
