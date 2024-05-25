items = input().split("|")
budget = float(input())
bought_items = []
current_budget = budget
sum = 0
for item in items:
    current_item = item.split("->")
    if current_item[0] == "Clothes" and float(current_item[1]) <= 50 and current_budget >= float(current_item[1]):
        current_budget -= float(current_item[1])
        bought_items.append(float(current_item[1]) * 1.4)
    elif current_item[0] == "Shoes" and float(current_item[1]) <= 35 and current_budget >= float(current_item[1]):
        current_budget -= float(current_item[1])
        bought_items.append(float(current_item[1]) * 1.4)
    elif current_item[0] == "Accessories" and float ( current_item[1] ) <= 20.5 and current_budget >= float(current_item[1]):
        current_budget -= float ( current_item[1] )
        bought_items.append ( float ( current_item[1] ) * 1.4 )
for num in bought_items:
    sum += num
formatted_numbers = ["{:.2f}".format(num) for num in bought_items]
print(" ".join(map(str, formatted_numbers)))
print(f"Profit: {((budget-current_budget)*0.4):.2f}")
print("Hello, France!" if current_budget + sum >= 150 else "Not enough money.")


