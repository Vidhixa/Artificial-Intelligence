#Vidhixa Joshi (vidjoshi)
# 04/September/2014

import random

def print_board():
    for i in range(0,3):
        for j in range(0,3):
            print map[2-i][j],
            if j != 2:
                print "|",
        print ""


def check_done():
	for i in range(0,3):
		if map[i][0] == map[i][1] == map[i][2] != " " \
		or map[0][i] == map[1][i] == map[2][i] != " ":
			print "*************************"
			print turn, "won!!!"
			print "*************************"
			return True

    	if map[0][0] == map[1][1] == map[2][2] != " " \
    	or map[0][2] == map[1][1] == map[2][0] != " ":
		print "*************************"
        	print turn, "won!!!"
		print "*************************"
        	return True

    	if " " not in map[0] and " " not in map[1] and " " not in map[2]:
        	print "*****************Draw***************"
        	return True


	return False

#Asking the user to select X or O
#Not case-sensitive
#player is given chances until proper input is received

print "Select your choice: X or O"
input_taken = False

while input_taken != True:
	user=raw_input("Choice: ")
	if user == "x" or user == "X":
		user = "X"
		bot = "0"
		input_taken = True
		
	elif user == "o"or user == "O":
		user = "O"
		bot="X"
		input_taken = True
	else:
		print "Wrong input, try again!"
	
	
turn = "X"
map = [[" "," "," "],
       [" "," "," "],
       [" "," "," "]]
done = False

#Counters used to take care of number of moves made by each to device appropriate strategy
countbot = 0
countuser = 0


