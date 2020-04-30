import pygame
from os.path import join
from numpy.random import choice
from random import shuffle

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
        self.bye = pygame.mixer.Sound(join('resource','bye.wav'))


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
        
        self.back_card = pygame.image.load(join('resource','back_card.png')).convert_alpha()

        self.spd_A = pygame.image.load(join('resource','spd_A.png')).convert_alpha()
        self.spd_2 = pygame.image.load(join('resource','spd_2.png')).convert_alpha()
        self.spd_3 = pygame.image.load(join('resource','spd_3.png')).convert_alpha()
        self.spd_4 = pygame.image.load(join('resource','spd_4.png')).convert_alpha()
        self.spd_5 = pygame.image.load(join('resource','spd_5.png')).convert_alpha()
        self.spd_6 = pygame.image.load(join('resource','spd_6.png')).convert_alpha()
        self.spd_7 = pygame.image.load(join('resource','spd_7.png')).convert_alpha()
        self.spd_8 = pygame.image.load(join('resource','spd_8.png')).convert_alpha()
        self.spd_9 = pygame.image.load(join('resource','spd_9.png')).convert_alpha()
        self.spd_10 = pygame.image.load(join('resource','spd_10.png')).convert_alpha()
        self.spd_J = pygame.image.load(join('resource','spd_J.png')).convert_alpha()
        self.spd_Q = pygame.image.load(join('resource','spd_Q.png')).convert_alpha()
        self.spd_K = pygame.image.load(join('resource','spd_K.png')).convert_alpha()

        self.hrt_A = pygame.image.load(join('resource','hrt_A.png')).convert_alpha()
        self.hrt_2 = pygame.image.load(join('resource','hrt_2.png')).convert_alpha()
        self.hrt_3 = pygame.image.load(join('resource','hrt_3.png')).convert_alpha()
        self.hrt_4 = pygame.image.load(join('resource','hrt_4.png')).convert_alpha()
        self.hrt_5 = pygame.image.load(join('resource','hrt_5.png')).convert_alpha()
        self.hrt_6 = pygame.image.load(join('resource','hrt_6.png')).convert_alpha()
        self.hrt_7 = pygame.image.load(join('resource','hrt_7.png')).convert_alpha()
        self.hrt_8 = pygame.image.load(join('resource','hrt_8.png')).convert_alpha()
        self.hrt_9 = pygame.image.load(join('resource','hrt_9.png')).convert_alpha()
        self.hrt_10 = pygame.image.load(join('resource','hrt_10.png')).convert_alpha()
        self.hrt_J = pygame.image.load(join('resource','hrt_J.png')).convert_alpha()
        self.hrt_Q = pygame.image.load(join('resource','hrt_Q.png')).convert_alpha()
        self.hrt_K = pygame.image.load(join('resource','hrt_K.png')).convert_alpha()

        self.dmd_A = pygame.image.load(join('resource','dmd_A.png')).convert_alpha()
        self.dmd_2 = pygame.image.load(join('resource','dmd_2.png')).convert_alpha()
        self.dmd_3 = pygame.image.load(join('resource','dmd_3.png')).convert_alpha()
        self.dmd_4 = pygame.image.load(join('resource','dmd_4.png')).convert_alpha()
        self.dmd_5 = pygame.image.load(join('resource','dmd_5.png')).convert_alpha()
        self.dmd_6 = pygame.image.load(join('resource','dmd_6.png')).convert_alpha()
        self.dmd_7 = pygame.image.load(join('resource','dmd_7.png')).convert_alpha()
        self.dmd_8 = pygame.image.load(join('resource','dmd_8.png')).convert_alpha()
        self.dmd_9 = pygame.image.load(join('resource','dmd_9.png')).convert_alpha()
        self.dmd_10 = pygame.image.load(join('resource','dmd_10.png')).convert_alpha()
        self.dmd_J = pygame.image.load(join('resource','dmd_J.png')).convert_alpha()
        self.dmd_Q = pygame.image.load(join('resource','dmd_Q.png')).convert_alpha()
        self.dmd_K = pygame.image.load(join('resource','dmd_K.png')).convert_alpha()

        self.cub_A = pygame.image.load(join('resource','cub_A.png')).convert_alpha()
        self.cub_2 = pygame.image.load(join('resource','cub_2.png')).convert_alpha()
        self.cub_3 = pygame.image.load(join('resource','cub_3.png')).convert_alpha()
        self.cub_4 = pygame.image.load(join('resource','cub_4.png')).convert_alpha()
        self.cub_5 = pygame.image.load(join('resource','cub_5.png')).convert_alpha()
        self.cub_6 = pygame.image.load(join('resource','cub_6.png')).convert_alpha()
        self.cub_7 = pygame.image.load(join('resource','cub_7.png')).convert_alpha()
        self.cub_8 = pygame.image.load(join('resource','cub_8.png')).convert_alpha()
        self.cub_9 = pygame.image.load(join('resource','cub_9.png')).convert_alpha()
        self.cub_10 = pygame.image.load(join('resource','cub_10.png')).convert_alpha()
        self.cub_J = pygame.image.load(join('resource','cub_J.png')).convert_alpha()
        self.cub_Q = pygame.image.load(join('resource','cub_Q.png')).convert_alpha()
        self.cub_K = pygame.image.load(join('resource','cub_K.png')).convert_alpha()

        self.start = pygame.image.load(join('resource','start.png')).convert_alpha()
        self.draw = pygame.image.load(join('resource','draw.png')).convert_alpha()
        self.not_draw = pygame.image.load(join('resource','not_draw.png')).convert_alpha()
        self.exit = pygame.image.load(join('resource','exit.png')).convert_alpha()

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
    
    def restart_pok(self):
        self.pok_game_menu = Pok_Game_Menu()

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
        self.game_state = 1
        self.draw_deck = Deck()
        self.is_draw = None
        self.result = [0, 0, 0, 0, 0, 0, 0, 0] # result ตัวสุดท้ายเป็น host
        self.player = [Bot(), Bot(), Bot(), Player(), Bot(), Bot(), Bot(), Bot()] # Bot ตัวสุดท้ายเป็น host
        self.player_pos = [(225, 150), (100, 300), (225, 450), (400, 500), (575, 450), (700, 300), (575, 150), (400, 100)] # ตพแหน่งวางการ์ด
        # game_state 
        # 1 = draw 1
        # 2 = draw 2
        # 3 = pok
        # 4 = ask for draw 3?          
        # 5 = draw 3
        # 6 = result
        

        self.start_button = (630,10),(780,80)
        self.draw_button = (200,260),(350,330)
        self.not_draw_button = (450,260),(600,330)
        self.suffle_button = (0,0),(0,0)
        self.exit_button = (630,520),(780,590)

    def run(self):
        super().run()
        
        # loop per second 
        clock = pygame.time.Clock()

        while True:
            # loop per second 
            clock.tick(50)
            
            self.draw_bg()      # draw_bg
            self.draw_ui()    # draw player's card & draw deck 
            pygame.display.update()   

            # game process
            if self.game_state == 1 or self.game_state == 2:
                #print ("state2")
                for player in self.player:
                    player.draw_in(self.draw_deck.draw_out())   # move card into player

                    self.draw_ui()   # draw player's card & draw deck 
                    pygame.display.update()   

                    pygame.time.delay(200)  # delay for animate

                self.game_state += 1

            elif self.game_state == 3:
                #print ("state3")
                pygame.time.delay(1000)
                if self.player[-1].is_pok(): # host pok
                    self.game_state = 6
                elif self.player[3].is_pok():   # player pok
                    self.game_state += 2
                else:

                    self.game_state += 1

            elif self.game_state == 5:
                #print ("state5")
                i=0
                for player in self.player:
                    if i==3 and self.is_draw :
                        player.draw_in(self.draw_deck.draw_out())
                    elif i!=3 and player.is_draw():
                        player.draw_in(self.draw_deck.draw_out())
                    self.draw_ui()   # draw player's card & draw deck 
                    pygame.display.update()   

                    pygame.time.delay(200)  # delay for animate

                    i += 1   
                self.game_state += 1

            self.draw_ui()    # draw player's card & draw deck  msg button

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

                # restart Button 
                if is_hit_box(mouse_pos,self.start_button[0], self.start_button[1]) and (self.game_state == 6):
                    #print ("start")
                    if clickdown:
                        self.game_state = 1
                        # new deck
                        self.draw_deck = Deck()
                        # reset value
                        self.is_draw = None
                        self.is_collected_stats = False
                        self.player = [Bot(), Bot(), Bot(), Player(), Bot(), Bot(), Bot(), Bot()] # Bot ตัวสุดท้ายเป็น host
                        
                
                #  draw Button
                if is_hit_box(mouse_pos,self.draw_button[0], self.draw_button[1]) and self.game_state == 4:
                    #print ("draw")
                    if clickdown:
                        self.game_state += 1
                        self.is_draw = True

                # not draw Button
                if is_hit_box(mouse_pos,self.not_draw_button[0], self.not_draw_button[1]) and self.game_state == 4:
                    #print ("no draw")
                    if clickdown:
                        self.game_state += 1
                        self.is_draw = False

                # request suffle Button
                if is_hit_box(mouse_pos,self.suffle_button[0], self.suffle_button[1]) and False:    # not use for now
                    #print ("suffle")
                    if clickdown:
                        self.draw_deck.shuffle()

                # finish Button (static display)
                if is_hit_box(mouse_pos,self.exit_button[0], self.exit_button[1]):
                    if clickdown:
                        return 0


    def draw_ui(self): # draw player's card & draw deck msg button
        show=False
        if self.game_state == 6:
            show = True
        i=0
        for player in self.player:
            if player.is_pok():
                player.draw_hand(self.player_pos[i],True)
                self.result[i] = player.draw_result(self.player_pos[i],True)
            else:
                player.draw_hand(self.player_pos[i],show)
                self.result[i] = player.draw_result(self.player_pos[i],show)
            i+=1

        # start button
        if self.game_state == 6:
            window.blit(pygame.transform.scale(loaded_image.start, (150,70)), self.start_button[0])

        
        if self.game_state == 4 and (not self.player[3].is_pok()):
            # draw_button
            window.blit(pygame.transform.scale(loaded_image.draw, (150,70)), self.draw_button[0])

            # not Draw button
            window.blit(pygame.transform.scale(loaded_image.not_draw, (150,70)), self.not_draw_button[0])

        # exit button
        window.blit(pygame.transform.scale(loaded_image.exit, (150,70)), self.exit_button[0])

        # Host msg
        font_size = pygame.font.SysFont("arial",60)
        msg = font_size.render("Host", True, (0,0,0),(255,215,0))
        window.blit(pygame.transform.scale(msg, (100,40)), (350,175))
        
        # Player msg
        msg = font_size.render(" You ", True, (0,0,0),(255,215,0))
        window.blit(pygame.transform.scale(msg, (100,40)), (350,385))
        
        # result msg
        if self.game_state == 6 and self.result[3] > self.result[7]:
            msg = font_size.render("You Win", True, (0,0,0),(0,191,255))
            window.blit(pygame.transform.scale(msg, (160,80)), (320,260))
        elif self.game_state == 6 and self.result[3] < self.result[7]:
            msg = font_size.render("You Lose", True, (0,0,0),(0,191,255))
            window.blit(pygame.transform.scale(msg, (160,80)), (320,260))
        elif self.game_state == 6 and self.result[3] == self.result[7]:
            msg = font_size.render("  Draw  ", True, (0,0,0),(0,191,255))
            window.blit(pygame.transform.scale(msg, (160,80)), (320,260))

