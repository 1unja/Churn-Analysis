# Customer Churn Analysis

## 1. Project overview

The aim of this project is to identify and analyse factors associated with customer churn.

The analysis focuses on exploring relationships between customer characteristics and churn behaviour using statistical tests and data visualisation.

## 2. Dataset

The dataset used in this project is the Bank Customer Churn Dataset from https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset.

It contains 10,000 customer records and the following variables:

1. customer_id - unused variable.
2. credit_score - used as input.
3. country - used as input.
4. gender - used as input.
5. age - used as input.
6. tenure - used as input.
7. balance - used as input.
8. products - number, used as input.
9. credit_card - used as input.
10. active_member - used as input.
11. estimated_salary - used as input.
12. churn - used as the target.

## 3. Research questions

Statistical Questions

1. Which Customer characteristics associated with churn rate? 
2. Are these associations significant?
3. How strong are these associations? 
4. What conclusions can be drawn from the statistical analysis?

Modeling Questions

4. Which variables are significant predictors of churn in the logistic regression model?
5. How well does the logistic regression model performs?
6. How reliable is the model and how well does it generalise to unseen data?

## 4. Methods

## 5. Statistical Analysis


### 5.1 Balance Analysis 


The main issue is the presence of customers with zero balance. It creates a new problem for analysis, since the presence of these customers affects
the means and medians. Then it's reasonable to split the data on three parts: 
1. ''All customers''
2. ''Only positive balance customers''
3. ''Proportion of Zero-Balance Customers''.


<img width="800" height="250" alt="Screenshot 2026-09-13 at 14 38 45" src="https://github.com/user-attachments/assets/6585b225-949d-4114-a328-ea2f7c143d9c" />

&nbsp;

For the ''Only positive balance customers'' Mann-Whitney comparison test clearly shows no statistically significant difference between the distributions. This is also reflected on the graph, where medians appear to be similar.


<img width="580" height="250" alt="Screenshot 2026-09-13 at 14 39 12" src="https://github.com/user-attachments/assets/1300ab6a-b501-4e0f-a640-82a67a7f5b80" />

&nbsp;

For the ''Proportion of Zero-Balance Customers'' Chi-square test of independence presented a statistically significant difference between groups. Zero balance was more common among non-churned customers (39.1%) than among churned customers (24.5%).


<img width="350" height="250" alt="Screenshot 2026-09-13 at 15 02 40" src="https://github.com/user-attachments/assets/8764dc1a-f7c0-4a72-8484-0b7b50a7b23c" />

&nbsp;

Overall, the results suggest that the observed difference in the overall balance distributions is mainly driven by the presence of zero-balance customers. Among customers with a positive balance, the balance amount itself does not appear to be significantly associated with churn.


### 5.2 Products Number Analysis

This factor contains categorical numbers(from 1 to 4) represented amount of products for each customer. Chi-square test of independence showed a statistically very significant difference between categories. Analysis showed continuous growth of the percentage of churned customers with growth of 0.2771:

-  7.58 for 0 products
-  27.71 for 1 product
-  82.71 for 2 products
-  100.00 for 3 products

<img width="350" height="250" alt="Screenshot 2026-09-13 at 18 01 34" src="https://github.com/user-attachments/assets/c1552ca1-471a-4a5a-a3d5-b8b15ecc75bf" />

