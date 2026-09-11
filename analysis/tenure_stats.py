from sql.query import query_tenure_churned, query_tenure_not_churned
from load_data import engine
from functions.mann_whitney_fun import mann_whitney_test
from functions.independence_fun import independece_chi2_test
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu
import numpy as np




query_tenure_churned, query_tenure_not_churned = (pd.read_sql(query_tenure_churned, engine)['tenure'],
                                                  pd.read_sql(query_tenure_not_churned, engine)['tenure'])




############################################################################
#TESTING ON INDEPENDENCE
############################################################################

result, new_df, effect_size = mann_whitney_test(u1 = query_tenure_churned,
                                                u2 = query_tenure_not_churned,
                                                group1_name = 'Churned',
                                                group2_name = 'Not churned')

print(f'p-value: {np.round(result.pvalue, 4)}')
print(f'u-statistic: {result.statistic}')
print(f'effect size: {np.round(effect_size, 4)}')
print(new_df)


############################################################################
#TESTING ON INDEPENDENCE
############################################################################


# statistics, chi_sqr = independece_chi2_test(products_number_df,
#                       'churned',
#                       'total',
#                       0.01,
#                       deg = 9)


# #effect size

# effect_size = np.sqrt(statistics/np.sum(products_number_df['total']))

# #p-value

# p_value = chi2.sf(statistics, 1)


# print('')
# print(f'statistics: {statistics}', f' chi^2: {chi_sqr}')
# print('p-value: ', np.round(p_value, 4))
# print('effect size: ', np.round(effect_size, 4))


############################################################################
#PLOTTING
############################################################################



fig, axes = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5),
                        layout="constrained")

axes[0, 0].hist(query_tenure_churned, bins = 25)
axes[0, 0].set_xlabel("tenure")
axes[0, 0].set_title("Churn = Yes")
axes[0,0].axvline(
    np.median(query_tenure_churned),
    color="red",
    label="Median"
)
axes[0,0].axvline(
    np.mean(query_tenure_churned),
    color="green",
    label="Mean"
)
axes[0,0].legend()



axes[0, 1].hist(query_tenure_not_churned, bins = 25)
axes[0, 1].set_xlabel("tenure")
axes[0, 1].set_title("Churn = No")
axes[0, 1].axvline(
    np.median(query_tenure_not_churned),
    color="red",
    label="Median"
)
axes[0, 1].axvline(
    np.mean(query_tenure_not_churned),
    color="green",
    label="Mean"
)
axes[0, 1].legend()



axes[1, 0].boxplot([query_tenure_churned, query_tenure_not_churned])
axes[1, 0].set_title("Churn = Yes")

plt.show()