import pygame
import sys, os
import tkinter as tk
from tkinter import messagebox

import data


def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def on_closing():
    """Exit python when the player clicks the cross button on the top right
    window
    """
    sys.exit()


class DisplayMap():
    def __init__(self,screen_size):
        self.screen = pygame.display.set_mode(screen_size,pygame.RESIZABLE,0,32)
                # pygame.FULLSCREEN RESIZABLE
        self.bg_img = pygame.image.load(resource_path('figures/1_0_kingdom_map.png'))
        self.explanation_window('Moverse por el mapa',
            'Este es el mapa del reino (como reconocerás)\nHaz click en el mapa para moverte a algún lugar')

    def explanation_window(self,root_title,root_msg):
        self.root = tk.Tk()
        self.root.eval('tk::PlaceWindow . center')
        self.root.attributes("-topmost", True)
        self.root.protocol("WM_DELETE_WINDOW",on_closing)
        self.root.title(root_title)

        explanation_label = tk.Label(self.root,text=root_msg,font=('Helvetica', 16))
        explanation_label.pack()

        ok_button = tk.Button(self.root,text='Okey',command=self.destroy_frame,font=('Helvetica', 16))
        ok_button.pack()
        
        self.root.mainloop()

    def destroy_frame(self):
        """When necessary, destroy the frame so that the next frame can be
        generated
        """
        self.root.destroy()
        self.root.quit()

    def initial_setup(self):
        pygame.display.update()
        self.screen.blit(self.bg_img, (0,0))
        
    def get_place(self,event):
        mx, my = pygame.mouse.get_pos()
        for place, c in data.kingdom_map_positions.items():
            if mx > c[0] and mx < c[2] and my > c[1] and my < c[3]:
                if place != 'Castillo':
                    self.explanation_window('No te entretengas',
                        'La princesa te ha pedido ayuda. ¿No deberías ir directa al castillo?')
                    # return False
                if place == 'Castillo':
                    return True


def main_kingdom_map():
    """Main function for the
    """
    screen_size = [680,560]

    pygame.init()
    pygame.display.set_caption('Mapa del reino. Haz click para moverte')
    screen = DisplayMap(screen_size)

    running = True
    while running:
        screen.initial_setup()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                status = screen.get_place(event)
                if status:
                    running = False
                    pygame.display.quit()


# main_kingdom_map()