# List conprehension
case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "F"]

res = [a + b for a in case_1 for b in case_2]
print(res)

res2 = [[a + b for a in case_1] for b in case_2]
print(res2)
