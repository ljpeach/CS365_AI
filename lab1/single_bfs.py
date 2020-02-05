def single_bfs(initialState):
    frontier=[FrontierNode(initialState,None)]
    visitedLocations=[(frontier[0].state.mouseX,frontier[0].state.mouseY)]
    nodesExpanded=0
    while True:
        currentNode=frontier.pop(0)
        for i in range(4):
            nodesExpanded+=1
            temp=transitionFunction(currentNode.state,i)
            if goalTest(temp):
                return path(FrontierNode(temp,currentNode),nodesExpanded)
            if (temp.mouseX,temp.mouseY) not in visitedLocations:
                frontier.append(FrontierNode(temp,currentNode))
                visitedLocations.append((temp.mouseX,temp.mouseY))
        if len(frontier)==0:
            break
    return "No Path!!"