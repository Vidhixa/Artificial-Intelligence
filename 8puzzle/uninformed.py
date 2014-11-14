import Queue
import collections
import copy

numRuns = 0
limit=5
count = 0

class Node():
	def __init__(self,state, parent, depth, pathCost):
		self.state = state
		self.parent = parent
		self.depth = depth
		self.pathcost = pathCost
	

def makeState(nw, n, ne, w, c, e, sw, s, se):
	list_state=[nw, n, ne, w, c, e, sw, s, se]
	return list_state

def printboard(listpr):
	for i in range(0,9):
		print " ",listpr[i],
		if (i+1)%3 == 0:
			print "\n"


def testProcedure(state):
	if goalState == state:
		return True
	else:
		return False

def outputProcedure(numRuns, node):
	#print count
	trace= []
	#print "test no ::: ", count
	print "Number of runs ::: ", numRuns
	print "Depth of tree ::: ", node.depth

	while not node == "null":
		trace.append(node.state)
		node=node.parent	
	
	j=len(trace)
	while j>0:
		listpr=trace[j-1]	
		for i in range(0,9):
			print " ", listpr[i],
			if (i+1)%3 == 0:
				print "  \n------------"
		print "\n\n\n"
		j=j-1
	#count=count+1


def testBFS(init, goal, limit):
	depth=1
	numRuns=0
	q = Queue.Queue()	
	node = Node(init,"null",depth,0)
	q.put(node)
	visited = []
	while not q.empty():
		node = q.get()
		#print "depth is :: ",node.depth
		visited.append(node.state)
		#print "node out of q is ::: ",node.state
		if testProcedure(node.state):
			return outputProcedure(numRuns, node)
		else:
			successor(node, q, visited, node.depth)
		s=node.depth
		depth += 1
		limit -= 1
		numRuns += 1
		#print "complete iteration"
	#print "result depth is :: ",(node.depth+1)
	return "not found"
					 
			
def successor(node, q, visited, depth):
	for i in range(0,8):
		if node.state[i] == " ":
			if (i+1)%3 != 0:
         			child = createchild(node.state, "toRight")
				if not isVisited(visited, child):
					#printboard(child)
					
					childnode= Node(child, node, (node.depth+1), 0)		
					visited.append(child)
					printboard(child)
					print "\n"				
					q.put(childnode)			
			if (i%3) != 0:
				child = createchild(node.state, "toLeft")
				if not isVisited(visited, child):
					#printboard(child)
					#print "\n"
					childnode= Node(child, node, (node.depth+1), 0)		
					visited.append(child)
					printboard(child)
					print "\n"				
					q.put(childnode)
			
			if i>2 and i<9:
	 			child = createchild(node.state, "toUp")
				if not isVisited(visited, child):
					#printboard(child)
					childnode= Node(child, node, (node.depth+1), 0)	
					visited.append(child)
					#print "\n"	
					#visited.put(child)
					printboard(child)
					print "\n"				
					q.put(childnode)
			
			if i>=0 and i<6:
				child = createchild(node.state, "toDown")
				if not isVisited(visited, child):
					#printboard(child)
					#print "\n"
					childnode= Node(child, node, (node.depth+1), 0)	
					visited.append(child)
					printboard(child)
					print "\n"	
					#visited.put(child)				
					q.put(childnode)
			
					

def createchild(parent, direction):
  child = copy.deepcopy(parent)
  for i in range(0,8):	
	
	if parent[i] == " ":
		if direction == "toRight":
			#print "inside right"
			temp=child[i+1]
			child[i+1]=child[i]
			child[i]=temp
			#print child
			return child
		elif direction == "toLeft":
			#print "inside left"
			temp=child[i]
			child[i]=child[i-1]
			child[i-1]=temp
			#print child
			return child
		elif direction == "toUp":
			#print "inside up"				
			temp=child[i-3]
			child[i-3]=child[i]
			child[i]=temp
			#print child
			return child
		else:
			#print "inside down"
			temp=child[i+3]
			child[i+3]=child[i]
			child[i]=temp
			#print child
			return child

def isVisited(visited, child):
	for i in range(len(visited)):
		if visited[i] == child:
			return True
	return False
	

#main

#initialState16 = makeState(2, 6, 5, 4, " ", 3, 7, 1, 8)
initialState = makeState(2, 8, 3, 1, 6, 4, 7, " ", 5)
initialState17 = makeState(3, 6, " ", 5, 7, 8, 2, 1, 4)
initialState18 = makeState(1, 5, " ", 2, 3, 8, 4, 6, 7)
initialState19 = makeState(2, 5, 3, 4, " ", 8, 6, 1, 7)
initialState20 = makeState(3, 8, 5, 1, 6, 7, 4, 2, " ")
g = makeState(1, 2, 3, " ", 4, 6, 7, 5, 8)
#goal state
goalState = makeState(1, 2, 3, 4, 5, 6, 7, 8, " ")
#testBFS(initialState, goalState, limit)













#def testBFS(init, goal, limit):
#def testDFS(init, goal, limit):
#def testInformedSearch1(init, goal, limit):
#def testInformedSearch2(init, goal, limit):
#def testAStar(init, goal, limit):
