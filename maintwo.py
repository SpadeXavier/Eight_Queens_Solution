import kivy 
kivy.require('1.10.1') 

from kivy.app import App 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.label import Label 
from kivy.uix.image import Image


class ChessLayout(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        
        self.drawBoard()

    def drawBoard(self):
        ''' Creates an 8x8 board with Image widgets, alternating by gray box
        image and black box image '''

        # create 8 by 8 grid of labels 
        gray_turn = True 

        board = {}
        for curr_row in 'ABCDEFGH':
            board[curr_row] = [] 
            for x in range(8):
                if gray_turn:
                    path="gray_box.jpg"
                else:
                    path="black_box.jpg"
                
                self.add_widget(Image(source=path, center=self.center,
                    allow_stretch=True, keep_ratio=False))
                    
                gray_turn = not(gray_turn)

            # next row must start with different color than previous row 
            gray_turn = not(gray_turn)

        print(board)



class ChessApp(App):
    
    def build(self):
        return ChessLayout() 



if __name__ == '__main__':
    app = ChessApp() 
    app.run() 


























































