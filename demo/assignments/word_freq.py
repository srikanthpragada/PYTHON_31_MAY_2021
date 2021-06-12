st = "how do you do how did you do last year"

words = st.split(" ")
for w in set(words):
     print(f"{w:10}  {words.count(w)}")
