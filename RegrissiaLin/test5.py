import random
with open('FileToTwoArg') as f:
    a=f.read()
string = ""
for i in range(1,35):
    p = random.randint(0,1)
    y = i*83+p*9+i*200 + 200
    string += f"{i} {p} {y}\n"
with open('FileToTwoArg', 'w') as f:
    f.write(string)
x = input()
import QuadratPodObsh
with open('FileToTwoArg') as f:
    a=f.read().strip()
a=a.split('\n')
x = [list(map(float, a[i].split()[:-1])) for i in range(len(a))]
y = [float(a[i].split()[-1]) for i in range(len(a))]
b, tg = QuadratPodObsh.LinRegAbs(y,x)
print(b,tg)
paramRegul = 0.00001
for i in range(len(tg)):
    for _ in range(200):
        tg[i] *= 1 - paramRegul
print(b,tg)

print(tg[0]*x[0][0]+tg[1]*x[0][1]+b, y[0])
