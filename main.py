import kivy 
kivy.require('1.10.1') 

from kivy.app import App 
from kivy.graphics import Color, Rectangle 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.pagelayout import PageLayout 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.label import Label 
from kivy.uix.image import Image
from kivy.uix.button import Button 

from simulation import Simulation 

class MasterLayout(BoxLayout):
    
    solutions = [] 
    counter = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        self.rows=2
        self.orientation='vertical' 

        s = Simulation()
        self.solutions = s.getSolutions()
        print(len(self.solutions))
        
        self.draw_solution() 
    
    def draw_solution(self):
        bl = BoxLayout(size_hint_y=None, height=20)
        # heading_layout = BoxLayout(size_hint_y=None, height=20)
        n = Button(text="Next", size_hint_y=None, height="20", size_hint_x=None, width="40", pos_hint={'right': 1})
        p = Button(text="Prev", size_hint_y=None, height="20", size_hint_x=None, width="40", pos_hint={'left': 1})
        n.bind(on_press=self.next_solution)
        p.bind(on_press=self.prev_solution)

        bl.add_widget(p)
        bl.add_widget(n)

        self.add_widget(bl)
        self.add_widget(ChessLayout(self.solutions[self.counter]))


    def next_solution(self, instance):
        self.counter += 1 
        self.clear_widgets()  
        self.draw_solution()

    def prev_solution(self, instance):
        self.counter -= 1 
        self.clear_widgets()  
        self.draw_solution()


class ChessLayout(BoxLayout):

    board = {} 
    chess_rows = 'ABCDEFGH'

    def __init__(self, solution, **kwargs):
        super().__init__(**kwargs) 
        self.drawBoard()
        self.drawSolution(solution)

    def drawSolution(self, s):
        ''' Takes a dictionary solution and draw it on the board ''' 
        for row_letter, row_values in s.items():
            for index,val in enumerate(row_values):
                if val == 'Q':
                    self.setQueen(row_letter + str(index+1))





    def drawBoard(self):
        ''' Creates an 8x8 board with Image widgets, alternating by gray box
        image and black box image '''

        # create 8 by 8 grid of Image widgets with Labels on side denoting row
        # and columns 

        # Top headings 
        heading_layout = BoxLayout(size_hint_y=None, height=20)
        self.add_widget(heading_layout) 
        for x in range(1,9):
            l = Label(text=str(x), size_hint_x=.1) 
            heading_layout.add_widget(l)

        # Box Layout for board and column 
        board_col_layout = BoxLayout(orientation="horizontal") 
        self.add_widget(board_col_layout) 
        # Column headings  
        col_layout = BoxLayout(orientation="vertical", size_hint_x=None, width=20) 
        board_col_layout.add_widget(col_layout) 
        for x in self.chess_rows:
            l = Label(text=x) 
            col_layout.add_widget(l)

        # Chess board 
        gl = GridLayout(rows=8) 
        board_col_layout.add_widget(gl)
        gray_turn = True 

        for curr_row in self.chess_rows:
            self.board[curr_row] = [] 
            for x in range(8):
                if gray_turn:
                    path="gray_box.jpg"
                else:
                    path="black_box.jpg"
                
                image = Image(source=path, center=self.center, allow_stretch=True, keep_ratio=False)

                self.board[curr_row].append(image)
                gl.add_widget(image)

                gray_turn = not(gray_turn)

            # next row must start with different color than previous row 
            gray_turn = not(gray_turn)

    def setQueen(self, pos):
        ''' Sets a position specified by row and number(e.g, G4) to the image
        given ''' 

        row_letter = pos[0] 
        col_number = int(pos[1])

        image_obj = self.board[row_letter][col_number-1]
        if row_letter in 'ACEG':
            if col_number % 2 == 0: 
                image_obj.source='queen_black_bkgrd.jpg' 
            else:
                image_obj.source='queen_gray_bkgrd.jpg' 
        else:
            if col_number % 2 == 0: 
                image_obj.source='queen_gray_bkgrd.jpg' 
            else:
                image_obj.source='queen_black_bkgrd.jpg' 




class ChessApp(App):
    
    def build(self):
        return MasterLayout() 



if __name__ == '__main__':
    app = ChessApp() 
    app.run() 


























































