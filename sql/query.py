query_full_data = '''
SELECT *,
CASE 
    WHEN churn = 'Yes' THEN 1
    WHEN churn = 'No' THEN 0
END AS churn_numeric
FROM customers;
'''

query_age_churned = '''
SELECT age
FROM customers
WHERE churn = 'Yes'
ORDER BY age;
'''

query_age_not_churned = '''
SELECT age
FROM customers
WHERE churn = 'No'
ORDER BY age;
'''

query_country = '''
SELECT
    country,
    SUM(churn = 'Yes') AS churned,
    COUNT(churn) AS total
FROM customers
GROUP BY country
ORDER BY -(total/churned); 
'''



query_credit_churned = '''
SELECT credit_score
FROM customers
WHERE churn = 'Yes'
ORDER BY credit_score;
'''

query_credit_not_churned = '''
SELECT credit_score
FROM customers
WHERE churn = 'No'
ORDER BY credit_score;
'''

query_balance_churned = '''
SELECT balance
FROM customers
WHERE churn = 'Yes'
ORDER BY balance;
'''

query_balance_not_churned = '''
SELECT balance
FROM customers
WHERE churn = 'No' 
ORDER BY balance;
'''



query_tenure_churned = '''
SELECT tenure
FROM customers
WHERE churn = 'Yes'
ORDER BY tenure;
'''

query_tenure_not_churned = '''
SELECT tenure
FROM customers
WHERE churn = 'No'
ORDER BY tenure;
''' 


query_estimated_salary_churned = '''
SELECT estimated_salary
FROM customers
WHERE churn = 'Yes'
ORDER BY estimated_salary;
'''

query_estimated_salary_not_churned = '''
SELECT estimated_salary
FROM customers
WHERE churn = 'No'
ORDER BY estimated_salary;
'''


query_products_number = '''
SELECT 
    SUM(CASE WHEN churn = 'Yes' THEN 1 END) AS churned,
    COUNT(churn) AS total,
    SUM(CASE WHEN churn = 'Yes' THEN 1 END)
    /COUNT(churn) AS ratio
FROM customers
GROUP BY products_number;
'''


query_gender = '''
SELECT
    gender,
    SUM(churn = 'Yes') AS churned,
    COUNT(churn) AS total,
    SUM(CASE WHEN churn = 'Yes' THEN 1 END)
    /COUNT(churn) AS ratio
FROM customers
GROUP BY gender;
'''


query_active_member = '''
SELECT
    active_member,
    SUM(churn = 'Yes') AS churned,
    COUNT(churn) AS total,
    SUM(CASE WHEN churn = 'Yes' THEN 1 END)
    /COUNT(churn) AS ratio
FROM customers
GROUP BY active_member;
'''


query_credit_card = '''
SELECT
    credit_card,
    SUM(churn = 'Yes') AS churned,
    COUNT(churn) AS total,
    SUM(CASE WHEN churn = 'Yes' THEN 1 END)
    /COUNT(churn) AS ratio
FROM customers
GROUP BY credit_card;
'''



query_balance = '''
SELECT balance,
        churn
FROM customers
ORDER BY balance;
'''