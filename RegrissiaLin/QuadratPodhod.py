import matplotlib.pyplot as plt
import FuncOfOshibok
n = 0.01
def tickLine(tg, b, x, y):
    global n
    b += (y - (tg*x+b)) * n
    tg += x*(y - (tg*x+b)) * n
    return (tg, b)

with open("FileToProstPodhod") as f:
    a=f.read().strip()
a=a.split("\n")
coord = [list(map(float,[a[i].split()[0],a[i].split()[1]])) for i in range(len(a))]
nachTg = 0.5
nachOtkl = 0
for i in range(250):
    for z in range(len(coord)):
        nachTg, nachOtkl = tickLine(nachTg, nachOtkl, coord[z][0], coord[z][1])
    yPogresh = FuncOfOshibok.RMSE([coord[x][0]*nachTg+nachOtkl for x in range(len(coord))],[coord[x][1] for x in range(len(coord))])
    plt.scatter(i, yPogresh)
plt.show()
print(nachTg*4+nachOtkl)
print(f"tg = {nachTg}, b = {nachOtkl}")
plt.scatter([4],[nachTg*4+nachOtkl])
plt.scatter([coord[x][0] for x in range(len(coord))],[coord[x][1] for x in range(len(coord))])
plt.plot([coord[0][0],coord[-1][0]], [nachTg*coord[0][0]+nachOtkl,nachTg*coord[-1][0]+nachOtkl])
plt.show()