from chess import *
import json 
import os 
import random 
import time 

class Simulation:

    rows = 'abcdefgh'
    cols = 8
    possible_positions = []
    board = None
    board_solutions = [] 
    save_file = 'board_solutions.txt'

    def start(self):
        # initialization

        self.board_solutions = [] 
        self.board = ChessBoard()
        self.possible_positions = self.board.getPossiblePositions()
        total_solutions = 0 

        # -- iterating over all possibilites

        new_pos_checked = [] 
        queen_counter = 0 
        for x in range(10000):
            for x in range(10000):
               new_pos = random.choice(self.possible_positions)
               # if it's already been checked then just move to next iteration
               if new_pos in new_pos_checked:
                   continue 
               
               new_pos_checked.append(new_pos)
               safe = self.safeAgainstAllPositions(new_pos)
               if safe:
                   self.board.placeQueen(new_pos)
                   queen_counter += 1
               if queen_counter == 8 and self.board not in self.board_solutions:
                   # print("queens on board: " + str(queen_counter))
                   self.board.draw()
                   total_solutions += 1
                   self.board_solutions.append(self.board)
                   break 
            # reset board before next iteration 
            self.board = ChessBoard()
            queen_counter = 0
            new_pos_checked = []

            if len(self.board_solutions) == 92:
                break 

        # print('total solutions: ' + str(total_solutions))

        return self.board_solutions 

    def safeAgainstAllPositions(self, new_pos):
        """ Checks new_pos to see if it can be attacked by a queen on the board """

        # Iterates through all positions and if a queen at any of
        # those positions could attack the new position it returns
        # False
        for toCheckPos in self.possible_positions:
            # print("\t-->Checking against: " + toCheckPos)
            if self.board.canAttack(toCheckPos, new_pos):
                return False

        return True

    def writeSolutionsToFile(self):
        if self.board_solutions == []:
            print('nah')
            self.board_solutions = self.start() 

        with open(self.save_file, 'w') as f:
            for solution in self.board_solutions:
                # converts it to json string and writes dictionary on a line 
                f.write(json.dumps(solution.board) + '\n')


    def getSolutionsFromFile(self):
        ''' Returns solutions from the save file as an array of dictionary objects. If save file doesn't exist returns False ''' 
        solutions = [] 
        if os.path.exists(self.save_file):
            with open(self.save_file, 'r') as f:
                for line in f.readlines():
                    d = json.loads(line) 
                    solutions.append(d) 

            return solutions 
        
        return False 

    def getSolutions(self):
        ''' Returns solutions as an array of dictionary objects. First looks for solutions in the save file. If no save file exists simulation is run and then solutions are returned ''' 
        solutions = self.getSolutionsFromFile() 
        if not self.getSolutionsFromFile() or not len(self.getSolutionsFromFile()) == 92:
            self.start() 
            self.writeSolutionsToFile() 
            solutions = self.getSolutionsFromFile() 

        print("Total Solutions: " + str(len(solutions)))
        return solutions 

    def file_len(self, file_obj):
        with open(file_obj, 'r') as f:
            for i,l in enumerate(f):
                pass 

        return i+1

if __name__ == '__main__':
    simulation = Simulation()
    # start = time.time()
    # simulation.start()
    # end = time.time()
    simulation.getSolutions()

    # print("Running time: " + str(end-start) + " seconds")






