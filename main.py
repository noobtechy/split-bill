total_money = int(input("Total money used in event: "))
names = input("Enter the names of the people separated by spaces: ").split()
n = len(names)
budgets = []
for name in names:
    budget = input(f"Enter the budget for {name} (use 'unlimited' for no limit): ")
    if budget.lower() == 'unlimited':
        budgets.append(float('inf'))  
    else:
        budgets.append(float(budget))
average_cost = total_money / n   
payments = [0] * n     
remaining_money = total_money
for i in range(n):
    if budgets[i] != float('inf'): 
        payments[i] = min(average_cost, budgets[i])
        remaining_money -= payments[i]
unlimited_indices = [i for i, budget in enumerate(budgets) if budget == float('inf')]
if unlimited_indices:
    remaining_per_person = remaining_money / len(unlimited_indices)
    for i in unlimited_indices:
        payments[i] = remaining_per_person

for i, name in enumerate(names):
    print(f"{name} - {payments[i]}")        