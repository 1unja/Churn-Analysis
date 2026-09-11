import pandas as pd
from sqlalchemy import create_engine
from scipy.io import arff
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2
from scipy.stats import mannwhitneyu
import statsmodels.api as sm

arff_file = arff.loadarff('/Users/lunja/Desktop/Mathematics/dataset')
df = pd.DataFrame(arff_file[0])
df = df.map(lambda x: x.decode('utf-8') if isinstance(x, bytes) else x)

# print(df.dtypes)

user = "root"
password = "Deker-On223"
host = "localhost"
database = "churn_db"

engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}/{database}"
)

# отправка DataFrame в таблицу
# df.to_sql(
#     name="customers",
#     con=engine,
#     if_exists="replace",
#     index=False
# )

# print("Загружено строк:", len(df))


query_age = """ 
SELECT 
    age,
    SUM(churn = 'Yes') AS churned_cust, 
    COUNT(churn) AS tot_cust,
    ROUND(SUM(churn = 'Yes')/COUNT(churn), 4) AS churn_ratio
FROM customers
GROUP by  age;
"""

result = pd.read_sql(query_age, engine)

# print(result['age'])

# plt.hist(x = result['age'], y = result['churn_ratio'])
# plt.show()

x_label = np.array(result['age']).flatten()



order = np.argsort(x_label)
# print(order)


weigh_mean = (result["age"][order]*result['churn_ratio'][order]).sum()/result['churn_ratio'].sum()

weigh_var = (result).sum()/result['churn_ratio'].sum()

# print(weigh_mean)

# plt.plot(result["age"][order], result["churn_ratio"][order], marker="o")
# plt.xlabel("Age")
# plt.ylabel("Churn rate")
# plt.grid(True)
# plt.axvline(weigh_mean, color='green', linestyle='--')

# plt.bar(result['age'][order], result['churn_ratio'][order])
# plt.show()



query_countery = """
SELECT 
    country,
    SUM(churn = 'Yes') AS churned_cust, 
    COUNT(churn) AS tot_cust,
    ROUND(SUM(churn = 'Yes')/COUNT(churn), 4) AS churn_ratio
FROM customers
GROUP by  country;
"""

# result_countery = pd.read_sql(query_countery, engine)

# expected_churn_ratio = result_countery['tot_cust']*0.2037

# estimated = (
#     (result_countery["churned_cust"] - expected_churn_ratio) ** 2
#     / expected_churn_ratio
# ).sum()

# critical_01 = chi2.ppf(1 - 0.01, 2)

# print(estimated, critical_01)



query_gender = """
SELECT
    gender, 
    COUNT(churn) AS tot_cust,
    SUM(churn = 'Yes') AS churned,
    ROUND(SUM(churn = 'Yes')/COUNT(churn), 4) AS churn_ratio
FROM customers
GROUP by  gender;
"""

result_gender = pd.read_sql(query_gender, engine)

expected_churn_ratio_gender = result_gender['tot_cust']*0.2037

estimated_gender = (
    (result_gender["churned"] - expected_churn_ratio_gender) ** 2
    / expected_churn_ratio_gender
).sum()

critical_01 = chi2.ppf(1 - 0.01, 1)

# print(estimated_gender, critical_01)



U1 = """
SELECT age, churn
FROM customers
WHERE churn = 'Yes';
"""

U2 = """ 
SELECT age, churn
FROM customers
WHERE churn = 'No';
"""

U1_Yes = pd.read_sql(U1, engine)['age']
U2_No = pd.read_sql(U2, engine)['age']


U1, p = mannwhitneyu(U1_Yes, U2_No)

U2 = len(U1_Yes)*len(U2_No) - U1

# print(min(U1,U2), p, np.median(U1_Yes), np.median(U2_No))
# print(U1_Yes, result["age"])


# fig, axes = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5),
#                         layout="constrained")
# axes[0, 1].hist(U1_Yes, bins = 25)
# axes[0, 1].set_title("Churn = Yes")
# axes[0, 1].axvline(np.median(U1_Yes), color = 'red')


# axes[1, 1].hist(U2_No, bins = 25)
# axes[1, 1].axvline(np.median(U2_No), color = 'red')
# axes[1, 1].set_title("Churn = No")

# axes[1, 0].hist(result["age"])
# # axes[1, 0].xlabel("Age")
# # axes[1, 0].ylabel("Churn rate")
# axes[1, 0].grid(True)
# axes[1, 0].axvline(weigh_mean, color='green', linestyle='--')

# plt.show()











query_everything = '''
SELECT * 
FROM customers;
'''


result_everything = pd.read_sql(query_everything, engine)

# x_train = result_everything[['credit_score', 'country', 'gender', 'age', 'tenure', 'balance', 'products_number', 'credit_card', 'active_member', 'estimated_salary']]
x_train = result_everything[['credit_score', 'age', 'tenure', 'balance', 'products_number', 'credit_card', 'active_member', 'estimated_salary']]
y_train = result_everything['churn'].map({
    'Yes': 1,
    'No': 0
})
x_train["credit_card"] = x_train["credit_card"].map({
    "1": 1,
    "0": 0
})
x_train["active_member"] = x_train["active_member"].map({
    "1": 1,
    "0": 0
})

log_reg = sm.Logit(y_train, x_train).fit()


print(log_reg.params.index)

order_params = np.argsort(np.abs(log_reg.params.values))


# plt.barh(
#     log_reg.params.index[order_params],
#     np.abs(log_reg.params.values)[order_params],
#     color = 'green'
# )
# plt.yticks(rotation=45)

# plt.boxplot([U1_Yes , U2_No])
# plt.show()




