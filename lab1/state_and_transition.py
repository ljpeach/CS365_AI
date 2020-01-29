class StateRepresentation:
    def __init__(self,mouseX,mouseY,pCount,mazeList):
        self.mouseX=mouseX
        self.mouseY=mouseY
        self.prizeCount=pCount
        self.maze=mazeList
    def copy(self):
        mazeCopy=[None]*len(self.maze)
        for i in range(len(self.maze)):
            mazeCopy[i]=[None]*len(self.maze[i])
            for j in range(len(self.maze[i])):
                mazeCopy[i][j]=self.maze[i][j]
        return StateRepresentation(self.mouseX,self.mouseY,self.prizeCount,mazeCopy)
    def __eq__(self,other):
        if self.mouseX==other.mouseX and self.mouseY==other.mouseY and self.prizeCount==other.prizeCount and self.maze==other.maze:
            return True
        return False
def transitionFunction(state,direction):
    newState=state.copy()
    if direction==0:#0 is North
        if(newState.maze[newState.mouseX-1][newState.mouseY]!="%"):
            newState.mouseX-=1
            if newState.maze[newState.mouseX][newState.mouseY]==".":
                newState.prizeCount-=1
    if direction==1:#1 is East
        if(newState.maze[newState.mouseX][newState.mouseY+1]!="%"):
            newState.mouseX-=1
            if newState.maze[newState.mouseX][newState.mouseY]==".":
                newState.prizeCount-=1
    if direction==2:#2 is South
        if(newState.maze[newState.mouseX+1][newState.mouseY]!="%"):
            newState.mouseX-=1
            if newState.maze[newState.mouseX][newState.mouseY]==".":
                newState.prizeCount-=1
    if direction==3:#3 is West
        if(newState.maze[newState.mouseX][newState.mouseY-1]!="%"):
            newState.mouseX-=1
            if newState.maze[newState.mouseX][newState.mouseY]==".":
                newState.prizeCount-=1
    return newState
def goalTest(state):
    if state.prizeCount==0:
        return True
    return False