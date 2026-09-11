from sql.query import query_gender
from functions.independence_fun import independece_chi2_test
from load_data import engine
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2




gender_df = pd.read_sql(query_gender, engine)
print(gender_df)

############################################################################
#TESTING ON INDEPENDENCE
############################################################################


statistics, chi_sqr = independece_chi2_test(gender_df,
                      'churned',
                      'total',
                      0.01,
                      deg = 1)


#effect size

effect_size = np.sqrt(statistics/np.sum(gender_df['total']))

#p-value

p_value = chi2.sf(statistics, 1)


print('')
print(f'statistics: {statistics}', f' chi^2: {chi_sqr}')
print('p-value: ', np.round(p_value, 4))
print('effect size: ', np.round(effect_size, 4))





#plot


fig, ax = plt.subplots(figsize=(7, 4.5))

x = gender_df['gender']
y = gender_df["ratio"] * 100

bars = ax.bar(x, y, width=0.65)

ax.set_title("Churn rate by gender", fontsize=14, pad=12)
ax.set_xlabel("Gender")
ax.set_ylabel("Churn rate (%)")
ax.set_ylim(0, 40)

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