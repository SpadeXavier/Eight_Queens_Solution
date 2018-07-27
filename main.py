import kivy 
kivy.require('1.10.1') 

from kivy.app import App 
from kivy.graphics import Color, Rectangle 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.label import Label 
from kivy.uix.image import Image


class ChessLayout(GridLayout):

    board = {} 
    chess_rows = 'ABCDEFGH'

    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        self.rows = 8  
        self.drawBoard()
        self.setPosImage('G8', 'queen.jpg')

    def drawBoard(self):
        ''' Creates an 8x8 board with Image widgets, alternating by gray box
        image and black box image '''

        # create 8 by 8 grid of Image widgets with Labels on side denoting row
        # and columns 
        gray_turn = True 

        for curr_row in self.chess_rows:
            self.board[curr_row] = [] 
            l = Label(text=curr_row, size_hint_x=.1)
            self.add_widget(l)

            for x in range(8):
                if gray_turn:
                    path="gray_box.jpg"
                else:
                    path="black_box.jpg"
                
                image = Image(source=path, center=self.center, allow_stretch=True, keep_ratio=False)

                self.board[curr_row].append(image)
                self.add_widget(image)

                gray_turn = not(gray_turn)

            # next row must start with different color than previous row 
            gray_turn = not(gray_turn)


        print(self.board)

    def setPosImage(self, pos, image):
        ''' Sets a position specified by row and number(e.g, G4) to the image
        given ''' 

        row_letter = pos[0] 
        col_number = int(pos[1])

        image_obj = self.board[row_letter][col_number-1]
        image_obj.source=''



class ChessApp(App):
    
    def build(self):
        return ChessLayout() 



if __name__ == '__main__':
    app = ChessApp() 
    app.run() 


























































