from tkinter import Button
import utils

class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=int(utils.width_prct(.8)),
            height=int(utils.height_prct(.6)),
            text='Text',
            # highlightbackground='blue'
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Key><Button-1>', self.right_click_actions)
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print(event)
        print("I am left clicked!")

    def right_click_actions(self, event):
        print(event)
        print("I am right clicked!")