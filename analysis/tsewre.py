from sql.query import query_balance
from load_data import engine
from functions.independence_fun import independece_chi2_test
from functions.mann_whitney_fun import mann_whitney_test
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu
import numpy as np
from scipy.stats import chi2



balance_df = pd.read_sql(query_balance, engine)

balance_df['churn'] = balance_df['churn'].map(
  {'Yes': 1,
    'No': 0}
)


print(balance_df, len(balance_df['balance']))
print(balance_df.corr())

