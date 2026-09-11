import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
from sklearn.metrics import r2_score
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error

print(pd.__version__, 'hello')

data = pd.read_csv('/Users/lunja/Desktop/tolc/TRY1.csv', index_col = 0)

# print(data[data.iloc[:,0] > 70].iloc[:, 0])

# x = np.log(data.iloc[:, [1]])
# y = np.log(data.iloc[:, [0]])

x = data.iloc[:, [1]]
y = data.iloc[:, [0]]

x2 = np.log(data.iloc[:, [1]])
y2 = np.log(data.iloc[:, [0]])

x3 = data.iloc[:, [1]]
y3 = data.iloc[:, [0]]

x4 = np.log(data.iloc[:, [1]])
y4 = data.iloc[:, [0]]

# print([x,y])

# print(data.columns[0])


lm = linear_model.LinearRegression()

poly = PolynomialFeatures(degree = 2)

X_poly = poly.fit_transform(x)

lm.fit(X_poly,y)


lm_predicted = lm.predict(X_poly)

print(r2_score(y, lm_predicted))


X3 = sm.add_constant(x3)
model3 = sm.OLS(y3, X3).fit()
y3_pred = model3.predict(X3)
print(model3.summary())

X2 = sm.add_constant(x2)
model2 = sm.OLS(y2, X2).fit()
y2_pred = model2.predict(X2)
print(model2.summary())

X = sm.add_constant(X_poly)
model = sm.OLS(y, X).fit()
y_pred = model.predict(X)
print(model.summary())

X4 = sm.add_constant(x4)
model4 = sm.OLS(y4, X4).fit()
y4_pred = model4.predict(X4)


mse_df = pd.DataFrame(
    { 'MSE' : [mean_squared_error(y3, y3_pred),
               mean_squared_error(y, np.exp(y2_pred)),
               mean_squared_error(y, y_pred),
               mean_squared_error(y, y4_pred)],
      'R2' : [r2_score(y3, y3_pred),
              r2_score(y, np.exp(y2_pred)),
              r2_score(y, y_pred),
              r2_score(y, y4_pred)]

    },
    index = ['SIMP', 'LOG', 'POLY2', 'EXP']
)

y_pred = np.array(y_pred).flatten()
y2_pred = np.array(y2_pred).flatten()
y3_pred = np.array(y3_pred).flatten()
y4_pred = np.array(y4_pred).flatten()

print(mse_df)

order = np.argsort(x.iloc[:,0])

data.plot.scatter(x = data.columns[1], 
                  y = data.columns[0], 
                  alpha = 0.5)
plt.plot(x.iloc[order, 0], y_pred[order], color = 'red')
plt.plot(x.iloc[order, 0], np.exp(y2_pred)[order], color = 'green')
plt.plot(x.iloc[order, 0], y3_pred[order], color = 'yellow')
plt.plot(x.iloc[order, 0], y4_pred[order], color = 'orange')
plt.show()


