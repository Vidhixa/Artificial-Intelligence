#-------------------------------------------------------------------------------
# Name:        Informed Search
# Author:      Vidhixa Joshi (vidjoshi)
# Date:         09/23/2014
#-------------------------------------------------------------------------------
import Queue
import copy
import time


#We create node object everywhere
class Node():
    def __init__(self, priority, state, parent, depth, cost):
        self.priority = priority
        self.state = state
        self.parent = parent
        self.depth = depth
        self.cost = cost

def makeState(nw, n, ne, w, c, e, sw, s, se):
    list_state=[nw, n, ne, w, c, e, sw, s, se]
    return list_state

#Comparing the state of current node with goal state
def testProcedure(state,goalState):
    if goalState == state:
        return True
    else:
        return False

#Following function takes the match with goal state node and
#traces its parent to display sequence of stages
def outputProcedure(numRuns, node):
    print "Number of runs ::: ", numRuns
    print "Depth of tree ::: ",node.depth
    print "\n\n\n"
    '''trace = []
    while not node == None:
        trace.append(node.state)
        node=node.parent

    j=len(trace)
    while j>0:
        listpr=trace[j-1]
        for i in range(0,9):
            if listpr[i] == "blank":
                listpr[i]= " "
            print " ", listpr[i],
            if (i+1)%3 == 0:
                print "  \n------------"
        print "\n\n\n"
        j=j-1
'''
#Uses Hamming distance as the heuristic:
def testInformedSearch1(initalState, goalState, limit):
    #Note the start and end time 
    start = time.time()
    priority = 0
    depth=0
    numRuns=0
    
    #Data structure I used is a priority queue of form (priority, node object)
    q = Queue.PriorityQueue()
    node = Node(priority,initalState, None, depth, 0)
    q.put((priority,node))
    
    #Closed an open list contains list of nodes
    closed = []
    open = []
    while not q.empty():
        if (limit>0):
            nodetuple = q.get()   
            node = nodetuple[1]  
            closed.append(node)
            open.append(node)
            if testProcedure(node.state, goalState):
                end = time.time()
                print "Number of nodes seen ::: ",len(open)
                print "Time taken to fund solution ::: ",(end-start)
                return outputProcedure(numRuns,node)            
            else:
                #Successor function will find non-visited children and put
                #it in queue
                successor(node, q, closed, open)
                depth += 1
                limit -= 1
                numRuns += 1
        else:
            return "Not found in given limit"
            return
    return

#Uses Manhattan distance#same as above function
#Applying heuristic will be handled by the hcalculate function 
def testInformedSearch2(initalState, goalState, limit):
    start = time.time()
    priority = 0
    depth=0
    numRuns=0
    q = Queue.PriorityQueue()
    node = Node(priority,initalState, None, depth, 0)
    q.put((priority,node))
    closed = []
    open = []
    while not q.empty():
        if (limit>0):
            nodetuple = q.get()   
            node = nodetuple[1]  
            closed.append(node)
            open.append(node)
            if testProcedure(node.state, goalState):
                end = time.time()
                print "Number of nodes seen ::: ",len(open)
                print "Time taken to fund solution ::: ",(end-start)
                return outputProcedure(numRuns,node)
            
            else:
                #Successor function will find non-visited children and put
                #it in queue
                successor(node, q, closed, open)
                depth += 1
                limit -= 1
                numRuns += 1
        else:
            return "Not found in given limit"
            return
    return

#Used Manhattan distance as its heuristics
#We maintain a list of visited and generated nodes
#We make a check in both list to select node that costs list provided it is present 
#on open or closed list
def testAStar(initalState, goalState, limit):
    #calculating time of each test run
    start = time.time()
    priority = 0
    depth=0
    numRuns=0
    q = Queue.PriorityQueue()
    node = Node(priority,initalState, None, depth, 0)
    x =hcalculate(node.state, algo, 0)
    q.put((x,node))
    closed = []
    open = [node]
    while not q.empty():
        if (limit>0):
            nodetuple = q.get()   
            node = nodetuple[1]  
            closed.append(node)
            if testProcedure(node.state, goalState):
                end = time.time()
                print "Time taken to fund solution ::: ",(end-start)
                return outputProcedure(numRuns, node)
            elif isOpenBetter(open, node):
                #We discard a child node, if there is a cheaper node
                # available in open list
                successor(q.get()[1], q, closed, open)            
            else:
                successor(node, q, closed, open)
                depth += 1
                limit -= 1
                numRuns += 1
        else:
            return "Not found in given limit "
            return 

