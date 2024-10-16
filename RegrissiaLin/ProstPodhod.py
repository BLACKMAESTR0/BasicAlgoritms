import matplotlib.pyplot as plt
with open("FileToProstPodhod") as f:
    a=f.read().strip()
a=a.split("\n")
coord = [list(map(float,[a[i].split()[0],a[i].split()[1]])) for i in range(len(a))]
nachTg = 1
nachOtkl = 0
n1 = 0.01
n2 = 0.01
for i in range(1000000):
    for z in range(len(coord)):
        if coord[z][1] >= nachTg*coord[z][0]:
            nachOtkl += n2
            if coord[z][0] >= 0:
                nachTg += n1
            else:
                nachTg -= n1
        else:
            nachOtkl -= n2
            if coord[z][0] >= 0:
                nachTg -= n1
            else:
                nachTg += n1

plt.scatter([coord[x][0] for x in range(len(coord))],[coord[x][1] for x in range(len(coord))])
plt.plot([0,coord[0][0],coord[-1][0]], [nachTg*0+nachOtkl,nachTg*coord[0][0]+nachOtkl,nachTg*coord[-1][0]+nachOtkl])
plt.show()
print(nachTg*4)