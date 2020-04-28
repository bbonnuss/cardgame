import pygame
from os.path import join

# return value
# -1 = exit game
# 0 = main menu
# 1 = game selection
# 2 = pok game
#
# Loader ======================= Loader ======================= Loader
class Sound_Loader():
    def __init__(self):
        self.main_menu = pygame.mixer.Sound(join('resource','main_theme.wav'))


class Image_Loader():
    def __init__(self):
        self.main_bg = pygame.image.load(join('resource','main_bg.png')).convert_alpha()
        self.selection_bg = pygame.image.load(join('resource','Selection.png')).convert_alpha()
        self.pok_bg = pygame.image.load(join('resource','pok_bg.png')).convert_alpha()
        self.bg = pygame.image.load(join('resource','bg.png')).convert_alpha()

# Function ======================= Function ======================= Function
def is_hit_box(position,box_a,box_b):
    # position คือ ตำแหน่งเมาส์ (tuple 2 element)(จุด x,y)
    # box_a คือ จุดมุมซ้ายบนของปุ่ม (tuple 2 element)(จุด x,y)
    # box_b คือ จุดมุมขวาล่างของปุ่ม (tuple 2 element)(จุด x,y)

    if box_a[0] < position[0] < box_b[0] : # ถ้า x อยู่ระหว่างนั้น
        if box_a[1] < position[1] < box_b[1] :
            return True
    
    return False

# Class ======================= Class ======================= Class 
# Menu ======================= Menu
class Menu_Controller():
    def __init__(self):
        self.main_menu = Main_Menu()
        self.game_selection_menu = Game_Selection_Menu()
        self.pok_game_menu = Pok_Game_Menu()
    

    def main(self):
        return self.main_menu.run()

    def selection(self):
        return self.game_selection_menu.run()
    
    def pok(self):
        return self.pok_game_menu.run()

class Menu():   
    def __init__(self):
        global loaded_image
        global loaded_sound
        global resolution

        self.background = None
        self.theme_song = None
        self.name = None

    def run(self):
         # set title
        pygame.display.set_caption("Card Game : "+ self.name)

        # วาดพื้นหลัง
        self.draw_bg()
        pygame.display.update()

        # music theme (ต้อง load ใหม่ เพื่อเปิดเสียงแยกจาก effect)
        pygame.mixer.music.load(self.theme_song)
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.play(loops=-1)
    

    def draw_bg(self):
        
        # background 
        window.blit(pygame.transform.scale(self.background, resolution), (0, 0))

class Main_Menu(Menu):
    def __init__(self):
        self.name = "Main Menu"
        self.background = loaded_image.main_bg
        self.theme_song = join('resource','main_theme.wav')
        self.start_button = (215,345),(600,420)
        self.exit_button = (215,450),(600,515)

    
    def run(self):
        super().run()
        
        # loop per second 
        clock = pygame.time.Clock()

        while True:
            # loop per second 
            clock.tick(40)

            # input - output
            for event in pygame.event.get():

                # pointer
                mouse_pos = pygame.mouse.get_pos()
                print (mouse_pos)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickdown = True
                else:
                    clickdown = False
                
                    
                # exit
                if event.type == pygame.QUIT:
                    # stop theme song
                    pygame.mixer.music.stop()
                    pygame.quit()
                
                # Botton ------------------------- Botton

                # start Button (to game selection)
                if is_hit_box(mouse_pos,self.start_button[0], self.start_button[1]):
                    if clickdown:
                        return 1
                
                # exit Button (exit game)
                if is_hit_box(mouse_pos,self.exit_button[0], self.exit_button[1]):
                    if clickdown:
                        return -1




        


class Game_Selection_Menu(Menu):
    def __init__(self):        
        self.name = "Game Selection"
        self.background = loaded_image.selection_bg
        self.theme_song = join('resource','main_theme.wav')
        
        self.pok_button = (215,345),(600,420)
        self.exit_button = (215,450),(600,515)

    def run(self):
        super().run()
        
        # loop per second 
        clock = pygame.time.Clock()

        while True:
            # loop per second 
            clock.tick(40)

            # input - output
            for event in pygame.event.get():

                # pointer
                mouse_pos = pygame.mouse.get_pos()
                print (mouse_pos)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickdown = True
                else:
                    clickdown = False
                
                    
                # exit
                if event.type == pygame.QUIT:
                    # stop theme song
                    pygame.mixer.music.stop()
                    pygame.quit()
                
                # Botton ------------------------- Botton

                # start Button (to game selection)
                if is_hit_box(mouse_pos,self.start_button[0], self.start_button[1]):
                    if clickdown:
                        return 1
                
                # exit Button (exit game)
                if is_hit_box(mouse_pos,self.exit_button[0], self.exit_button[1]):
                    if clickdown:
                        return -1


class Pok_Game_Menu(Menu):
    def __init__(self):
        self.background = None

    def run(self):
        return None

# Mechanic ======================= Mechanic

class deck():
    def __init__(self):
        # data
        self.card = list()
    
    def suffle(self):
        return None

# Main ======================= Main ======================= Main
def main():

    menu = Menu_Controller()
    # start at main menu
    go = menu.main()
    while go != -1:
        if go == 0:
            go = menu.main()
        elif go == 1:
            go = menu.selection()
        elif go == 2:
            go = menu.pok()



# Launcher ======================= Launcher ======================= Launcher 
pygame.init()
resolution = (800,600)
window = pygame.display.set_mode(resolution)
pygame.display.set_caption("Card Game : "+"Loading...")

window.fill((255,255,153)) # make a color at loading screen
pygame.display.update()

loaded_image = Image_Loader() # load image
loaded_sound = Sound_Loader() # load sound

# Run game
main()

# EXIT !
pygame.quit()