# Mechanic ======================= Mechanic


class Deck():
    def __init__(self, suffle=True):
        # data
        self.card = [spd_A(), spd_2(), spd_3(),spd_4(), spd_5(), spd_6(), spd_7(), spd_8(), spd_9(), spd_10(), spd_J(), spd_Q(), spd_K(),
                    hrt_A(), hrt_2(), hrt_3(),hrt_4(), hrt_5(), hrt_6(), hrt_7(), hrt_8(), hrt_9(), hrt_10(), hrt_J(), hrt_Q(), hrt_K(),
                    dmd_A(), dmd_2(), dmd_3(),dmd_4(), dmd_5(), dmd_6(), dmd_7(), dmd_8(), dmd_9(), dmd_10(), dmd_J(), dmd_Q(), dmd_K(),
                    cub_A(), cub_2(), cub_3(),cub_4(), cub_5(), cub_6(), cub_7(), cub_8(), cub_9(), cub_10(), cub_J(), cub_Q(), cub_K()]
        if suffle:
            self.shuffle()


    def shuffle(self): # สับ deck
        shuffle(self.card)
    
    def draw_out(self):
        if len(self.card) > 0:
            return self.card.pop(0)
        return None 


class Card():
    def __init__(self):
        self.image = None
        self.num = None
        self.suit = None
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
        self.num = 11
        self.suit = 4
        self.char = True

