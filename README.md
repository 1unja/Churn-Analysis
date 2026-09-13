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


### 5.1 Balance Analyse


The main problem is that customers with zero balance shift the distribution. 


<img width="800" height="250" alt="Screenshot 2026-09-13 at 14 38 45" src="https://github.com/user-attachments/assets/6585b225-949d-4114-a328-ea2f7c143d9c" />


After customers with empty balance were removed, it turned out, that there's no significant difference between distribution for people with positive balance, it 
also can be presented on graph.


<img width="700" height="354" alt="Screenshot 2026-09-13 at 14 39 12" src="https://github.com/user-attachments/assets/1300ab6a-b501-4e0f-a640-82a67a7f5b80" />









