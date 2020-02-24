#8-Puzzle Problem solved using BFS algorithm
#Author : Sukoon Sarin
import numpy as np 
from copy import copy
import imutils
import os

#################################################################################################################################

#Function to take user input
def userInput():
	value = input("Enter the Initial state of the 8 Puzzle. Please enter in the form of a 1-D array, seperated by commas : \n") 
	if value == '':
		value = input("Please enter the Initial state to begin the puzzle : \n")
	value = value.split(",")
	#print(value)
	Initial_input = []
	for i in value:
		Initial_input.append(int(i))
	#print(Initial_input)
	if check_repetition(Initial_input) == 1:
		Initial_State = np.array(Initial_input)
		Initial_State = Initial_State.reshape(3,3)
		print("The Initial state given : ")
		print(Initial_State)
	else : 
		print("Invalid input, Please don't repeat Numbers in puzzle")
		exit(0)
	return Initial_State
#################################################################################################################################

#Function to check if input elements are being repeated or not
def check_repetition(ip):
    
    for i in range(9):
        cnt = 0
        for j in range(9):
            if ip[i] == ip[j]:
                cnt += 1
        if cnt >= 2:
        	return 0
    else:
    	return 1
#################################################################################################################################

#Solvability check for the 8 Puzzle Problem for the input Configuration taken from user
def solvableCheck(initial):
	check = initial.flatten()
	sol=0
	for i in range(9):
		for j in range(i+1,9):
			if check[i]>check[j] and check[i]-check[j]!=check[i]:
				sol+=1
				
	if sol%2==0:
		return True
	else:
		return False
#################################################################################################################################
#Function to find location of the 0th tile
def find_index_zero(node):
	for i in range(node.shape[0]):
		for j in range(node.shape[1]):
			if node[i][j]==0:
				return i,j
#################################################################################################################################

#Function to move the 0th tile down
def moveDown(nodedata):
    i, j = find_index_zero(nodedata)
    if i == 2:
        return None
    else:
        swap_array = nodedata.copy()
        swap = swap_array[i + 1, j]
        swap_array[i, j] = swap
        swap_array[i + 1, j] = 0
        return swap_array
#################################################################################################################################

#Function to move the 0th tile up
def moveUp(data):
    i, j = find_index_zero(data)
    if i == 0:
        return None
    else:
        swap_array = data.copy()
        swap = swap_array[i - 1, j]
        swap_array[i, j] = swap
        swap_array[i - 1, j] = 0
        return swap_array
#################################################################################################################################

#Function to move the 0th tile right
def moveRight(data):
    i, j = find_index_zero(data)
    if j == 2:
        return None
    else:
        swap_array = data.copy()
        swap = swap_array[i, j + 1]
        swap_array[i, j] = swap
        swap_array[i, j + 1] = 0
        return swap_array

#################################################################################################################################

#Function to move the 0th tile left
def moveLeft(data):
    i, j = find_index_zero(data)
    if j == 0:
        return None
    else:
        swap_array = data.copy()
        swap = swap_array[i, j - 1]
        swap_array[i, j] = swap
        swap_array[i, j - 1] = 0
        return swap_array
#################################################################################################################################

def moveTile_0(movement, nodeinput):
    if movement == 'U':
        return moveUp(nodeinput)
    if movement == 'D':
        return moveDown(nodeinput)
    if movement == 'L':
        return moveLeft(nodeinput)
    if movement == 'R':
        return moveRight(nodeinput)
    else:
        return None
#################################################################################################################################

class State:
    def __init__(self, data, nodeIndex, parent, cost):
        self.data = data
        self.nodeIndex = nodeIndex
        self.parent = parent
        self.cost = cost
#################################################################################################################################

#Function for backtracking the optimal path to child node
def optimal_path(node):  
    p = []  
    p.append(node)
    parent_node = node.parent
    while parent_node is not None:
        p.append(parent_node)
        parent_node = parent_node.parent
    list_path = list(p)
    return list_path[::-1]
#################################################################################################################################
#Function to write 3 output files : nodePath.txt, Nodes.txt, NodesInfo.txt
def write_files(path,all_nodes,nodes_visited):
	op_file1 = open("./SukoonOutputFIles/nodePath.txt", "w+")
	op_file2 = open("./SukoonOutputFIles/Nodes.txt", "w+")
	op_file3 = open('./SukoonOutputFIles/NodesInfo.txt','w+')

	#file "NodePath" #Showing Optimal path to Goal
	for object1 in path:
		for i in range(len(object1.data)):
			for j in range(len(object1.data)):
				op_file1.write(str(object1.data[j][i]) + " ")
		op_file1.write("\n")
	op_file1.close()

	#file "Nodes" #Showing all explored Nodes using a BFS algorithm
	for object2 in all_nodes:
		for i in range(len(object2)):
			for j in range(len(object2)):
				op_file2.write(str(object2[j][i]) + " ")
		op_file2.write("\n")
	op_file2.close()

	#File "NodeInfo" #Index info of child nodes and parent nodes
	for object3 in nodes_visited:
		op_file3.write(str(object3.nodeIndex) + "\t" + str(object3.parent.nodeIndex) + "\t" + str(object3.cost))
		op_file3.write("\n")
	op_file3.close()
##################################################################################################################################
#BFS Algorithm
def BFS_solve(node,goal):
    action_set = ["D", "U", "R", "L"] #Down , Up, Right, Left
    queue = [node]
    explored = []
    visited = []
    #All explored Nodes
    explored.append(queue[0].data.tolist()) 
    count_node = 0 
    while queue:
    	#Removing element from the queue and that becomes our current node
   		current_node = queue.pop(0)  # Pop the element 0 from the list
   		if current_node.data.tolist() == goal.tolist():
   			return current_node, explored, visited

   		for direction in action_set:
   			temp_arr = moveTile_0(direction, current_node.data)
   			if temp_arr is not None:
   				count_node += 1
   				child = State(np.array(temp_arr),count_node,current_node, 0)  # Create a child node

   				if child.data.tolist() not in explored:  # Add the child node data in final node list
   					queue.append(child)
   					explored.append(child.data.tolist())
   					visited.append(child)
   					if child.data.tolist() == goal.tolist():
   						return child, explored, visited  # return statement if the goal node is not reached
#################################################################################################################################

#MAIN: 
initial_state = userInput()
goal_state = np.array([[1,2,3],[4,5,6],[7,8,0]],dtype='int32')
print("The goal State to be reached is")
print(goal_state)
#print(initial_state.shape[0])
#print(initial_state.shape[1])

#creates a folder "SukoonOutputFiles" in the root directory, where the files will be stored.
if (not(os.path.isdir('./SukoonOutputFIles'))):
	os.makedirs('./SukoonOutputFIles')

start_node = State(initial_state,0, None, 0)
if solvableCheck(initial_state) == True:
	print("Puzzle is Solvable")
	print("----------------------Solving----------------------")
	child_node, final_nodes , nodes_visited = BFS_solve(start_node,goal_state)
	
	#Display FInal Path : 
	print("Final Path Found:")
	final_path = optimal_path(child_node)
	for item in final_path:
		print(str(item.data)+ "\t")
	print("GOAL REACHED")

	#Write Desired FIles
	write_files(final_path,final_nodes,nodes_visited)
else : 
	print("Puzzle is unsolvable for this state")
##########################################################

