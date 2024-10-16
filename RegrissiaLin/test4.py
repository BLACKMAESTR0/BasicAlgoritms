import FuncOfOshibok
with open("FileTest") as f:
    a=f.read()
a=a.split("\n")
print(FuncOfOshibok.RMSE([float(a[i].split()[1]) for i in range(len(a))], [2*float(a[i].split()[0])+50 for i in range(len(a))]))