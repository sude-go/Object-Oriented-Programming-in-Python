"""
Starting on page 144, we gave code to compute separate totals for the
deposits and withdrawals on a list of transactions. That code used a single for loop
with a nested if-else statement. Give an alternate implementation that achieves the
same end results using a single for loop and a single if statement (without use of an
else or elif clause).
"""

transactions = [('deposit', 100), ('withdrawal', 25), ('deposit', 200), ('withdrawal', 50)]
deposits = 0
withdrawals = 0

for transaction in transactions:
    if transaction[0] == 'deposit':
        deposits += transaction[1]
    else:
        withdrawals += transaction[1]

print("Deposits", deposits)
print("Withdrawals", withdrawals)

