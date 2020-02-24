8 Puzzle Solver: 
Using Breadth First Search(BFS) Algorithm.
The project has been written in Python 3.7.6.

Instructions: 
To execute the file:

	1. Open terminal
	2. Enter command: cd "/Path of the '8Puzzle.py' file" python 8Puzzle.py
	3. Next the Python program for 8 puzzle solver will run.

To run the 8 Puzzle solver: 
	
	1. The Program will ask for a user input, which is the initial state of the 8 puzzle. 
	   The input should be given in the form of a 1-D array. That is, if the initial node to be input is 
 	   1 4 5
           8 7 2
           0 6 3
	   the input entered should be seprated by commas and given as 1,4,5,8,7,2,0,6,3.
	2. The program shows the goal configuration to be reached and if solvable,
	   returns the the optimal path to the Goal by Using Breadth First Search(BFS) algortihm.
	3. The Program generates a folder "SUkoonOutputFIles" in the directory where the '8Puzzle.py' file is being run from. This is 		   where the 3 output files will be stored.

The code generates 3 text files:

	1. nodePath.txt = Gives the Optimal Path taken to reach the final output or the goal. All entries of the file are the node 		   states ordered from start node to the goal node.
	   Format of the file : The elements are being stored column-wise, i.e. for this state 1 8 0 4 7 6 5 2 3, the eight puzzle                  node state is
 	   1 4 5
           8 7 2
           0 6 3

	2. Nodes.txt: Gives all the explored states and are  present in the format of nodePath.txt

	3. NodesInfo.txt: Gives Node Info  
			  First column: Node Index
			  Second Column: Parent Node Index
			  Third Colum : Cost(Not Used here in BFS. Hence 0)

