from tkinter import Button
import utils
import settings
import random

class Cell:
    all = []
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # append the object to the Cell.all list
        Cell.all.append(self)


    def create_btn_object(self, location):
        btn = Button(
            location,
            width=int(utils.width_prct(5/settings.GRID_SIZE)),
            height=int(utils.height_prct(4/settings.GRID_SIZE)),
            text=f"{self.x, self.y}",
            highlightbackground='grey',
            highlightthickness='1'
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Key><Button-1>', self.right_click_actions)
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    def get_cell_by_axis(self, x, y):
        # Return a cell object based on x, y values
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def show_cell(self):
        surrounded_cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
        ]
        print(surrounded_cells)

    def show_mine(self):
        # A logic to interrupt the game and display message that player lost
        self.cell_btn_object.configure(highlightbackground='red')

    def right_click_actions(self, event):
        print(event)
        print("I am right clicked!")

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINE_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"