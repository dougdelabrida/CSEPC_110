print("===========================")
print("===== Meal calculator =====")
print("===========================")

child_meal_price = float(input("\nWhat is the price of a child's meal? [number] \n"))
adult_meal_price = float(input("\nWhat is the price of an adult's meal? [number] \n"))
child_quantity = int(input("\nHow many children are there? [number] \n"))
adult_quantity = int(input("\nHow many adults are there? [number] \n"))
sales_tax_rate = float(input("\nWhat is the sales tax rate? [number] \n"))

subtotal = child_quantity * child_meal_price + adult_quantity * adult_meal_price
sales_tax = (subtotal * sales_tax_rate) / 100;
total = subtotal + sales_tax;

currency = "${:,.2f}"

print("\n===========================")
print(f"Subtotal:    {currency.format(subtotal)}")
print(f"Sales Tax:   {currency.format(sales_tax)}")
print(f"Total:       {currency.format(total)}")
print("===========================\n")

payment = float(input("What is the payment amount? "))
print(f"Change: {currency.format(payment - total)}")
