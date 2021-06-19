def getprice(st):
    parts = st.split(",")
    return int(parts[1])


products = ["p1,500", "p3,100", "p2,200", "p4,50"]

for s in sorted(products, key=lambda v: int(v.split(",")[1]), reverse=True):
    print(s)

for s in sorted(products, key=getprice, reverse=True):
    print(s)
