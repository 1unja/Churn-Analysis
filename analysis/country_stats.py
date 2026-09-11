from sql.query import query_country
from functions.independence_fun import independece_chi2_test
from load_data import engine
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2




country_df = pd.read_sql(query_country, engine)


############################################################################
#TESTING ON INDEPENDENCE
############################################################################


statistics, chi_sqr = independece_chi2_test(country_df,
                      'churned',
                      'total',
                      0.01,
                      deg = 2)

print(country_df)
print(f'statistics: {statistics}', f' chi^2: {chi_sqr}')

 
############################################################################
#PLOTTING
############################################################################




plt.barh(country_df['country'], 
        (country_df['churned']/country_df['total']),
        align= 'edge')
plt.show()