from sql.query import query_age_churned, query_age_not_churned
from functions.mann_whitney_fun import mann_whitney_test
from load_data import engine
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu
import numpy as np


query_age_churned = pd.read_sql(query_age_churned, engine)
query_age_not_churned = pd.read_sql(query_age_not_churned, engine)

query_age_churned, query_age_not_churned = query_age_churned['age'], query_age_not_churned['age']


############################################################################
#TESTING ON INDEPENDENCE
############################################################################


result, new_df, effect_size = mann_whitney_test(u1 = query_age_churned,
                           u2 = query_age_not_churned,
                           group1_name = 'Churned',
                           group2_name = 'Not churned')

print(f'p-value: {np.round(result.pvalue, 4)}')
print(f'u-statistic: {result.statistic}')
print(f'effect size: {np.round(effect_size, 4)}')
print(new_df)



############################################################################
#PLOTTING
############################################################################



fig, axes = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5),
                        layout="constrained")

axes[0, 0].hist(query_age_churned, bins = 25)
axes[0, 0].set_xlabel("Age")
axes[0, 0].set_title("Churn = Yes")
axes[0,0].axvline(
    np.median(query_age_churned),
    color="red",
    label="Median"
)
axes[0,0].axvline(
    np.mean(query_age_churned),
    color="green",
    label="Mean"
)
axes[0,0].legend()



axes[0, 1].hist(query_age_not_churned, bins = 25)
axes[0, 1].set_xlabel("Age")
axes[0, 1].set_title("Churn = No")
axes[0, 1].axvline(
    np.median(query_age_not_churned),
    color="red",
    label="Median"
)
axes[0, 1].axvline(
    np.mean(query_age_not_churned),
    color="green",
    label="Mean"
)
axes[0, 1].legend()



axes[1, 0].boxplot([query_age_churned, query_age_not_churned])
axes[1, 0].set_title("Churn = Yes")

plt.show()