class spd_Q(Card):
    def __init__(self):
        self.image = loaded_image.spd_Q
        self.num = 12
        self.suit = 4
        self.char = True

class spd_K(Card):
    def __init__(self):
        self.image = loaded_image.spd_K
        self.num = 13
        self.suit = 4
        self.char = True

class hrt_A(Card):
    def __init__(self):
        self.image = loaded_image.hrt_A
        self.num = 1
        self.suit = 3
        self.char = True

class hrt_2(Card):
    def __init__(self):
        self.image = loaded_image.hrt_2
        self.num = 2
        self.suit = 3
        self.char = False

class hrt_3(Card):
    def __init__(self):
        self.image = loaded_image.hrt_3
        self.num = 3
        self.suit = 3
        self.char = False

class hrt_4(Card):
    def __init__(self):
        self.image = loaded_image.hrt_4
        self.num = 4
        self.suit = 3
        self.char = False

class hrt_5(Card):
    def __init__(self):
        self.image = loaded_image.hrt_5
        self.num = 5
        self.suit = 3
        self.char = False

class hrt_6(Card):
    def __init__(self):
        self.image = loaded_image.hrt_6
        self.num = 6
        self.suit = 3
        self.char = False

class hrt_7(Card):
    def __init__(self):
        self.image = loaded_image.hrt_7
        self.num = 7
        self.suit = 3
        self.char = False

