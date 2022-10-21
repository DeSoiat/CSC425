import numpy as np
from EightPuzzleGame_State import State
'''
This class implement the Best-First-Search (BFS) algorithm along with the Heuristic search strategies

Open list is used to store the unexplored states 
Closed list is used to store the visited state. 

Open list is a priority queue (First-In-First-Out). 

The priority is insured through sorting the Open list each time after new states are generated 
and added into the list. 

The heuristics are used to decide which node should be visited next.

In this informed search, reducing the state space search complexity is the main criterion. 
We define heuristic evaluations to reduce the states that need to be checked every iteration. 
Evaluation function is used to express the quality of informedness of a heuristic algorithm. 

'''

class InformedSearchSolver:
    current = State()
    goal = State()
    openlist = []
    closed = []
    states_path = []
    depth = 0

    def __init__(self, current, goal):
        self.current = current
        self.goal = goal
        self.openlist.append(current)

    #this is used to sort the openlist in ascending order accoring to the heuristic value of state
    def sortFun(self, e):
        return e.weight


    def check_inclusive(self, s):
        """
         * The check_inclusive function is designed to check if the expanded state is in open list or closed list
         * This is done to prevent looping. (You can use a similar code from uninformedsearch program)
         * @param s
         * @return
        """
        #in_open = 0
        #in_closed = 0
        ret = -1

        # TODO your code start here

        # the child is not in open or closed
        if s not in self.openlist or s not in self.closed :
            ret = 1

        # the child is already in open
        #return 2
        elif s in self.openlist :
            ret = 2

        # the child is already in closed
        #return 3
        elif s in self.closed :
            ret = 3

        return ret



    # TODO your code start here
    def state_walk(self):
        """
        * The following state_walk function is designed to move the blank tile --> perform actions
        * There are four types of possible actions/walks of for the blank tile, i.e.,
        *  ↑ ↓ ← → (move up, move down, move left, move right)
        * Note that in this framework the blank tile is represent by '0' 
        """

        
        # move to the next heuristic state
        walk_state = self.current.tile_seq
        row = 0
        col = 0

        for i in range(len(walk_state)):
            for j in range(len(walk_state[i])):
                if walk_state[i, j] == 0:
                    row = i
                    col = j
                    break

        self.depth += 1

        ''' The following program is used to do the state space actions
         The 4 conditions for moving the tiles all use similar logic, they only differ in the location of the 
         tile that needs to be swapped. That being the case, I will only comment the first subroutine         
         '''
        # TODO your code start here
        ### ↑(move up) action ###
        
        if (row - 1) >= 0:
            temp_state1 = State()
            temp_state1.tile_seq = walk_state
            """
            """
            temp = temp_state1.tile_seq[row-1,col]
            temp_state1.tile_seq[row-1,col] = temp_state1.tile_seq[row,col]
            temp_state1.tile_seq[row,col] = temp
            ret = self.check_inclusive(temp_state1)
            if ret == 1 :
                temp_state1.depth = self.depth
                temp_state1.weight = self.heuristic_test(temp_state1)
                self.openlist.append(temp_state1)
            if ret == 2 :
                #if heuristic_test(temp_state1) < heuristic_test(temp) or depath < 
                self.openlist.append(temp_state1) 
            if ret == 3 :
                #if heuristic_test(temp_state1) < heuristic_test(temp)
                self.closed.remove(temp_state1)
                self.openlist.append(temp_state1) 


            """
             *get the 2d array of current 
             *define a temp 2d array and loop over current.tile_seq
             *pass the value from current.tile_seq to temp array
             *↑ is correspond to (row, col) and (row-1, col)
             *exchange these two tiles of temp
             *define a new temp state via temp array
             *call check_inclusive(temp state)
             *do the next steps according to flag

             *if flag = 1 //not in open and closed
             *begin
             *assign the child a heuristic value via heuristic_test(temp state);
             *add the child to open
             *end;

             *if flag = 2 //in the open list
             *if the child was reached by a shorter path  #  by compare the heuristic value ?
             *then give the state on open the shorter path # what does this mean ? add to the open list ?

             *if flag = 3 //in the closed list
             *if the child was reached by a shorter path then
             *begin
             *remove the state from closed;
             *add the child to open
             *end;
            """


        ### ↓(move down) action ###
        if (row + 1) <= 2:
            temp_state1 = State()
            temp_state1.tile_seq = walk_state
            temp = temp_state1.tile_seq[row+1,col]
            temp_state1.tile_seq[row+1,col] = temp_state1.tile_seq[row,col]
            temp_state1.tile_seq[row,col] = temp
            ret = self.check_inclusive(temp_state1)


        ### ←(move left) action ###
        if (col - 1) >= 0:
           temp_state1 = State()
           temp_state1.tile_seq = walk_state
           temp = temp_state1.tile_seq[row,col-1]
           temp_state1.tile_seq[row,col-1] = temp_state1.tile_seq[row,col]
           temp_state1.tile_seq[row,col] = temp
           ret = self.check_inclusive(temp_state1)


        ### →(move right) action ###
        if (col + 1) <= 2:
           temp_state1 = State()
           temp_state1.tile_seq = walk_state
           temp = temp_state1.tile_seq[row,col+1]
           temp_state1.tile_seq[row,col+1] = temp_state1.tile_seq[row,col]
           temp_state1.tile_seq[row,col] = temp
           ret = self.check_inclusive(temp_state1)


        # sort the open list first by h(n) then g(n)
   
        # Set the next current state
        
        self.states_path.append(self.current)

        #TODO your code end here




    def heuristic_test(self, current):
        """
        * Solve the game using heuristic search strategies

        * There are three types of heuristic rules:
        * (1) Tiles out of place
        * (2) Sum of distances out of place
        * (3) 2 x the number of direct tile reversals

        * evaluation function
        * g(n) is the distance from start state to the current state
        * h(n) is the distance from current to the goal state
        * f(n) = g(n) + h(n)
        * g(n) = depth of path length to start state
        * h(n) = (1) + (2) + (3)
        """

        curr_seq = current.tile_seq
        goal_seq = self.goal.tile_seq

        # (1) Tiles out of place
        h1 = 0
        #TODO your code start here
        """
         *loop over the curr_seq
         *check the every entry in curr_seq with goal_seq
        """
        #TODO your code end here
        

        # (2) Sum of distances out of place
        h2 = 0
        #TODO your code start here
        """
         *loop over the goal_seq and curr_seq in nested way
         *locate the entry which has the same value in 
         *curr_seq and goal_seq then calculate the offset
         *through the absolute value of two differences
         *of curr_row-goal_row and curr_col-goal_col
         *absoulte value can be calculated by abs(...)
        """
        #TODO your code end here
        
        
        # (3) 2 x the number of direct tile reversals
        h3 = 0
        #TODO your code start here
        """
         *loop over the curr_seq
         *use a Γ(gamma)shap slider to walk throught curr_seq and goal_seq
         *rule out the entry with value 0
         *set the boundry restriction
         *don't forget to time 2 at last
         *for example 
         *goal_seq  1 2 3   curr_seq  2 1 3 the Γ shape starts 
         *       4 5 6          4 5 6
         *       7 8 0          7 8 0
         *with 1 2 in goal_seq and 2 1 in curr_seq thus the 
         *    4             4
         *reversal is 1 2 and 2 1
        """

        # update the heuristic value for current state

        #TODO your code end here




    # You can change the following code to print all the states on the search path
    def run(self):
        # output the goal state
        target = self.goal.tile_seq
        print("\nReached goal state: ")
        target_str = np.array2string(target, precision=2, separator=' ')
        print(target_str[1:-1])

        print("\n The visited states are: ")
        path = 0
        # add closed state
        self.current = self.openlist.pop(0)
        self.closed.append(self.current)
        
        while not self.openlist:
            if self.current.equals(self.goal):
                print("1")
                #return the path from the start to current state
            else:
                self.state_walk()
                print('Visited State number ', path + 1)
                pathstate_str = np.array2string(self.current.tile_seq, precision=2, separator=' ')
                print(pathstate_str[1:-1])
                path += 1

        print("\nIt took ", path, " iterations to reach to the goal state")
        print("The length of the path is: ", self.current.depth)

