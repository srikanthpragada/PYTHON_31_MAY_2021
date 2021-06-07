pos_count = neg_count = 0
for i in range(5):
    num = int(input("Enter a number :"))
    if num >= 0:
        pos_count += 1
    else:
        neg_count += 1


print(f"Positive : {pos_count}, Negative : {neg_count}")
