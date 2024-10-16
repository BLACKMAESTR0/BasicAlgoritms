def RecDeigsrta(graph, costs, parents, Start, End):
    if Start == End:
        return
    for i in graph[Start]:
        newCost = costs[Start]+graph[Start][i]
        if costs[i] > newCost:
            costs[i] = newCost
            parents[i] = Start
            RecDeigsrta(graph, costs, parents, i,End)

def Out(graph, costs, parents, Start, End):
    if parents[End] == "name":
        print("No current ways")
    else:
        answer = ''
        x=End
        while x!=Start:
            answer = f" --> ({costs[x]}){x}" + answer
            x = parents[x]
        print(f"{Start}{answer}")