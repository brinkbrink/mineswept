from tkinter import Button, Label
import utils
import settings
import random

class Cell:
    all = []
    cell_count_label_object = None
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
            highlightbackground='grey',
            highlightthickness='1'
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Key><Button-1>', self.right_click_actions)
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text=f"Cells Left: {settings.CELL_COUNT}",
            font=("", 30),
            width=int(utils.width_prct(5/settings.GRID_SIZE)),
            height=int(utils.height_prct(4/settings.GRID_SIZE)),
            highlightbackground='blue',
            highlightthickness='10'
        )
        Cell.cell_count_label_object = lbl


    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

    def get_cell_by_axis(self, x, y):
        # Return a cell object based on x, y values
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
        ]
        
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        
        return counter

    def show_cell(self):
        self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)

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