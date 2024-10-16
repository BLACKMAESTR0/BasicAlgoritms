import matplotlib.pyplot as plt
from UrOut import  Out
with open('FileToTwoArg') as f:
    a=f.read()
string = ""
n = 10
for x in range(1,n):
    y = x
    for z in range(1, 4):
        string += f"{x**z} "
    string += f"{y}\n"
with open('FileNewPolinom', 'w') as f:
    f.write(string)

x = input()







import QuadratPodObsh
with open('FileNewPolinom') as f:
    a=f.read().strip()
a=a.split('\n')
x = [list(map(float, a[i].split()[:-1])) for i in range(len(a))]
y = [float(a[i].split()[-1]) for i in range(len(a))]
plt.scatter([x for x in range(1,n)], y)
plt.show()
b, tg = QuadratPodObsh.LinRegAbs(y,x)
print(b,tg)
paramRegul = 0.00001
for i in range(len(tg)):
    for _ in range(1000):
        if abs(tg[i]) < 0.001:
            tg[i] = 0
            break
        if tg[i] > 0:
            tg[i] -= paramRegul
        elif tg[i] < 0:
            tg[i] += paramRegul
print(b,tg)
NewY = []
for i in range(1,n):
    this = b
    for step in range(len(tg)):
        this += tg[step]*i**(step+1)
    NewY.append(this)
print(y)


print(Out(tg,b))
plt.scatter([x for x in range(1,n)], y)
plt.plot([x for x in range(1,n)], NewY)
plt.show()