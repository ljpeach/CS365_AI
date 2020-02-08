def multi_astar(state,prizeLocations):
    totalCost=0
    prizeNumber=1
    expanded=0
    while True: #weight tuple: cost, state
        minAstarWeight,expand=astarForMulti(removePrizes(state,prizeLocations,prizeLocations[0]),prizeLocations[0])
        expanded+=expand
        for i in range(1,len(prizeLocations)):
            newWeight,expand=astarForMulti(removePrizes(state,prizeLocations,prizeLocations[i]),prizeLocations[i])
            expanded+=expand
            #print("minWeight:",minAstarWeight[0])
            #print("newWeight:",newWeight[0])
            if newWeight[0]<minAstarWeight[0]:
                minAstarWeight=newWeight
        #print(minAstarWeight[1].mouseX,minAstarWeight[1].mouseY)
        prizeLocations.remove((minAstarWeight[1].mouseX,minAstarWeight[1].mouseY))
        state.maze[minAstarWeight[1].mouseX][minAstarWeight[1].mouseY]=" "
        state.mouseX=minAstarWeight[1].mouseX
        state.mouseY=minAstarWeight[1].mouseY
        state.prizeCount-=1
        if prizeNumber>9 and prizeNumber<36:
            state.maze[minAstarWeight[1].mouseX][minAstarWeight[1].mouseY]=chr(87+prizeNumber)
        elif prizeNumber>=36:
            state.maze[minAstarWeight[1].mouseX][minAstarWeight[1].mouseY]=chr(29+prizeNumber)
        else:
            state.maze[minAstarWeight[1].mouseX][minAstarWeight[1].mouseY]=prizeNumber
        totalCost+=minAstarWeight[0]
        prizeNumber+=1
        if goalTest(state):
            print("Nodes expanded:",expanded)
            print("Cost:",totalCost)
            state.printState()
            break
def removePrizes(state,prizes,prizeKeep):
    cleanState=state.copy()
    for i in prizes:
        if i != prizeKeep:
            cleanState.maze[i[0]][i[1]]=" "
    cleanState.prizeCount=1
    return cleanState
        

def astarForMulti(initialState,prizeLocation):
    frontier=[FrontierAstarNodeWithWeight(initialState,None,weightCalc(initialState,prizeLocation),0)]
    visitedLocations=[(frontier[0].state.mouseX,frontier[0].state.mouseY,frontier[0].depth+frontier[0].weight)]
    nodesExpanded=0
    while True:
        currentNode=frontier.pop(0)
        for i in range(4):
            nodesExpanded+=1
            temp=transitionFunction(currentNode.state,i)
            newNode=FrontierAstarNodeWithWeight(temp,currentNode,weightCalc(temp,prizeLocation),currentNode.depth+1)
            if goalTest(temp):
                return silentPath(newNode),nodesExpanded
            frontierAdd=True
            updated=False
            for i in range(len(visitedLocations)):
                if visitedLocations[i][0]==newNode.state.mouseX and visitedLocations[i][1]==newNode.state.mouseY:
                    if visitedLocations[i][2]<=newNode.weight+newNode.depth:
                        frontierAdd=False
                    else:
                        visitedLocations[i]=(newNode.state.mouseX,newNode.state.mouseY,newNode.weight+newNode.depth)
                    updated=True
                    break
            if not updated:
                visitedLocations.append((temp.mouseX,temp.mouseY,newNode.weight+newNode.depth))
            if frontierAdd:
                frontier.insert(binaryNodeSearch(frontier,0,len(frontier)-1,newNode.weight+newNode.depth),newNode) 
                """
                print("Frontier: ",end="")
                for i in frontier:
                    print(i.weight+i.depth,end=", ")
                print()
                """
        if len(frontier)==0:
            break
    return "No Path!!"

def silentPath(node):
    cost=-1
    currentNode=node
    while currentNode!=None:
        cost+=1
        currentNode=currentNode.parent
    return cost,node.state