#Finding the successor of removed parent node
#If not visited, we will create a node and out it in the priority queue
def successor(node, q, closed, open):
    for i in range(0,9):
        if node.state[i] == "blank":
            if (i+1)%3 != 0:
                child = createchild(node.state, "toRight")
                if not isVisited(closed, child):
                    x = hcalculate(child, algo, node.cost)
                    childnode= Node(x, child, node, (node.depth+1),(node.cost+1))
                    q.put((x,childnode))
                    open.append(childnode)

                    
            if i>=0 and i<6:
                child = createchild(node.state, "toDown")
                if not isVisited(closed, child):
                    x = hcalculate(child, algo, node.cost)
                    childnode= Node(x, child, node, (node.depth+1),(node.cost+1))
                    q.put((x,childnode))
                    open.append(childnode)
                    
            if (i%3) != 0:
                child = createchild(node.state, "toLeft")
                if not isVisited(closed, child):
                    x = hcalculate(child, algo, node.cost)
                    childnode= Node(x, child, node, (node.depth+1),(node.cost+1))
                    q.put((x,childnode))
                    open.append(childnode)


            if i>2 and i<9:
                child = createchild(node.state, "toUp")
                if not isVisited(closed, child):
                    x = hcalculate(child, algo, node.cost)
                    childnode= Node(x, child, node, (node.depth+1),(node.cost+1))
                    q.put((x,childnode))
                    open.append(childnode)

#Calculate heuristic cost for all three methods.
#Algo is the parameter that tells  us which heuristic to follow                    
def hcalculate(child, algo,cost):
    if algo == "1":
        count = 0		
        for i in range(0,8):
            if child[i] != (i+1):
                count+=1	
                return count
    elif algo == "2":
        dis = 0
        childcopy = copy.deepcopy(child)
        for i in range(0,9):
            if childcopy[i] != "blank" and childcopy[i] != (i+1):
                dis = dis + calculateDis(childcopy, i)   
                return dis 
    else:
        totalcost = hcalculate(child, "2",0)+ cost  
        return totalcost
    
#calculate the Manhattan distance
def calculateDis(childcopy, i):
    if (childcopy[i]%3 == 0):
        val = (abs ((i/3)-((childcopy[i]-1)/3))+ abs ((i%3)-(childcopy[i]%3)))
    else:
        val = (abs ((i/3)-((childcopy[i]-1)/3))+ abs ((i%3)-((childcopy[i]-1)%3)))
    return val

#Creating child state based on input direction
def createchild(parent, direction):
    child = copy.deepcopy(parent)
    for i in range(0,9):
        if parent[i] == "blank":
            if direction == "toRight":
                child[i+1]=parent[i]
                child[i]=parent[i+1]
                return child
            elif direction == "toLeft":
                child[i]=parent[i-1]
                child[i-1]=parent[i]
                return child
            elif direction == "toUp":
                child[i-3]=parent[i]
                child[i]=parent[i-3]
                return child
            else:
                child[i+3]=parent[i]
                child[i]=parent[i+3]
                return child
#Check if the child state is already present (duplicate check)
#if it is, simply discard
def isVisited(closed, child):
    for i in range(len(closed)):
        if closed[i].state == child:
            return True
    return False    

#For Astar we check if there is a node in open list with same state as child, but better cost
#In that case we simply disregards the child
def isOpenBetter(open, node):
    for i in range(len(open)):
        if (open[i].state == node.state) and ((open[i].cost+open[i].priority)<(node.cost+node.priority)):
            return True
    return False
  
##############################################
# I have included all the test case.
#Runs only for initialstate7. 
#Uncomment to run all cases
##############################################

#main function
#Arbitary limit
limit = 100000

#I have used this as my goalstate for all the problem states given
goalState = makeState(1, 2, 3, 4, 5, 6, 7, 8, "blank")

# First group of test cases - should have solutions with depth <= 5
initialState1 = makeState(2, "blank", 3, 1, 5, 6, 4, 7, 8)
initialState2 = makeState(1, 2, 3, "blank", 4, 6, 7, 5, 8)
initialState3 = makeState(1, 2, 3, 4, 5, 6, 7, "blank", 8)
initialState4 = makeState(1, "blank", 3, 5, 2, 6, 4, 7, 8)
initialState5 = makeState(1, 2, 3, 4, 8, 5, 7, "blank", 6)

# Second group of test cases - should have solutions with depth <= 10
initialState6 = makeState(2, 8, 3, 1, "blank", 5, 4, 7, 6)
initialState7 = makeState(1, 2, 3, 4, 5, 6, "blank", 7, 8)
initialState8 = makeState("blank", 2, 3, 1, 5, 6, 4, 7, 8)
initialState9 = makeState(1, 3, "blank", 4, 2, 6, 7, 5, 8)
initialState10 = makeState(1, 3, "blank", 4, 2, 5, 7, 8, 6)

