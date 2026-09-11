from sql.query import query_balance_churned, query_balance_not_churned
from load_data import engine
from functions.independence_fun import independece_chi2_test
from functions.mann_whitney_fun import mann_whitney_test
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu
import numpy as np
from scipy.stats import chi2



query_balance_churned, query_balance_not_churned = (pd.read_sql(query_balance_churned, engine)['balance'],
                                                    pd.read_sql(query_balance_not_churned, engine)['balance'])




############################################################################
#TESTING ON INDEPENDENCE
############################################################################


result, new_df, effect_size = mann_whitney_test(u1 = query_balance_churned,
                                                u2 = query_balance_not_churned,
                                                group1_name = 'Churned',
                                                group2_name = 'Not churned')

print(f'p-value: {np.round(result.pvalue, 4)}')
print(f'u-statistic: {result.statistic}')
print(f'effect size: {np.round(effect_size, 4)}')
print(new_df)



############################################################################
#TESTING ON INDEPENDENCE
############################################################################



result, new_df, effect_size = mann_whitney_test(u1 = query_balance_churned[query_balance_churned != 0],
                                                u2 = query_balance_not_churned[query_balance_not_churned != 0],
                                                group1_name = 'Churned',
                                                group2_name = 'Not churned')

print(f'p-value: {np.round(result.pvalue, 4)}')
print(f'u-statistic: {result.statistic}')
print(f'effect size: {np.round(effect_size, 4)}')
print(new_df)



############################################################################
#TESTING ON INDEPENDENCE
############################################################################

# print(query_balance_churned.map(query_balance_churned == 0))



churned_by_zero = pd.DataFrame(
    {
        'amount of zero': [
            (query_balance_churned == 0).sum(),
            (query_balance_not_churned == 0).sum()
        ],
        'total': [
            len(query_balance_churned),
            len(query_balance_not_churned)
        ],
        'ratio': [
            (query_balance_churned == 0).sum()/len(query_balance_churned),
            (query_balance_not_churned == 0).sum()/len(query_balance_not_churned)
        ]        
    }, 
    index = ['churned', 'not churned']
)


statistics, chi_sqr = independece_chi2_test(churned_by_zero,
                                            'amount of zero',
                                            deg = 1)


#effect size

effect_size = np.sqrt(statistics/np.sum(churned_by_zero['total']))

#p-value

p_value = chi2.sf(statistics, 1)


print('')
print(f'statistics: {statistics}', f' chi^2: {chi_sqr}')
print('p-value: ', np.round(p_value, 4))
print('effect size: ', np.round(effect_size, 4))
print(churned_by_zero)




############################################################################
#PLOTTING
############################################################################



fig, axes = plt.subplots(ncols=2, nrows=3, figsize=(5.5, 3.5),
                        layout="constrained")

axes[0, 0].hist(query_balance_churned[query_balance_churned != 0], bins = 25)
axes[0, 0].set_xlabel("Balance")
axes[0, 0].set_title("Churn = Yes")
axes[0,0].axvline(
    np.median(query_balance_churned[query_balance_churned != 0]),
    color="red",
    label="Median"
)
axes[0,0].axvline(
    np.mean(query_balance_churned[query_balance_churned != 0]),
    color="green",
    label="Mean"
)
axes[0,0].legend()



axes[0, 1].hist(query_balance_not_churned[query_balance_not_churned != 0], bins = 25)
axes[0, 1].set_xlabel("Balance")
axes[0, 1].set_title("Churn = No")
axes[0, 1].axvline(
    np.median(query_balance_not_churned[query_balance_not_churned != 0]),
    color="red",
    label="Median"
)
axes[0, 1].axvline(
    np.mean(query_balance_not_churned[query_balance_not_churned != 0]),
    color="green",
    label="Mean"
)
axes[0, 1].legend()



axes[1, 0].hist(query_balance_churned, bins = 25)
axes[1, 0].set_xlabel("Balance (including zero)")
axes[1, 0].set_title("Churn = Yes")
axes[1, 0].axvline(
    np.median(query_balance_churned),
    color="red",
    label="Median"
)
axes[1, 0].axvline(
    np.mean(query_balance_churned),
    color="green",
    label="Mean"
)
axes[1, 0].legend()



axes[1, 1].hist(query_balance_not_churned, bins = 25)
axes[1, 1].set_xlabel("Balance (including zero)")
axes[1, 1].set_title("Churn = No")
axes[1, 1].axvline(
    np.median(query_balance_not_churned),
    color="red",
    label="Median"
)
axes[1, 1].axvline(
    np.mean(query_balance_not_churned),
    color="green",
    label="Mean"
)
axes[1, 1].legend()


axes[2, 0].boxplot([query_balance_churned[query_balance_churned != 0], query_balance_not_churned[query_balance_not_churned != 0]])
axes[2, 0].set_title("Churned vs Not churned")

axes[2, 1].barh(['churned', 'not churned'],
                churned_by_zero['ratio'])
axes[2, 1].set_title("comparing in zero")

plt.show()