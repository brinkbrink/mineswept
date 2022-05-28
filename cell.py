from tkinter import Button, Label, messagebox
import utils
import settings
import random
import sys

class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
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
        btn.bind('<Key><Button-1>', self.right_click_actions)
        btn.bind('<Button-1>', self.left_click_actions)
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text=f"Cells Left: {Cell.cell_count}",
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
            # if cell count is equal to mine count, winner!
            if Cell.cell_count == settings.MINE_COUNT:
                messagebox.showerror(title='You lose!', message='YOU WIN!!! LOSER!!!')
        # cancel left/rick click events if cell open
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Key><Button-1>')

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
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            # replace the text of cell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left: {Cell.cell_count}"
                    )
            # protect against being mine candidate and show cell at same time
            self.cell_btn_object.configure(highlightbackground='grey')
        # mark the cell as opened
        self.is_opened = True

    def show_mine(self):
        self.cell_btn_object.configure(highlightbackground='red')
        messagebox.showerror(title='You lose!', message='YOU LOSE!!! LOSER!!!')
        sys.exit()

    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                highlightbackground='orange',
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                highlightbackground='grey'
            )
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINE_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"