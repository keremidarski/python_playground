# Problem description:
# https://leetcode.com/problems/bank-account-summary-ii/

SELECT name, SUM(amount) AS balance
FROM users AS u
JOIN transactions AS t
ON u.account = t.account
GROUP BY u.account
HAVING balance > 10000;
