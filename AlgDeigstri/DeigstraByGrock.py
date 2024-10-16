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
    for i in Start:
        newCost = graph[Start][i]+costs[Start]
        if newCost < costs[i]:
            costs[i] = newCost
            parents[i] = Start

graph = {"start": {"a":6,"b":2}, "a":{"fin":1},"b":{"a":3,"fin":5},"fin":{}}
costs = {"a":6,"b":2,"fin":float("inf")}
parents = {"a":"start","b":"start","fin":None}
processed = []
