import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

gdp_df = pd.read_csv('data/gdppercapita_us_inflation_adjusted.csv')
life_df = pd.read_csv('data/life_expectancy_years.csv')
pop_df = pd.read_csv('data/population_total.csv')

gdp_cap = gdp_df['2007']
print(gdp_cap)


np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop*2

plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()

# Display the plot
plt.show()
