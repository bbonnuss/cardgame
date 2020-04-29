import pygame
from os.path import join
from numpy.random import choice

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
        self.credit1 = pygame.image.load(join('resource','credit1.png')).convert_alpha()
        self.credit2 = pygame.image.load(join('resource','credit2.png')).convert_alpha()
        self.credit_back = pygame.image.load(join('resource','credit_back.png')).convert_alpha()
        self.credit_next = pygame.image.load(join('resource','credit_next.png')).convert_alpha()
        
        self.spd_ = pygame.image.load(join('resource','credit_next.png')).convert_alpha()

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
                
                # credit Button (exit game)
                if is_hit_box(mouse_pos,self.credit_button[0], self.credit_button[1]):
                    #print ("credit")
                    if clickdown:
                        return 32


class Credit_Menu(Menu):
    def __init__(self):
        self.name = "Credit"
        self.background = loaded_image.bg
        self.theme_song = None
        self.page = 1

        self.next_button = (550,500),(700,570)
        self.back_button = (100,500),(250,570)
    
    def run(self):
        super().run()
        
        # loop per second 
        clock = pygame.time.Clock()

        # draw credit page
        self.draw_page()
        pygame.display.update()

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
                # next Button
                if is_hit_box(mouse_pos,self.next_button[0], self.next_button[1]):
                    #print ("nextpage")
                    if clickdown:
                        if self.page == 1:
                            self.page += 1

                             # draw credit page
                            self.draw_bg()
                            self.draw_page()
                            pygame.display.update()

                # back Button (main menu)
                if is_hit_box(mouse_pos,self.back_button[0], self.back_button[1]):
                    #print ("back")
                    if clickdown:
                        if self.page == 1:
                            return 0
                        else:
                            self.page -= 1
                            
                            # draw credit page
                            self.draw_bg()
                            self.draw_page()
                            pygame.display.update()


    def draw_page(self): # draw text , next&back button
        if self.page == 1:
            # text
            window.blit(pygame.transform.scale(loaded_image.credit1, (600,400)), (100, 50))
            # back button
            window.blit(pygame.transform.scale(loaded_image.credit_back, (150, 70)), self.back_button[0])
            # next button
            window.blit(pygame.transform.scale(loaded_image.credit_next, (150, 70)), self.next_button[0])

        elif self.page == 2:
            # text
            window.blit(pygame.transform.scale(loaded_image.credit2, (600,400)), (100, 50))
            # back button
            window.blit(pygame.transform.scale(loaded_image.credit_back, (150, 70)), self.back_button[0])
            
        
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
                
                    
                # window exit button
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
        self.name = "Pok Deng"
        self.background = loaded_image.bg
        self.theme_song = None
        self.draw_deck = Deck()
        self.trash_deck = Deck()
        self.game_state = 0
        # game_state 
        # 0 = start phase
        # 1 = draw 1
        # 2 = draw 2
        # 3 = pok
        # 4 = ask for draw 3?          
        # 5 = draw 3
        # 6 = result
        

        self.start_button = (0,0),(0,0)
        self.draw_button = (0,0),(0,0)
        self.not_draw_button = (0,0),(0,0)
        self.suffle_button = (0,0),(0,0)
        self.exit_button = (0,0),(0,0)

    def run(self):
        super().run()
        
        # loop per second 
        clock = pygame.time.Clock()

        while True:
            # loop per second 
            clock.tick(50)

            
            self.draw_bg()      # draw_bg
            self.draw_card()    # draw player's card & draw deck 
            self.draw_ui()      # draw result msg      

            # input - output
            for event in pygame.event.get():

                # pointer
                mouse_pos = pygame.mouse.get_pos()
                print (mouse_pos)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickdown = True
                else:
                    clickdown = False
                
                    
                # window exit button
                if event.type == pygame.QUIT:
                    # stop theme song
                    pygame.mixer.music.stop()
                    pygame.quit()
                
                # Botton ------------------------- Botton

                # start/restart Button 
                if is_hit_box(mouse_pos,self.start_button[0], self.start_button[1]) and (self.game_state == 0 or self.game_state == 6):
                    #print ("start")
                    if clickdown:
                        self.game_state += 1
                        
                
                #  draw Button
                if is_hit_box(mouse_pos,self.draw_button[0], self.draw_button[1]) and self.game_state == 4:
                    #print ("draw")
                    if clickdown:
                        print ("draw")

                # not draw Button
                if is_hit_box(mouse_pos,self.not_draw_button[0], self.not_draw_button[1]) and self.game_state == 4:
                    #print ("no draw")
                    if clickdown:
                        print ("no draw")

                # request suffle Button
                if is_hit_box(mouse_pos,self.suffle_button[0], self.suffle_button[1]) and False:    # not use for now
                    #print ("suffle")
                    if clickdown:
                        print ("suffle")

                # finish Button (main menu)
                if is_hit_box(mouse_pos,self.exit_button[0], self.exit_button[1]) and self.game_state == 6:
                    #print ("back")
                    if clickdown:
                        return 0


    def draw_card(self):
        return None
    

    def draw_ui(self):
        return None