class hrt_8(Card):
    def __init__(self):
        self.image = loaded_image.hrt_8
        self.num = 8
        self.suit = 3
        self.char = False

class hrt_9(Card):
    def __init__(self):
        self.image = loaded_image.hrt_9
        self.num = 9
        self.suit = 3
        self.char = False

class hrt_10(Card):
    def __init__(self):
        self.image = loaded_image.hrt_10
        self.num = 10
        self.suit = 3
        self.char = False

class hrt_J(Card):
    def __init__(self):
        self.image = loaded_image.hrt_J
        self.num = 11
        self.suit = 3
        self.char = True

class hrt_Q(Card):
    def __init__(self):
        self.image = loaded_image.hrt_Q
        self.num = 12
        self.suit = 3
        self.char = True

class hrt_K(Card):
    def __init__(self):
        self.image = loaded_image.hrt_K
        self.num = 13
        self.suit = 3
        self.char = True

class dmd_A(Card):
    def __init__(self):
        self.image = loaded_image.dmd_A
        self.num = 1
        self.suit = 2
        self.char = True

class dmd_2(Card):
    def __init__(self):
        self.image = loaded_image.dmd_2
        self.num = 2
        self.suit = 2
        self.char = False

class dmd_3(Card):
    def __init__(self):
        self.image = loaded_image.dmd_3
        self.num = 3
        self.suit = 2
        self.char = False

class dmd_4(Card):
    def __init__(self):
        self.image = loaded_image.dmd_4
        self.num = 4
        self.suit = 2
        self.char = False

class dmd_5(Card):
    def __init__(self):
        self.image = loaded_image.dmd_5
        self.num = 5
        self.suit = 2
        self.char = False

class dmd_6(Card):
    def __init__(self):
        self.image = loaded_image.dmd_6
        self.num = 6
        self.suit = 2
        self.char = False

class dmd_7(Card):
    def __init__(self):
        self.image = loaded_image.dmd_7
        self.num = 7
        self.suit = 2
        self.char = False

class dmd_8(Card):
    def __init__(self):
        self.image = loaded_image.dmd_8
        self.num = 8
        self.suit = 2
        self.char = False

class dmd_9(Card):
    def __init__(self):
        self.image = loaded_image.dmd_9
        self.num = 9
        self.suit = 2
        self.char = False

class dmd_10(Card):
    def __init__(self):
        self.image = loaded_image.dmd_10
        self.num = 10
        self.suit = 2
        self.char = False

