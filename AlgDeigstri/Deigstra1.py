def RecursDeigsrta(Start,needToFind):
    for x in info[Start]:
        newCost = info[Start][x] + Deigstra[Start][1]
        if newCost < Deigstra[x][1]:
            Deigstra[x] = [Start, newCost]
            RecursDeigsrta(x, needToFind)

info = {"Книга":{"Пластинка": 5,"Постер": 0}, "Пластинка": {"Гитара": 15, "Барабан": 20},"Постер":{"Гитара": 30, "Барабан":35},"Гитара":{"Пианино": 20},"Барабан":{"Пианино":10}, "Пианино":{}}
needToFind = "Пианино"
Start = "Книга"
Deigstra = {x: ["name",float("inf")] for x in info}
Deigstra[Start] = ["name", 0]

RecursDeigsrta(Start,needToFind)

x = needToFind
answer = ''
while x!=Start:
    answer = f" --> ({Deigstra[x][1]}){x}" + answer
    x = Deigstra[x][0]
print(f"{Start}{answer}")