# Mechanic ======================= Mechanic

class Deck():
    def __init__(self):
        # data
        self.card = [None] *52
    
    def suffle(self):
        return None


class Card():
    def __init__(self)
        self.image = None
        self.num = -1
        self.suit = -1
        self.char = None
    
    def get_num(self):
        return self.num
    
    def get_suit(self):
        return self.suit
    
    def get_image(self):
        return self.image

    def is_char(self):
        return self.char


class spd_A(Card):
    def __init__(self):
        self.image = loaded_image.spd_A
        self.num = 1
        self.suit = 4
        self.char = True

class spd_2(Card):
    def __init__(self):
        self.image = loaded_image.spd_2
        self.num = 2
        self.suit = 4
        self.char = False

class spd_3(Card):
    def __init__(self):
        self.image = loaded_image.spd_3
        self.num = 3
        self.suit = 4
        self.char = False

class spd_4(Card):
    def __init__(self):
        self.image = loaded_image.spd_4
        self.num = 4
        self.suit = 4
        self.char = False

class spd_5(Card):
    def __init__(self):
        self.image = loaded_image.spd_5
        self.num = 5
        self.suit = 4
        self.char = False

class spd_6(Card):
    def __init__(self):
        self.image = loaded_image.spd_6
        self.num = 6
        self.suit = 4
        self.char = False

class spd_7(Card):
    def __init__(self):
        self.image = loaded_image.spd_7
        self.num = 7
        self.suit = 4
        self.char = False

class spd_8(Card):
    def __init__(self):
        self.image = loaded_image.spd_8
        self.num = 8
        self.suit = 4
        self.char = False

class spd_9(Card):
    def __init__(self):
        self.image = loaded_image.spd_9
        self.num = 9
        self.suit = 4
        self.char = False

class spd_10(Card):
    def __init__(self):
        self.image = loaded_image.spd_10
        self.num = 10
        self.suit = 4
        self.char = False

class spd_J(Card):
    def __init__(self):
        self.image = loaded_image.spd_J
        self.num = 0
        self.suit = 4
        self.char = True

class spd_Q(Card):
    def __init__(self):
        self.image = loaded_image.spd_Q
        self.num = 0
        self.suit = 4
        self.char = True

class spd_K(Card):
    def __init__(self):
        self.image = loaded_image.spd_K
        self.num = 0
        self.suit = 4
        self.char = True

class hrt_A(Card):
    def __init__(self):
        self.image = loaded_image.hrt_A
        self.num = 1
        self.suit = 4
        self.char = True

class hrt_2(Card):
    def __init__(self):
        self.image = loaded_image.hrt_2
        self.num = 2
        self.suit = 4
        self.char = False

class hrt_3(Card):
    def __init__(self):
        self.image = loaded_image.hrt_3
        self.num = 3
        self.suit = 4
        self.char = False

class hrt_4(Card):
    def __init__(self):
        self.image = loaded_image.hrt_4
        self.num = 4
        self.suit = 4
        self.char = False

class hrt_5(Card):
    def __init__(self):
        self.image = loaded_image.hrt_5
        self.num = 5
        self.suit = 4
        self.char = False

class hrt_6(Card):
    def __init__(self):
        self.image = loaded_image.hrt_6
        self.num = 6
        self.suit = 4
        self.char = False

class hrt_7(Card):
    def __init__(self):
        self.image = loaded_image.hrt_7
        self.num = 7
        self.suit = 4
        self.char = False

class hrt_8(Card):
    def __init__(self):
        self.image = loaded_image.hrt_8
        self.num = 8
        self.suit = 4
        self.char = False

class hrt_9(Card):
    def __init__(self):
        self.image = loaded_image.hrt_9
        self.num = 9
        self.suit = 4
        self.char = False

class hrt_10(Card):
    def __init__(self):
        self.image = loaded_image.hrt_10
        self.num = 10
        self.suit = 4
        self.char = False

class hrt_J(Card):
    def __init__(self):
        self.image = loaded_image.hrt_J
        self.num = 0
        self.suit = 4
        self.char = True

class hrt_Q(Card):
    def __init__(self):
        self.image = loaded_image.hrt_Q
        self.num = 0
        self.suit = 4
        self.char = True

class hrt_K(Card):
    def __init__(self):
        self.image = loaded_image.hrt_K
        self.num = 0
        self.suit = 4
        self.char = True

class dmd_A(Card):
    def __init__(self):
        self.image = loaded_image.dmd_A
        self.num = 1
        self.suit = 4
        self.char = True

class dmd_2(Card):
    def __init__(self):
        self.image = loaded_image.dmd_2
        self.num = 2
        self.suit = 4
        self.char = False

class dmd_3(Card):
    def __init__(self):
        self.image = loaded_image.dmd_3
        self.num = 3
        self.suit = 4
        self.char = False

class dmd_4(Card):
    def __init__(self):
        self.image = loaded_image.dmd_4
        self.num = 4
        self.suit = 4
        self.char = False