class dmd_J(Card):
    def __init__(self):
        self.image = loaded_image.dmd_J
        self.num = 11
        self.suit = 2
        self.char = True

class dmd_Q(Card):
    def __init__(self):
        self.image = loaded_image.dmd_Q
        self.num = 12
        self.suit = 2
        self.char = True

class dmd_K(Card):
    def __init__(self):
        self.image = loaded_image.dmd_K
        self.num = 13
        self.suit = 2
        self.char = True

class cub_A(Card):
    def __init__(self):
        self.image = loaded_image.cub_A
        self.num = 1
        self.suit = 1
        self.char = True

class cub_2(Card):
    def __init__(self):
        self.image = loaded_image.cub_2
        self.num = 2
        self.suit = 1
        self.char = False

class cub_3(Card):
    def __init__(self):
        self.image = loaded_image.cub_3
        self.num = 3
        self.suit = 1
        self.char = False

class cub_4(Card):
    def __init__(self):
        self.image = loaded_image.cub_4
        self.num = 4
        self.suit = 1
        self.char = False

class cub_5(Card):
    def __init__(self):
        self.image = loaded_image.cub_5
        self.num = 5
        self.suit = 1
        self.char = False

class cub_6(Card):
    def __init__(self):
        self.image = loaded_image.cub_6
        self.num = 6
        self.suit = 1
        self.char = False

class cub_7(Card):
    def __init__(self):
        self.image = loaded_image.cub_7
        self.num = 7
        self.suit = 1
        self.char = False

class cub_8(Card):
    def __init__(self):
        self.image = loaded_image.cub_8
        self.num = 8
        self.suit = 1
        self.char = False

class cub_9(Card):
    def __init__(self):
        self.image = loaded_image.cub_9
        self.num = 9
        self.suit = 1
        self.char = False

class cub_10(Card):
    def __init__(self):
        self.image = loaded_image.cub_10
        self.num = 10
        self.suit = 1
        self.char = False

class cub_J(Card):
    def __init__(self):
        self.image = loaded_image.cub_J
        self.num = 11
        self.suit = 1
        self.char = True

class cub_Q(Card):
    def __init__(self):
        self.image = loaded_image.cub_Q
        self.num = 12
        self.suit = 1
        self.char = True

class cub_K(Card):
    def __init__(self):
        self.image = loaded_image.cub_K
        self.num = 13
        self.suit = 1
        self.char = True


