class FrontierAstarNodeWithWeight(FrontierNode):
    def __init__(self,state,parent,weight,depth):
        super().__init__(state,parent)
        self.weight=weight
        self.depth=depth

def weightCalc(state,prizeLocation):
    return abs(state.mouseX-prizeLocation[0])+abs(state.mouseY-prizeLocation[1])
    
def binaryNodeSearch(array,start,stop,searchFor)
    if start>stop:
        return start
    middle=(stop+start)//2
    if array[middle].weight==searchFor:
        return middle
    elif array[middle].weight>searchFor:
        return binaryNodeSearch(array,start,middle-1,searchFor)
    else:
        return binaryNodeSearch(array,middle+1,stop,searchFor)

def single_astar(initialState,prizeLocation):
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
                return path(newNode,nodesExpanded)
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