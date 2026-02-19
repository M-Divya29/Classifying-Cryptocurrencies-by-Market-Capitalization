# Reading datasets/coinmarketcap_06122017.csv into pandas
import pandas as pd
from matplotlib import pyplot as plt

dec6 = pd.read_csv('coinmarketcap_06012018.csv')
# Selecting the 'id' and the 'market_cap_usd' columns
market_cap_raw = dec6[['id', 'market_cap_usd']]
# Counting the number of values
print(market_cap_raw.count())

# Filtering out rows without a market capitalization
cap = market_cap_raw.query('market_cap_usd > 0')
# Counting the number of values again
print(cap.count())

#Declaring these now for later use in the plots
TOP_CAP_TITLE = 'Top 10 market capitalization'
TOP_CAP_YLABEL = '% of total cap'
# Selecting the first 10 rows and setting the index
cap10 = cap.head(10).set_index('id')
# Calculating market_cap_perc
cap10=cap10.assign(market_cap_perc=lambda x: (x.market_cap_usd / cap.market_cap_usd.sum()) * 100)
# Plotting the barplot with the title defined above
ax = cap10.market_cap_perc.head(10).plot.bar(title=TOP_CAP_TITLE)
# Annotating the y axis with the label defined above
ax.set_ylabel(TOP_CAP_YLABEL)
plt.show()

# Colors for the bar plot
COLORS = ['orange', 'green', 'orange', 'cyan', 'cyan', 'blue', 'silver', 'orange', 'red', 'green']
# Plotting market_cap_usd as before but adding the colors and scaling the y-axis
ax = cap10.market_cap_perc.head(10).plot.bar(title=TOP_CAP_TITLE, logy=True)
# Annotating the y axis with 'USD'
ax.set_ylabel('USD')
# Final touch! Removing the xlabel as it is not very informative
ax.set_xlabel('')
plt.show()

# Selecting the id, percent_change_24h and percent_change_7d columns
volatility = dec6[['id', 'percent_change_24h', 'percent_change_7d']]
# Setting the index to 'id' and dropping all NaN rows
volatility = volatility.set_index('id').dropna()
# Sorting the DataFrame by percent_change_24h in ascending order
volatility = volatility.sort_values(['percent_change_24h'], ascending=True)
# Checking the first few rows
print(volatility.head())