#Switch turns until game has not ended
while done != True:
	if turn == user:
		print "Your turn"

		moved = False
		while moved != True:
			print "Please select position by typing in a number between 1 and 9, see below for which number that is which position..."
			print "7|8|9"
			print "4|5|6"
			print "1|2|3"
			print

			try:
				pos = input("Select: ")
				if pos <=9 and pos >=1:
					Y = pos/3
					X = pos%3
					if X != 0:
						X -=1
					else:
						 X = 2
						 Y -=1

					if map[Y][X] == " ":
						map[Y][X] = turn
						moved = True
						done = check_done()

						if done == False:
							countuser = countuser + 1
							turn = bot
							print_board()
							print
							print					
					else:
						print "Can't select this position, try again!!"
			except:
				print "You need to add a numeric value"
						

	else :
		print "Bot's turn"
		moved = False


		# Bot 'X' first move is random but one of the four corners
		if countuser == 0 and countbot == 0 : 
			foo = [2 , 0]
			p = random.choice(foo)
			q = random.choice(foo)				
			map[p][q] = turn
			moved = True


		#For an 'O' bot first move is a randomly selected corner if user placed in center; otherwise center 
		if countuser == 1 and countbot == 0 :
			if map[1][1] == user :
				foo = [2 , 0]
				p = random.choice(foo)
				q = random.choice(foo)				
				map[p][q] = turn
				moved = True			
			else :
				map[1][1] = turn
				moved = True
							
		# Attack 3 corner strategy
		if countbot == 1 and countuser == 1 :
			if map[1][1] == user :
				if p != q:
					map[q][p]= turn		
				elif p == q == 0 :
					map[2][2] = turn
				else :
					map[0][0] = turn
				
				moved = True			
				
			else :
				map[1][1] = turn
				moved = True

		# Blocking user from trying to reach to 2 possible wins  
		if countuser == 2 and countbot == 1:
			if map[2][2] == map[0][0] ==  user or map[2][0] == map[0][2] ==  user :
				map[2][1] = turn 
				moved = True

			elif map[0][0] == map[2][1]== user or map[1][0] == map[2][2]== user :
				map[2][0] = turn
				moved = True

			elif map[0][2] == map[2][1]== user or map[2][0] == map[1][2]== user :
				map[2][2] = turn
				moved = True

			elif map[0][0] == map[1][2]== user or map[2][2] == map[0][1]== user :
				map[0][2] = turn
				moved = True			
		
			elif map[0][2] == map[1][0]== user or map[2][0] == map[0][1]== user  :
				map[0][0] = turn
				moved = True
		


		# Winning move row and column wise 
		i = 0
		while i<3 and moved != True:
			if map[i][0] == map[i][1] == bot and map[i][2] == " " : 
				map[i][2] = turn  
				moved = True
			elif map[i][1] == map[i][2] == bot and map[i][0] == " " :
				map[i][0] = turn
				moved = True
			elif map[i][0] == map[i][2] == bot and map[i][1] == " " :
				map[i][1] = turn 
				moved = True
			elif map[0][i] == map[1][i] == bot and map[2][i] == " " :
				map[2][i] = turn 
				moved = True
			elif map[0][i] == map[2][i] == bot and map[1][i] == " " :
				map[1][i] = turn 
				moved = True
			elif map[1][i] == map[2][i] == bot and map[0][i] == " " :
				map[0][i] = turn 
				moved = True
			else:
				i= i+1 

		# Diagonally winning 
		if moved != True:
			if map[0][0] == map[1][1] == bot and map[2][2] == " " :
					map[2][2] = turn 
					moved = True
			elif map[0][0] == map[2][2] == bot and map[1][1] == " " :
					map[1][1] = turn 
					moved = True
			elif map[2][2] == map[1][1] == bot and map[0][0] == " " :
					map[0][0] = turn 
					moved = True
			elif map[0][2] == map[2][0] == bot and map[1][1] == " " :
					map[1][1] = turn 
					moved = True
			elif map[0][2] == map[1][1] == bot and map[2][0] == " " :
					map[2][0] = turn 
					moved = True
			elif map[1][1] == map[2][0] == bot and map[0][2] == " " :
					map[0][2] = turn 
					moved = True		
				
				 

		# Blocking move to defend against a possible win in game by opponent 
		i = 0
		while i<3 and moved != True:
			if map[i][0] == map[i][1] == user and map[i][2] == " " : 
				map[i][2] = turn  
				moved = True
			elif map[i][1] == map[i][2] == user and map[i][0] == " " :
				map[i][0] = turn
				moved = True
			elif map[i][0] == map[i][2] == user and map[i][1] == " " :
				map[i][1] = turn 
				moved = True
			elif map[0][i] == map[1][i] == user and map[2][i] == " " :
				map[2][i] = turn 
				moved = True
			elif map[0][i] == map[2][i] == user and map[1][i] == " " :
				map[1][i] = turn 
				moved = True
			elif map[1][i] == map[2][i] == user and map[0][i] == " " :
				map[0][i] = turn 
				moved = True
			else:
				i= i+1 

		# Diagonally blocking 
		if moved != True:
			if map[0][0] == map[1][1] == user and map[2][2] == " " :
					map[2][2] = turn 
					moved = True
			elif map[0][0] == map[2][2] == user and map[1][1] == " " :
					map[1][1] = turn 
					moved = True
			elif map[2][2] == map[1][1] == user and map[0][0] == " " :
					map[0][0] = turn 
					moved = True
			elif map[0][2] == map[2][0] == user and map[1][1] == " " :
					map[1][1] = turn 
					moved = True
			elif map[0][2] == map[1][1] == user and map[2][0] == " " :
					map[2][0] = turn 
					moved = True
			elif map[1][1] == map[2][0] == user and map[0][2] == " " :
					map[0][2] = turn 
					moved = True
			

			
		# When no strategy above works, we will put bot move at next open place row-wise
			if moved != True:
				for i in range(0,3):
					for j in range(0,3):
						if map[i][j] == " ":
							map[i][j] = turn
							moved = True
							break
					if moved == True:
						break
				
																					


	     		 
		print_board()   		
		done = check_done()
		if done == False:
			countbot = countbot + 1
			turn = user
		
		print 
		print 
			
	
	

		


