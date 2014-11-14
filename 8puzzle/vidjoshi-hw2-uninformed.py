import Queue
import copy
import time

#We create node object everywhere
class Node():
	def __init__(self, state, parent, depth, pathCost):
		self.state = state
		self.parent = parent
		self.depth = depth
		self.pathcost = pathCost	

def makeState(nw, n, ne, w, c, e, sw, s, se):	
	list_state=[nw, n, ne, w, c, e, sw, s, se]
	return list_state

#Comparing the state of current node with goal state
def testProcedure(state):
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
	trace = []
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

# Breadth wise the nodes will be expanded
#open list will be used to get length of states generated
#closed list will check if state has been visisted or not
def testBFS(init, goal, limit):
	start = time.time()
	depth=0
	numRuns=0
	q = Queue.Queue()	
	node = Node(init,None,depth,0)
	q.put(node)
	closed = []
	open = []
	open.append(node.state)
	while not q.empty():
		#we use limit to keep a check that number of nodes visited does not exceed 
		if (limit > 0):
			node = q.get()
			closed.append(node.state)
			if testProcedure(node.state):
				end = time.time()
				print "Number of nodes seen ::: ",len(open)
				print "Time taken to fund solution ::: ",(end-start)
				return outputProcedure(numRuns,node)
			else:
				successorBFS(node, q, closed, open)
			depth += 1
			limit -= 1
			numRuns += 1
		else:
			print "Not found in given limit"
			return

# Depth wise the nodes will be expanded
#open list will be used to get length of states generated
#closed list will check if state has been visited or not
def testDFS(init, goal, limit):
	start = time.time()
	depth=0
	numRuns=0
	stack = []
	closed = []
	open = []
	node = Node(init,None,depth,0)
	open.append(node.state)
	stack.append(node)
	while len(stack)!=0:
		if (limit>0):
			node = stack.pop()
			closed.append(node.state)
			if testProcedure(node.state):
				end = time.time()
				print "Number of nodes seen ::: ",len(open)
				print "Time taken to fund solution ::: ",(end-start)
				return outputProcedure(numRuns,node)			
			else:
				successorDFS(node, stack, closed, open)
				limit -= 1
				numRuns += 1
				depth += 1
		else:
			print "Not found in given limit"
			return
		
#Finding the successor of removed parent node
#If not visited, we will create a node and out it in the queue			
def successorBFS(node, q, closed, open):
	for i in range(0,9):
		if node.state[i] == "blank":
			if (i+1)%3 != 0:
				child = createchild(node.state, "toRight")
				if not isVisited(closed, child):
					childnode= Node(child, node, (node.depth+1), 0)				
					q.put(childnode)
					open.append(child)			
			if (i%3) != 0:
				child = createchild(node.state, "toLeft")
				if not isVisited(closed, child):
					childnode= Node(child, node, (node.depth+1), 0)					
					q.put(childnode)	
					open.append(child)
			if i>2 and i<9:
				child = createchild(node.state, "toUp")
				if not isVisited(closed, child):
					childnode= Node(child, node, (node.depth+1), 0)		
					q.put(childnode)
					open.append(child)
			if i>=0 and i<6:
				child = createchild(node.state, "toDown")
				if not isVisited(closed, child):
					childnode= Node(child, node, (node.depth+1), 0)				
					q.put(childnode)
					open.append(child)
	

# Seperate function written for successor nodes as I have used stack data structure					
def successorDFS(node, q, closed, open):
	for i in range(0,9):
		if node.state[i] == "blank":
			if (i%3) != 0:
				child = createchild(node.state, "toLeft")
				if not isVisited(closed, child):
					childnode= Node(child, node, (node.depth+1), 0)
					q.append(childnode)
					open.append(child)

			if i>=0 and i<6:
				child = createchild(node.state, "toDown")
				if not isVisited(closed, child):
					childnode= Node(child, node, (node.depth+1), 0)
					q.append(childnode)
					open.append(child)

			if (i+1)%3 != 0:
				child = createchild(node.state, "toRight")
				if not isVisited(closed, child):
					childnode= Node(child, node, (node.depth+1), 0)
					q.append(childnode)	
					open.append(child)		

			if i>2 and i<9:
				child = createchild(node.state, "toUp")
				if not isVisited(closed, child):
					childnode= Node(child, node, (node.depth+1), 0)
					q.append(childnode)
					open.append(child)

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

