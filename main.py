from tkinter import *

root = Tk()
# override the settings of the window
root.configure(bg="black")
root.geometry('1440x720')
root.title('Mineswept')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='red', # change later to black
    width=1440,
    height=180
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='blue', # change later to black
    width=360,
    height=540
)

left_frame.place(x=0, y=180)

# run the window
root.mainloop()