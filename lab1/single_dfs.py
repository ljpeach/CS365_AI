class FrontierNode:
    def __init__(self,state,parent):
        self.state=state
        self.parent=parent #Obj of FrontierNode
def path(node,nodesExpanded):#Takes a node, and returns directions
    cost=-1
    currentNode=node
    while currentNode!=None:
        cost+=1
        node.state.maze[currentNode.state.mouseX][currentNode.state.mouseY]="#"
        currentNode=currentNode.parent
    node.state.printState()
    print("Cost:",cost)
    print("Nodes expanded:", nodesExpanded)

def single_dfs(initialState):
    frontier=[FrontierNode(initialState,None)]
    visitedLocations=[(frontier[0].state.mouseX,frontier[0].state.mouseY)]
    nodesExpanded=0
    while True:
        currentNode=frontier.pop()
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