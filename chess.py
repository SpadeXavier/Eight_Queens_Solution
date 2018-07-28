from termcolor import colored


def printc(*args, **kwargs):
    print(colored(args[0], args[1]), **kwargs)


class ChessBoard:
    rows = 'ABCDEFGH'
    columns = 8
    delimeter = '  '
    board = {}

    def __init__(self):
        self.board = self.getEmptyBoard()

    def draw(self):

        # empty space at top left
        print(self.delimeter, end=' ')

        # print out numbers, spaced out with the delimter
        print(self.delimeter.join(str(x) for x in range(1, len(self.rows) + 1)))

        # print out board
        for row, column in self.board.items():
            print(row, end=self.delimeter)
            for space in column:
                if space == 'Q':
                    printc('Q', 'red', end=self.delimeter)
                    # printc('Q', end=self.delimeter)
                else:
                    print(space, end=self.delimeter)
            # amount of lines b/w each row determined by delimeter
            for x in range(len(self.delimeter)):
                print()

    def getEmptyBoard(self):
        board = {}

        for row in self.rows:
            board[row] = []
            for x in range(self.columns):
                board[row].append('e')

        return board

    def placeQueen(self, position):
        """ Inserts a queen(Q) at a given position given in the format of row letter and column number such as E1 """
        letter = position[0]
        col_num = int(position[1]) - 1
        row = self.board[letter]

        del row[col_num]
        row.insert(col_num, 'Q')

    def removeQueen(self, position):
        """ Deletes a queen(Q) at a given position given in the format of row letter and column number such as E1 """

        letter = position[0]
        col_num = int(position[1]) - 1
        row = self.board[letter]
        del row[col_num]
        row.insert(col_num, 'e')

    def isQueen(self, pos):
        """ Checks if a queen(Q) exists at the given position """
        letter = pos[0]
        col_num = int(pos[1]) - 1
        row = self.board[letter]
        piece = row[col_num]

        return piece == 'Q'

    def canAttack(self, pos_one, pos_two):
        """ Checks if a theoretical queen at pos_two is being attacked by a (potential)queen at pos_one """
        letter_one = pos_one[0]
        col_num_one = int(pos_one[1])

        letter_two = pos_two[0]
        col_num_two = int(pos_two[1])

        if not self.isQueen(pos_one):
            return False

        # Checking straight up and down
        if col_num_one == col_num_two:
            return True

        # Checking row
        if letter_one == letter_two:
            return True

        # Checking diagonals
        pos_hits = self.getDiagonals(pos_two)
        # print("\t-->" + str(pos_hits))
        for ph in pos_hits:
            if self.isQueen(ph):
                return True

        return False

    def getPossiblePositions(self):
        possible_positions = []
        for row_letter in self.rows:
            for col_num in range(1, self.columns + 1):
                possible_positions.append(row_letter + str(col_num))

        return possible_positions

    def getDiagonals(self, pos):
        letter_index = self.rows.index(pos[0])
        col_num = int(pos[1])
        pos_hits = []

        col_index = col_num
        letter_index_cp = letter_index
        # get left backward hits 
        
        # -- notice how column index can't be one and letter index
        # -- can't be zero since you'd get a negative index for 
        # -- querying rows and notic how column can't be one since 
        # -- you'd append 0 to the hits
        while(col_index != 1 and letter_index_cp != 0):
            pos_hits.append(self.rows[letter_index_cp - 1] + str(col_index - 1))
            letter_index_cp -= 1
            col_index -= 1
        
        # -- resetting indexes
        col_index = col_num
        letter_index_cp = letter_index
        
        # get right backward hits 
        while(col_index <= 7 and letter_index_cp != 0):
            pos_hits.append(self.rows[letter_index_cp -1] + str(col_index + 1))
            letter_index_cp -= 1 
            col_index += 1

        # get right forward hits
        
        # -- resetting indexes
        col_index = col_num
        letter_index_cp = letter_index

        # -- notice how column number land letter number can't be 7
        # -- because you are adding one when appending 
        while(col_index <= 7 and letter_index_cp != 7):
            pos_hits.append(self.rows[letter_index_cp + 1] + str(col_index + 1))
            col_index += 1
            letter_index_cp += 1
        

        # -- resetting indexes
        col_index = col_num
        letter_index_cp = letter_index
        
        # get left forward hits 
        while(col_index != 1 and letter_index_cp != 7):
            pos_hits.append(self.rows[letter_index_cp+1] + str(col_index - 1))
            col_index -= 1 
            letter_index_cp += 1

        return pos_hits

    def __eq__(self, c):
        return self.board == c.board


if __name__ == "__main__":
    b = ChessBoard()
    b.placeQueen('A1')
    b.placeQueen('B2')
    b.draw()
    print(b.getDiagonals('C5'))



