try:
    num = int(input("Enter number :"))
    print(100 // num)
except ValueError as ex:
    print("Sorry!", ex)
# except ZeroDivisionError:
#     print("Sorry! Zero is not allowed!")
except Exception as ex:
    print("Error:", ex)
