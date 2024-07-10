def maximum_wealth(accounts):
    max_wealth_so_far = 0

    for account in accounts:
        current_customer_wealth = 0
        for money in account:
            current_customer_wealth += money
        max_wealth_so_far = max(max_wealth_so_far, current_customer_wealth)  

    return max_wealth_so_far

# Example usage
accounts = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 9]]
max_wealth = maximum_wealth(accounts)
print("Maximum Wealth:", max_wealth)