class Player():
    def __init__(self, bot=False):
        self.hand_card = list()
        self.bot = bot
        self.num = 0
        self.result = 0
        self.deng2 = False
        self.deng3 = False
    
    def draw_result(self, pos, show): # also calculate and return result
        msg_resolution = (200,40)    
        left_top_pos = (pos[0]-(msg_resolution[0]/2),pos[1]-msg_resolution[1]/2)
        font_size = pygame.font.SysFont("arial",60)
        if self.is_pok9():
            if self.is_flood() or self.is_double():
                self.deng2 = True
                msg = font_size.render("Pok 9 Double", True, (0,0,0),(255,140,0))
            else:
                msg = font_size.render("    Pok 9    ", True, (0,0,0),(255,140,0))
            

        elif self.is_pok8():
            if self.is_flood() or self.is_double():
                self.deng2 = True
                msg = font_size.render("Pok 8 Double", True, (0,0,0),(255,140,0))
            else:
                msg = font_size.render("    Pok 8    ", True, (0,0,0),(255,140,0))

        elif self.is_tong():
            msg = font_size.render("Three of a kind "+str(self.get_point()), True, (0,0,0),(255,140,0))

        elif self.is_straight_flood():
            msg = font_size.render("Straight Flood "+str(self.hand_card[0].get_num())+str(self.hand_card[1].get_num())+str(self.hand_card[2].get_num()), True, (0,0,0),(255,140,0))
        elif self.is_close():
            msg = font_size.render("    Edge    ", True, (0,0,0),(255,140,0))
        else:
            self.result = self.get_point()
            msg_str = "   "+str(self.get_point())+" Points   "
            if (self.is_flood()  or self.is_double()) and self.num == 2 :
                self.deng2 = True
                msg_str = str(self.get_point())+" Points Double"
            elif self.is_flood() and self.num == 3:
                self.deng3 = True
                msg_str = str(self.get_point())+" Points Triple"
            msg = font_size.render(msg_str, True, (0,0,0),(255,140,0))
        
        if show or not self.bot:
            window.blit(pygame.transform.scale(msg, msg_resolution), left_top_pos)
        return self.result
            


    def draw_hand(self, pos, show):
        # pos = tuple : center of location to draw (x,y)
        # show = bool : true=show front card / false=show back card
        overlap_per_card = 20 # pixel
        card_resolution = (int(124*.8),int(180*.8))
        card_horizon = card_resolution[0]
        card_verical = card_resolution[1]
        full_horizon = card_horizon+((self.num-1)*overlap_per_card)    #card1 + 20 + 20 = full horizon pixel 
        full_verical = card_verical
        card_pos = (pos[0]-(full_horizon/2),pos[1]-full_verical/2)

        for card in self.hand_card:
            if show or not self.bot:
                # draw
                window.blit(pygame.transform.scale(card.get_image(), card_resolution), card_pos)
            else:
                window.blit(pygame.transform.scale(loaded_image.back_card, card_resolution), card_pos)
            # move right 
            card_pos = (card_pos[0]+overlap_per_card, card_pos[1])


    def draw_in(self, card):
        self.hand_card.append(card)
        self.hand_card.sort(key=lambda x: x.get_num())
        self.num += 1
    

    def clear_hand(self):
        self.hand_card = list()
        self.num = 0
    

    def get_point(self):
        # return int 
        point = 0
        for card in self.hand_card:
            if card.get_num() <= 10:
                point += (card.get_num()%10)

        if point >= 10:
            point %= 10
        return point


    def is_straight(self): # ไพ่เรียง? 
        # return true when 3 card are straight
        if self.num == 3:
            if self.hand_card[1].get_num()-self.hand_card[0].get_num() == 1:
                if self.hand_card[2].get_num()-self.hand_card[1].get_num() == 1:
                    return True
        return False


    def is_flood(self):
        # return true when 2-3 card are the same suit
        if self.num < 2:
            return False

        suit_list = self.get_suit()
        for i in range(0,self.num-1,1):
            if suit_list[i] != suit_list[i+1]:
                return False
        return True              


    def get_suit(self):
        # return list of suit
        suit = list()
        i=0
        for card in self.hand_card:
            suit.append(card.get_suit())
            i += 1
        return suit
    

    def get_num(self):
        # return list of num
        num = list()
        i=0
        for card in self.hand_card:
            num.append(card.get_num())
            i += 1
        return num


    def is_draw(self):
        if self.bot :
            if self.is_pok():
                draw_rate = 0
            else:
                draw_rate = (9-self.get_point())/9

            draw = bool(choice([True,False],p=[draw_rate, 1-draw_rate]))
            return draw
    
    def is_bot(self):
        return self.bot

    
    def is_pok(self):
        if self.num == 2 and self.get_point() >= 8:
            return True
        return False


    def is_pok9(self):
        if self.num == 2 and self.get_point() == 9:
            self.result = 99
            return True
        return False

    def is_pok8(self):
        if self.num == 2 and self.get_point() == 8:
            self.result = 88
            return True
        return False

    def is_tong(self):
        # return true when 3 card are the same number
        if self.num < 3:
            return False
        num_list = self.get_num()
        for i in range(0,self.num-1,1):
            if num_list[i] != num_list[i+1]:
                return False
        self.result = 30+self.hand_card[0].get_num()
        return True  
    
    def is_straight_flood(self):
        if self.is_straight() and self.is_flood():
            self.result = 10+self.hand_card[0].get_num()
            return True
        return False
    
    def is_close(self): # ขอบ
        if self.num == 3:
            if self.hand_card[0].is_char() and self.hand_card[1].is_char() and self.hand_card[2].is_char():
                if self.get_point() == 0:
                    self.result = 10
                    return True
        return False

    def is_double(self):
        if self.num == 2:
            num_list = self.get_num()
            for i in range(0,self.num-1,1):
                if num_list[i] != num_list[i+1]:
                    return False
            return True 

    
class Bot(Player):
    def __init__(self):
        super().__init__(True)


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
            #pygame.mixer.music.stop()
            menu.restart_pok()  # clear old game data before start new game
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