#Checks for the occurances of child state in already visited states
#On returning true, child would be simply discarded
def isVisited(visited, child):
	for i in range(len(visited)):
		if visited[i] == child:
			return True
	return False
	
##############################################
# I have included all the test case.
#Runs only for initialstate7. 
#Uncomment to run all cases
##############################################

#main function
#Arbitary limit
limit = 5000

#main 
# First group of test cases - should have solutions with depth <= 5
initialState1 = makeState(2, "blank", 3, 1, 5, 6, 4, 7, 8)
initialState2 = makeState(1, 2, 3, "blank", 4, 6, 7, 5, 8)
initialState3 = makeState(1, 2, 3, 4, 5, 6, 7, "blank", 8)
initialState4 = makeState(1, "blank", 3, 5, 2, 6, 4, 7, 8)
initialState5 = makeState(1, 2, 3, 4, 8, 5, 7, "blank", 6)


# Second group of test cases - should have solutions with depth <= 10
initialState6 = makeState(1, 2, 3, 4, 5, 6, 7, "blank",8)
initialState7 = makeState(1, 2, 3, 4, 5, 6, "blank", 7, 8)
initialState8 = makeState("blank", 2, 3, 1, 5, 6, 4, 7, 8)
initialState9 = makeState(1, 3, "blank", 4, 2, 6, 7, 5, 8)
initialState10 = makeState(1, 3, "blank", 4, 2, 5, 7, 8, 6)


# Third group of test cases - should have solutions with depth <= 20
initialState11 = makeState("blank", 5, 3, 2, 1, 6, 4, 7, 8)
initialState12 = makeState(5, 1, 3, 2, "blank", 6, 4, 8, 7)
initialState13 = makeState(2, 3, 8, 1, 6, 5, 4, 7, "blank")
initialState14 = makeState(1, 2, 3, 5, "blank", 6, 4, 7, 8)
initialState15 = makeState("blank", 3, 6, 2, 1, 5, 4, 7, 8)


# Fourth group of test cases - should have solutions with depth <= 50
initialState16 = makeState(2, 6, 5, 4, "blank", 3, 7, 1, 8)
initialState17 = makeState(3, 6, "blank", 5, 7, 8, 2, 1, 4)
initialState18 = makeState(1, 5, "blank", 2, 3, 8, 4, 6, 7)
initialState19 = makeState(2, 5, 3, 4, "blank", 8, 6, 1, 7)
initialState20 = makeState(3, 8, 5, 1, 6, 7, 4, 2, "blank")

#I have used this as my goalstate for all the problem states given
goalState = makeState(1, 2, 3, 4, 5, 6, 7, 8, "blank")

'''testBFS(initialState1, goalState, limit)
testBFS(initialState2, goalState, limit)
testBFS(initialState3, goalState, limit)
testBFS(initialState4, goalState, limit)
testBFS(initialState5, goalState, limit)
testBFS(initialState6, goalState, limit)'''
testBFS(initialState7, goalState, limit)
'''testBFS(initialState8, goalState, limit)
testBFS(initialState9, goalState, limit)
testBFS(initialState10, goalState, limit)
testBFS(initialState11, goalState, limit)
testBFS(initialState12, goalState, limit)
testBFS(initialState13, goalState, limit)
testBFS(initialState14, goalState, limit)
testBFS(initialState15, goalState, limit)
testBFS(initialState16, goalState, limit)
testBFS(initialState17, goalState, limit)
testBFS(initialState18, goalState,limit)
testBFS(initialState19, goalState, limit)
testBFS(initialState20, goalState, limit)'''

'''testDFS(initialState1, goalState, limit)
testDFS(initialState2, goalState, limit)
testDFS(initialState3, goalState, limit)
testDFS(initialState4, goalState, limit)
testDFS(initialState5, goalState, limit)
testDFS(initialState6, goalState, limit)'''
testDFS(initialState7, goalState, limit)
'''testDFS(initialState8, goalState, limit)
testDFS(initialState9, goalState, limit)
testDFS(initialState10, goalState, limit)
testDFS(initialState11, goalState, limit)
testDFS(initialState12, goalState, limit)
testDFS(initialState13, goalState, limit)
testDFS(initialState14, goalState, limit)
testDFS(initialState15, goalState, limit)
testDFS(initialState16, goalState, limit)
testDFS(initialState17, goalState, limit)
testDFS(initialState18, goalState, limit)
testDFS(initialState19, goalState, limit)
testDFS(initialState20, goalState, limit)'''




