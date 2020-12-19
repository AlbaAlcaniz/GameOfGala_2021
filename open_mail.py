import pygame
import sys, os


def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class MainScreen():
    def __init__(self,screen_size):
        self.screen = pygame.display.set_mode(screen_size,pygame.RESIZABLE,0,32)
        self.bg_img = pygame.image.load(resource_path('figures/0_1_youhavemail.png'))

    def initial_setup(self):
        pygame.display.update()
        self.screen.blit(self.bg_img, (0,0))
        
    def check_mail(self,event):
        mx, my = pygame.mouse.get_pos()
        if mx > 108 and mx < 291 and my > 128 and my < 241:
            return True
        else:
            return False

def main_mail():
    """Main function for the
    """
    screen_size = [400,283]

    pygame.init()
    pygame.display.set_caption('Tienes correo')
    screen = MainScreen(screen_size)

    running = True
    while running:
        screen.initial_setup()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                status = screen.check_mail(event)
                if status:
                    running = False
                    pygame.display.quit()


# main_mail()