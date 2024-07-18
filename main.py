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
unlimited_people = [i for i in range(n) if budgets[i] == float('inf')]
if unlimited_people:
    remaining_per_person = remaining_money / len(unlimited_people)
    for i in unlimited_people:
        payments[i] = remaining_per_person
    remaining_money = 0  
for i in range(n):
    print(f"{names[i]} - {payments[i]}")

if remaining_money > 0:
    print(f"Remaining unpaid amount: {remaining_money}")
else:
    print("Total bill has been fully paid.")
