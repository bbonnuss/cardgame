import pygame
from os.path import join

# return value
# -1 = exit game
# 0 = main menu
# 1 = game selection
# 2 = pok game
# 32 = credit

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
        self.credit_menu = Credit_Menu()

    def main(self):
        return self.main_menu.run()

    def selection(self):
        return self.game_selection_menu.run()
    
    def pok(self):
        return self.pok_game_menu.run()
    
    def credit(self):
        return self.credit_menu.run()

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

    

    def draw_bg(self):
        
        # background 
        window.blit(pygame.transform.scale(self.background, resolution), (0, 0))

class Main_Menu(Menu):
    def __init__(self):
        self.name = "Main Menu"
        self.background = loaded_image.main_bg
        self.theme_song = None
        self.start_button = (215,345),(600,420)
        self.exit_button = (215,450),(600,515)
        self.credit_button = (635,510),(780,577)

    
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
                    #print ("start")
                    if clickdown:
                        return 1
                
                # exit Button (exit game)
                if is_hit_box(mouse_pos,self.exit_button[0], self.exit_button[1]):
                    #print ("exit game")
                    if clickdown:
                        return -1
                
                # exit Button (exit game)
                if is_hit_box(mouse_pos,self.exit_button[0], self.exit_button[1]):
                    #print ("exit game")
                    if clickdown:
                        return 9


class Credit_Menu(Menu):
    def __init__(self):
        self.name = "Credit"
        self.background = loaded_image.bg
        self.theme_song = None

        self.next_button = (0,0),(0,0)
        self.back_button = (0,0),(0,0)

    def draw_page1(self):
        return None

class Game_Selection_Menu(Menu):
    def __init__(self):        
        self.name = "Game Selection"
        self.background = loaded_image.selection_bg
        self.theme_song = None
        
        self.pok_button = (200,90),(620,175)
        self.x_button = (200,230),(620,315)
        self.y_button = (200,360),(620,440)
        self.back_button = (647,511),(782,578)

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
                #print (mouse_pos)

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

                # Pok deng Button (to game selection)
                if is_hit_box(mouse_pos,self.pok_button[0], self.pok_button[1]):
                    #print ("pok")
                    if clickdown:
                        return 2
                
                # x Button
                if is_hit_box(mouse_pos,self.x_button[0], self.x_button[1]):
                    #print ("x")
                    if clickdown:
                        print ("comming soon...")

                # x Button
                if is_hit_box(mouse_pos,self.y_button[0], self.y_button[1]):
                    #print ("y")
                    if clickdown:
                        print ("comming soon...")

                # back Button (main menu)
                if is_hit_box(mouse_pos,self.back_button[0], self.back_button[1]):
                    #print ("back")
                    if clickdown:
                        return 0


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
    # init 
    menu = Menu_Controller()

    # start at main menu
    go = 0
    while go != -1:
        if go == 0:
            # open main music theme (ต้อง load ใหม่ เพื่อเปิดเสียงแยกจาก effect)
            pygame.mixer.music.load(join('resource','main_theme.wav'))
            pygame.mixer.music.set_volume(0.25)
            pygame.mixer.music.play(loops=-1)

            go = menu.main()

        elif go == 1:
            go = menu.selection()
        elif go == 2:
            # stop main music theme
            pygame.mixer.music.stop()

            go = menu.pok()
        elif go == 32:
            go = menu.credit()



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
