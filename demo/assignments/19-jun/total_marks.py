marks_list = ["30,35,45",
              "55,60,60,abc",
              "90,,75",
              "1,2,3,4"]

for s in marks_list:
    smarks = filter(str.isdigit, s.split(","))
    marks = map(int, smarks)
    print(sum(marks))

