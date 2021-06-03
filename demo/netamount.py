# Calculate Net Amount

price = int(input("Enter price :"))
qty = int(input("Enter qty :"))
amount = price * qty
discount = amount * 0.10
gross_amount = amount - discount
tax = gross_amount * 0.05
net_amount = gross_amount + tax

print(f"Amount       : {amount:10.2f}")
print(f" - Discount  : {discount:10.2f}")
print(f"               ----------")
print(f"               {gross_amount:10.2f}")
print(f" + Tax       : {tax:10.2f}")
print(f"               ----------")
print(f"Net Amount   : {net_amount:10.2f}")
