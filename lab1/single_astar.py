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
    visitedLocations=[(frontier[0].state.mouseX,frontier[0].state.mouseY)]
    nodesExpanded=0
    while True:
        currentNode=frontier.pop(0)
        for i in range(4):
            nodesExpanded+=1
            temp=transitionFunction(currentNode.state,i)
            newNode=FrontierAstarNodeWithWeight(temp,currentNode,weightCalc(temp,prizeLocation),currentNode.depth+1)
            if goalTest(temp):
                return path(newNode,nodesExpanded)
            if (temp.mouseX,temp.mouseY) not in visitedLocations:
                frontier.insert(binaryNodeSearch(frontier,0,len(frontier)-1,newNode.weight+newNode.depth),newNode)                
                visitedLocations.append((temp.mouseX,temp.mouseY))
        if len(frontier)==0:
            break
    return "No Path!!"