class dmd_5(Card):
    def __init__(self):
        self.image = loaded_image.dmd_5
        self.num = 5
        self.suit = 4
        self.char = False

class dmd_6(Card):
    def __init__(self):
        self.image = loaded_image.dmd_6
        self.num = 6
        self.suit = 4
        self.char = False

class dmd_7(Card):
    def __init__(self):
        self.image = loaded_image.dmd_7
        self.num = 7
        self.suit = 4
        self.char = False

class dmd_8(Card):
    def __init__(self):
        self.image = loaded_image.dmd_8
        self.num = 8
        self.suit = 4
        self.char = False

class dmd_9(Card):
    def __init__(self):
        self.image = loaded_image.dmd_9
        self.num = 9
        self.suit = 4
        self.char = False

class dmd_10(Card):
    def __init__(self):
        self.image = loaded_image.dmd_10
        self.num = 10
        self.suit = 4
        self.char = False

class dmd_J(Card):
    def __init__(self):
        self.image = loaded_image.dmd_J
        self.num = 0
        self.suit = 4
        self.char = True

class dmd_Q(Card):
    def __init__(self):
        self.image = loaded_image.dmd_Q
        self.num = 0
        self.suit = 4
        self.char = True

class dmd_K(Card):
    def __init__(self):
        self.image = loaded_image.dmd_K
        self.num = 0
        self.suit = 4
        self.char = True

class cub_A(Card):
    def __init__(self):
        self.image = loaded_image.cub_A
        self.num = 1
        self.suit = 4
        self.char = True

class cub_2(Card):
    def __init__(self):
        self.image = loaded_image.cub_2
        self.num = 2
        self.suit = 4
        self.char = False

class cub_3(Card):
    def __init__(self):
        self.image = loaded_image.cub_3
        self.num = 3
        self.suit = 4
        self.char = False

class cub_4(Card):
    def __init__(self):
        self.image = loaded_image.cub_4
        self.num = 4
        self.suit = 4
        self.char = False

class cub_5(Card):
    def __init__(self):
        self.image = loaded_image.cub_5
        self.num = 5
        self.suit = 4
        self.char = False

class cub_6(Card):
    def __init__(self):
        self.image = loaded_image.cub_6
        self.num = 6
        self.suit = 4
        self.char = False

class cub_7(Card):
    def __init__(self):
        self.image = loaded_image.cub_7
        self.num = 7
        self.suit = 4
        self.char = False

class cub_8(Card):
    def __init__(self):
        self.image = loaded_image.cub_8
        self.num = 8
        self.suit = 4
        self.char = False

class cub_9(Card):
    def __init__(self):
        self.image = loaded_image.cub_9
        self.num = 9
        self.suit = 4
        self.char = False

class cub_10(Card):
    def __init__(self):
        self.image = loaded_image.cub_10
        self.num = 10
        self.suit = 4
        self.char = False

class cub_J(Card):
    def __init__(self):
        self.image = loaded_image.cub_J
        self.num = 0
        self.suit = 4
        self.char = True

class cub_Q(Card):
    def __init__(self):
        self.image = loaded_image.cub_Q
        self.num = 0
        self.suit = 4
        self.char = True

class cub_K(Card):
    def __init__(self):
        self.image = loaded_image.cub_K
        self.num = 0
        self.suit = 4
        self.char = True


class Player():
    def __init__(self, bot=False):
        self.hand_card = list()
        self.bot = bot
        self.num = 0
    

    def draw(self, card):
        self.hand_card.append(card)
        self.num += 1
        self.hand_card.sort()
    
    def clear_hand(self):
        self.hand_card = list()
        self.num = 0
    
    def get_point(self):
        # return int 
        point = 0
        for card in self.hand_card:
            point += (card.get_num()%10)

        return point


    def is_straight(self): # ไพ่เรียง? 
        # return true when 3 card are straight
        if self.num == 3:
            if self.hand_card[1].get_num()-self.hand_card[0].get_num() == 1:
                if self.hand_card[2].get_num()-self.hand_card[1].get_num() == 1:
                    return True
        return False

    def is_flood(self):
        # return true when 3 card are the same suit
        if self.num < 3:
            return False
        suit_list = self.get_suit()
        for i in range(0,self.num-1,1):
            if suit_list[i] != suit_list[i+1]:
                return False
        return True        


    def is_tong(self):
        # return true when 3 card are the same number
        if self.num < 3:
            return False
        num_list = self.get_num()
        for i in range(0,self.num-1,1):
            if num_list[i] != num_list[i+1]:
                return False
        return True        

    def get_suit(self):
        # return list of suit
        suit = list()
        i=0
        for card in self.hand_card:
            suit[i] = card.get_suit()
            i += 1
        return suit
    
    def get_num(self):
        # return list of num
        num = list()
        i=0
        for card in self.hand_card:
            num[i] = card.get_num()
            i += 1
        return num

    def is_draw(self):
        if self.bot :
            draw_rate = 0.50
            draw = bool(choice([True,False],p=[draw_rate, 1-draw_rate]))
            return draw
    
    def is_bot(self):
        return self.bot
    


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