# Third group of test cases - should have solutions with depth <= 20
initialState11 = makeState("blank", 5, 3, 2, 1, 6, 4, 7, 8)
initialState12 = makeState(5, 1, 3, 2, "blank", 6, 4, 7, 8)
initialState13 = makeState(2, 3, 8, 1, 6, 5, 4, 7, "blank")
initialState14 = makeState(1, 2, 3, 5, "blank", 6, 4, 7, 8)
initialState15 = makeState("blank", 3, 6, 2, 1, 5, 4, 7, 8)

# Fourth group of test cases - should have solutions with depth <= 50
initialState16 = makeState(2, 6, 5, 4, "blank", 3, 7, 1, 8)
initialState17 = makeState(3, 6, "blank", 5, 7, 8, 2, 1, 4)
initialState18 = makeState(1, 5, "blank", 2, 3, 8, 4, 6, 7)
initialState19 = makeState(2, 5, 3, 4, "blank", 8, 6, 1, 7)
initialState20 = makeState(3, 8, 5, 1, 6, 7, 4, 2, "blank")


#User input taken for different heuristics
print "Enter your choice for informed search: \n 1. Hamming distance heuristic \n 2. Manhattan distance \n 3. A* "
algo=raw_input("Choice: ")
if algo == "1":
    print "Heuristic Hamming distance  :::" 
    testInformedSearch1(initialState7, goalState, limit)
    '''testInformedSearch1(initialState1, goalState, limit)
    testInformedSearch1(initialState2, goalState, limit)
    testInformedSearch1(initialState3, goalState, limit)
    testInformedSearch1(initialState4, goalState, limit)
    testInformedSearch1(initialState5, goalState, limit)
    testInformedSearch1(initialState6, goalState, limit)
    testInformedSearch1(initialState7, goalState, limit)
    testInformedSearch1(initialState8, goalState, limit)
    testInformedSearch1(initialState9, goalState, limit)
    testInformedSearch1(initialState10, goalState, limit)
    testInformedSearch1(initialState11, goalState, limit)
    testInformedSearch1(initialState12, goalState, limit)
    testInformedSearch1(initialState13, goalState, limit)
    testInformedSearch1(initialState14, goalState, limit)
    testInformedSearch1(initialState15, goalState, limit)
    testInformedSearch1(initialState16, goalState, limit)
    testInformedSearch1(initialState17, goalState, limit)
    testInformedSearch1(initialState18, goalState, limit)
    testInformedSearch1(initialState19, goalState, limit)
    testInformedSearch1(initialState20, goalState, limit)'''
    
elif algo == "2":
    print "Heuristic Manhattan distance ::: "
    testInformedSearch2(initialState7, goalState, limit)
    '''testInformedSearch2(initialState12, goalState, limit)
    testInformedSearch2(initialState2, goalState, limit)
    testInformedSearch2(initialState3, goalState, limit)
    testInformedSearch2(initialState4, goalState, limit)
    testInformedSearch2(initialState5, goalState, limit)
    testInformedSearch2(initialState6, goalState, limit)
    testInformedSearch2(initialState7, goalState, limit)
    testInformedSearch2(initialState8, goalState, limit)
    testInformedSearch2(initialState9, goalState, limit)
    testInformedSearch2(initialState10, goalState, limit)
    testInformedSearch2(initialState11, goalState, limit)
    testInformedSearch2(initialState12, goalState, limit)
    testInformedSearch2(initialState13, goalState, limit)
    testInformedSearch2(initialState14, goalState, limit)
    testInformedSearch2(initialState15, goalState, limit)
    testInformedSearch2(initialState16, goalState, limit)
    testInformedSearch2(initialState17, goalState, limit)
    testInformedSearch2(initialState18, goalState, limit)
    testInformedSearch2(initialState19, goalState, limit)
    testInformedSearch2(initialState20, goalState, limit)'''
else:
    algo = "3"
    print "A* with heuristic manhattan distance:::"
    testAStar(initialState7, goalState, limit)
`   '''testAStar(initialState1, goalState, limit)
    testAStar(initialState2, goalState, limit)
    testAStar(initialState3, goalState, limit)
    testAStar(initialState4, goalState, limit)
    testAStar(initialState5, goalState, limit)
    testAStar(initialState6, goalState, limit)
    testAStar(initialState7, goalState, limit)
    testAStar(initialState8, goalState, limit)
    testAStar(initialState9, goalState, limit)
    testAStar(initialState10, goalState, limit)
    testAStar(initialState11, goalState, limit)
    testAStar(initialState12, goalState, limit)
    testAStar(initialState13, goalState, limit)
    testAStar(initialState14, goalState, limit)
    testAStar(initialState15, goalState, limit)
    testAStar(initialState16, goalState, limit)
    testAStar(initialState17, goalState, limit)
    testAStar(initialState18, goalState, limit)
    testAStar(initialState19, goalState, limit)
    testAStar(initialState20, goalState, limit)'''






