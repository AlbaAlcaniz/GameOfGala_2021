import tkinter as tk
from tkinter import messagebox
import sys, os
import pygame


def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class MainTopLevel():
    """Create a tkinter window on top of the main window with the explanation 
    of the game.
    """
    def __init__(self, master, corr_string, pygame_win=False):
        """Create the top level window.

        Args:
            master (tkinter.Tk): window of the general game.
            corr_string (str): string with the correct message that the player
                has to write on the text box.
        """
        self.top = tk.Toplevel(master)
        self.top.attributes('-topmost', True)
        self.top.attributes('-topmost', False)
        self.top.geometry("+600+100")
        self.corr_string = corr_string
        if pygame_win:
            pygame.display.update()

    def retrieve_input(self):
        """Read the string written in a text box. 
        If the message written on the text box is correct, the game window is
        destroyed. Otherwise, a warning message stating that the message is
        incorrect is shown.
        """
        inputValue = self.textBox.get('1.0','end-1c')
        clean_input = ''.join([x for x in inputValue if x.isalpha()])
        if clean_input.upper() == self.corr_string:
            self.top.destroy()
            self.top.quit()
        else:
            self.message_box()
            self.top.attributes('-topmost', True)
            self.top.attributes('-topmost', False)

    def message_box(self):
        """Generate a warning message in case the message is not correct"""
        root = tk.Toplevel(self.top)
        root.attributes('-topmost', True)
        root.geometry("+650+100")
        root.withdraw()
        messagebox.showinfo('Oh oh', 'Wrong message. Try again!')
        try:
            root.destroy()
        except:
            pass

    def display_image(self, img, img_pos):
        """Display images on the game window.

        Args:
            img (tkinter.PhotoImage): image to be displayed in the window
            img_pos (list): positions defining the location of the image
        """
        image = tk.Label(self.top, image=img)
        image.grid(row=img_pos[0], column=img_pos[1],
            columnspan=img_pos[2], rowspan=img_pos[3])

    def create_entries(self, text_font, bg_color, entries_distribution):
        """Create five entries where the result of the minigame operations can
        be written.

        Args:
            text_font (int): font size of the text
            bg_color (list): list of strings representing hex colors for the
                background of each of the entries
            entries_distribution (string): either 'h' or 'v' indicating that
                the entries are displayed next to each other or on top of one
                another.
        """
        for i in range(5):
            if entries_distribution == 'h':
                entry_row = 1
                entry_col = i
            else:
                entry_row = i
                entry_col = 1
            tk.Entry(
                self.top, 
                font=('Helvetica', text_font),
                background=bg_color[i],
                width=3
            ).grid(row=entry_row, column=entry_col)

    def create_text_box(self, box_pos, text_font):
        """Create text box where the message can be written by the player.

        Args:
            box_pos (list): positions defining the location of the box
            text_font (int): font size of the text
        """
        self.textBox = tk.Text(self.top, height=1, width=17,
            font=('Helvetica', text_font))
        self.textBox.grid(row=box_pos[0], column=box_pos[1],
            columnspan=box_pos[2], rowspan=box_pos[3])

    def create_next_button(self, img_next, but_pos):
        """Create a button for when the string is ready to be written.

        Args:
            img_next (tkinter.PhotoImage): image displayed in the button
            but_pos (list): positions defining the location of the button
        """
        tk.Button(self.top, height=50, width=50, image=img_next, 
            command=lambda: self.retrieve_input()).grid(row=but_pos[0], 
            column=but_pos[1])


def main_password(master):
    """Function for the series game, where numerical series need to be
    continued. The final number of the series needs to be related to the
    alphabet position in order to know the message.
    This function imports the images needed for the game and displays them in
    the window.

    Args:
        master (tkinter.Tk): window of the general game.
    """
    top_series = MainTopLevel(master,'AZUL')

    img1 = tk.PhotoImage(file=resource_path('figures/3_2_series.png'))
    img2 = tk.PhotoImage(file=resource_path('figures/3_2_alphabet.png'))
    img_next = tk.PhotoImage(file=resource_path('figures/0_0_next.png'))
    text_font = 32
    bg_color = ['#0000ff','#ffff00','#ffffff','#ff79dc','#00ffff']

    top_series.display_image(img1, [0,0,1,5])
    top_series.create_entries(text_font, bg_color, 'v')
    top_series.display_image(img2, [0,2,2,5])
    top_series.create_text_box([5,2,None,None], text_font)
    top_series.create_next_button(img_next, [5,3])

    top_series.top.mainloop()


main_password()