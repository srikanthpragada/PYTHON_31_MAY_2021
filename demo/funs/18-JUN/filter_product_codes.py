# Program to use filter to select valid product codes
product_codes = ["A2343B", "C4252dG", "A2453", "12343GFH", "X6426", "AdksngsnZ"]

def isvalidcode(code):
    return code[0].isupper() and code[-1].isupper()


for c in filter(isvalidcode, product_codes):
    print(c)
