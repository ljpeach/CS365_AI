'''
Roger Lu, Liam Peachey, Yanzhi Li
CS365 Lab1
multi_astar.py

multi_astar API
'''

from state_and_transition import StateRepresentation,transitionFunction,goalTest
from maze_initializer import maze_initializer
import argparse

parser = argparse.ArgumentParser(description="maze reader")
parser.add_argument('-i', '--input', help = 'Enter the input maze .txt file', \
	required = True, dest = "inMaze")

args = parser.parse_args()

inputMaze = args.inMaze

class FrontierAstarNodeWithWeight():
    def __init__(self,state,parent,weight,depth):
        self.state=state
        self.parent=parent
        self.weight=weight
        self.depth=depth

def weightCalc(state,prizeLocation):
    return abs(state.mouseX-prizeLocation[0])+abs(state.mouseY-prizeLocation[1])

def binaryNodeSearch(array,start,stop,searchFor):
    if start>stop:
        return start
    middle=(stop+start)//2
    goal=array[middle].depth+array[middle].weight
    if goal==searchFor:
        return middle
    elif goal>searchFor:
        return binaryNodeSearch(array,start,middle-1,searchFor)
    else:
        return binaryNodeSearch(array,middle+1,stop,searchFor)

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
            state.printState()
            print("Cost:",totalCost)
            print("Nodes expanded:",expanded)
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

mousePos,prizePos,mazeArray = maze_initializer(inputMaze)
state = StateRepresentation(mousePos[0],mousePos[1],len(prizePos),mazeArray)
multi_astar(state,prizePos)