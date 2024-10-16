import QuadratPodObsh
with open("NewFile") as f:
    a=f.read()
a=a.split('\n')
yArr = [float(a[i].split()[0]) for i in range(len(a))]
xArr = [list(map(float, a[i].split()[1:])) for i in range(len(a))]
Otkl, weight = QuadratPodObsh.LinRegQuadr(yArr,xArr)
print(Otkl, weight)
print(Otkl + weight[0]*7)
