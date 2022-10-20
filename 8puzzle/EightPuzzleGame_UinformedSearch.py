import numpy as np
import copy
from EightPuzzleGame_State import State

'''
This class implement one of the Uninformed Search algorithm
You may choose to implement the Breadth-first or Depth-first or Iterative-Deepening search algorithm

python list insert (index,item), append (item), extend (anotherList), remove (item), pop (index)

'''


class UninformedSearchSolver:
    current = State()
    goal = State()
    openlist = []
    closed = []
    depth = 0

    def __init__(self, current, goal):
        self.current = current
        self.goal = goal
        self.openlist.append(current)


    def check_inclusive(self, s):
        """
        * The check_inclusive function is designed to check if the expanded state is or is not in open list or closed list
        * This is done to prevent looping
        * @param s
        * @return
        """
        ret = -1


        #TODO your code start here
        for state in self.openlist:
            a = s.tile_seq == state.tile_seq
            if a.all():
                return 1
            

        for state in self.closed:
            a = s.tile_seq == state.tile_seq
            if a.all():
                return 1
        #TODO your code end here
        return ret      


    def state_walk(self):

        """
        * The following state_walk function is designed to move the blank tile =0 --> perform actions
         * There are four types of possible actions/walks of for the blank tile, i.e.,
         *  ↑ ↓ ← → (move up, move down, move left, move right)
         * Note that in this framework the blank tile is represent by '0'
        """

        walk_state = self.current
        row = 0
        col = 0

        # Loop to find the location of the blank space
        for i in range(len(walk_state.tile_seq)):
            for j in range(len(walk_state.tile_seq[i])):
                if walk_state.tile_seq[i, j] == 0:
                    row = i
                    col = j
                    break

        ''' The following program is used to do the state space actions
            The 4 conditions for moving the tiles all use similar logic, they only differ in the location of the 
            tile that needs to be swapped. That being the case, I will only comment the first subroutine
        '''
        # TODO your code start here
        ### ↑(move up) action ###
        #(row - 1) is checked to prevent out of bounds errors, the tile is swapped with the one above it
        temp_state1 = copy.deepcopy(walk_state)
        if (row - 1) >= 0:
            """
             
            """
            temp = temp_state1.tile_seq[row-1,col]
            temp_state1.tile_seq[row-1,col] = temp_state1.tile_seq[row,col]
            temp_state1.tile_seq[row,col] = temp
            ret = self.check_inclusive(temp_state1)
            if ret != 1 :
                self.openlist.append(temp_state1)
              

        ### ↓(move down) action ###
        temp_state2 = copy.deepcopy(walk_state)
        if (row+1) <= 2 :
            temp = temp_state2.tile_seq[row+1,col]
            temp_state2.tile_seq[row+1,col] = temp_state2.tile_seq[row,col]
            temp_state2.tile_seq[row,col] = temp
            ret = self.check_inclusive(temp_state2)
            if ret != 1 :
                self.openlist.append(temp_state2)

        ### ←(move left) action ###
        temp_state3 = copy.deepcopy(walk_state)
        if (col - 1) >=0 :
            temp = temp_state3.tile_seq[row,col-1]
            temp_state3.tile_seq[row,col-1] = temp_state3.tile_seq[row,col]
            temp_state3.tile_seq[row,col] = temp
            ret = self.check_inclusive(temp_state3)
            if ret != 1 :
                self.openlist.append(temp_state3)

        ### →(move right) action ###
        temp_state4 = copy.deepcopy(walk_state)
        if (col + 1) <= 2 :
            temp = temp_state4.tile_seq[row,col+1]
            temp_state4.tile_seq[row,col+1] = temp_state4.tile_seq[row,col]
            temp_state4.tile_seq[row,col] = temp
            ret = self.check_inclusive(temp_state4)
            if ret != 1 :
                self.openlist.append(temp_state4)

        # Set the next current state


        #TODO your code end here


    # # You can change the following code to print all the states on the search path
    def run(self):
        # output the goal state
        target = self.goal.tile_seq
        print("\nReached goal state: ")
        target_str = np.array2string(target, precision=2, separator=' ')
        print(target_str[1:-1])

        #breadth first search
        print("\n The visited states are: ")

        while self.openlist:
            # First you need to remove the current node from the open array and move it to the closed array
            self.current = self.openlist.pop(0)
            self.closed.append(self.current)

            if self.current.equals(self.goal):
                print("success")
                return "success"
                
            else:
                self.state_walk()#generate the children
                #for loop print out the content openlist
                print("openlist")
                for state in self.openlist:
                    state_str = np.array2string(state.tile_seq, precision=2, separator=' ')
                    print(state_str[1:-1])
                print(" ")
                


