from sql.query import query_products_number
from functions.independence_fun import independece_chi2_test
from load_data import engine
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2




products_number_df = pd.read_sql(query_products_number, engine)
print(products_number_df)

############################################################################
#TESTING ON INDEPENDENCE
############################################################################


statistics, chi_sqr = independece_chi2_test(products_number_df,
                      'churned',
                      'total',
                      0.01,
                      deg = 3)


#effect size

effect_size = np.sqrt(statistics/np.sum(products_number_df['total']))

#p-value

p_value = chi2.sf(statistics, 1)


print('')
print(f'statistics: {statistics}', f' chi^2: {chi_sqr}')
print('p-value: ', np.round(p_value, 4))
print('effect size: ', np.round(effect_size, 4))





#plot


fig, ax = plt.subplots(figsize=(7, 4.5))

x = products_number_df.index.astype(str)
y = products_number_df["ratio"] * 100

bars = ax.bar(x, y, width=0.65)

ax.set_title("Churn rate by number of bank products", fontsize=14, pad=12)
ax.set_xlabel("Number of products")
ax.set_ylabel("Churn rate (%)")
ax.set_ylim(0, 110)

ax.grid(axis="y", alpha=0.25)
ax.set_axisbelow(True)

for bar, value in zip(bars, y):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value + 2,
        f"{value:.1f}%",
        ha="center",
        va="bottom",
        fontsize=10
    )

plt.tight_layout()
plt.show()