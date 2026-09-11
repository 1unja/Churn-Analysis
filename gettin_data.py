from load_data import df
from load_data import engine
from sql.query import query_full_data 
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_sql(query_full_data, engine)
data = data.drop(data.iloc[:, [-2]], axis=1)

plt.scatter(x = data['balance'], y = data['credit_score'])
plt.show()
print(data.dtypes)

