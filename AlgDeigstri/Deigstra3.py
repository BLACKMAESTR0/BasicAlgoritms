graph = {"start":{"A":10},"A":{"B":20},"B":{"C":1,"End":30},"C":{"A":1},"End":{}}
costs = {x:float("inf") for x in graph}
parents = {x:"name" for x in graph}
costs["start"] = 0

def Out(Start,End):
    if parents[End] == "name":
        print("No current ways")
    else:
        answer = ''
        x=End
        while x!=Start:
            answer = f" --> ({costs[x]}){x}" + answer
            x = parents[x]
        print(f"{Start}{answer}")

def RecDeigsrta(Start,End):
    if Start == End:
        return
    for i in graph[Start]:
        newCost = costs[Start]+graph[Start][i]
        if costs[i] > newCost:
            costs[i] = newCost
            parents[i] = Start
            RecDeigsrta(i,End)
RecDeigsrta("start","B")
print(parents)
Out("start","B")