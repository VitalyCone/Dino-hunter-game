import pygame
import random

pygame.init()


"""Дисплей"""

screen = pygame.display.set_mode((1280,800))
pygame.display.set_caption("Dino Hunter")

"""Загрузка"""

icon = pygame.image.load("game_data/happy.png").convert_alpha()
download_bg = pygame.image.load("game_data/fon.png").convert_alpha()
download_bg_stone = pygame.image.load("game_data/fon_stone.png").convert_alpha()
bullet_r = pygame.image.load("game_data/bullet_r.png").convert_alpha()
bullet_l = pygame.image.load("game_data/bullet_l.png").convert_alpha()
dino_kill_logo = pygame.image.load("game_data/dinosaur.png").convert_alpha()
myfont = pygame.font.Font("game_data/PressStart2P-Regular.ttf", 40)
totalfont = pygame.font.Font("game_data/PressStart2P-Regular.ttf", 40)
restart_bot = [
            pygame.image.load("game_data/game_over/restart/white.png").convert_alpha(),
            pygame.image.load("game_data/game_over/restart/black.png").convert_alpha()
            ]
quit_bot = [
            pygame.image.load("game_data/game_over/quit/white.png").convert_alpha(),
            pygame.image.load("game_data/game_over/quit/black.png").convert_alpha()
            ]
play_bot = [
            pygame.image.load("game_data/menu/play/white.png").convert_alpha(),
            pygame.image.load("game_data/menu/play/black.png").convert_alpha()
            ]
menu_screen = [
                pygame.image.load("game_data/menu/dh_anim/1.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/2.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/3.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/4.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/4.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/1.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/2.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/3.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/4.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/4.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/1.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/5.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/6.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/7.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/8.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/9.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/9.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/9.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/8.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/7.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/6.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/5.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/1.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/5.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/6.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/7.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/8.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/10.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/11.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/12.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/13.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/13.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/13.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/13.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/13.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/12.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/11.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/10.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/8.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/7.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/6.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/5.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/1.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/1.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/1.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/14.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/15.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/16.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/17.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/18.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/19.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/20.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/21.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/22.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/23.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/23.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/23.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/23.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/23.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/24.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/25.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/26.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/27.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/28.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/29.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/29.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/29.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/29.png").convert_alpha(),
                pygame.image.load("game_data/menu/dh_anim/30.png").convert_alpha(),
                ]
game_over_screen = [
                    pygame.image.load("game_data/game_over/game_over_anim/1.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/2.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/1.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/2.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/3.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/2.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/1.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/2.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/3.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/4.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/5.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/5.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/6.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/5.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/4.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/3.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/2.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/1.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/2.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/3.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/4.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/5.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/6.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/7.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/8.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/9.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/10.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/10.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/10.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/10.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/11.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/12.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/13.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/14.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/15.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/16.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/17.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/18.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/19.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/18.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/20.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/21.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/22.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/23.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/24.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/25.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/26.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/27.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/28.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/29.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/30.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/31.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/32.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/33.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/34.png").convert_alpha(),
                    pygame.image.load("game_data/game_over/game_over_anim/35.png").convert_alpha(),
                    ]
player_stay_left = [
                    pygame.image.load("game_data/player_set/player_stay_left/1.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_left/1.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_left/11.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_left/11.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_left/2.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_left/21.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_left/21.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_left/3.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_left/31.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_left/31.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_left/4.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_left/41.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_left/41.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_left/5.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_left/51.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_left/51.png").convert_alpha(),
                    ]
player_stay_right = [
                    pygame.image.load("game_data/player_set/player_stay_right/1.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_right/11.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_right/11.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_right/2.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_right/21.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_right/21.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_right/3.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_right/31.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_right/31.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_right/4.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_right/41.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_right/41.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_right/5.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_right/51.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_stay_right/51.png").convert_alpha(),
                    ]
player_move_right = [
                    pygame.image.load("game_data/player_set/player_move_right/1.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_right/11.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_right/2.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_right/21.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_right/3.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_right/31.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_right/4.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_right/41.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_right/5.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_right/51.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_right/6.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_right/61.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_right/7.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_right/71.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_right/8.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_right/81.png").convert_alpha(),
                    ]
player_move_left = [
                    pygame.image.load("game_data/player_set/player_move_left/1.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_left/11.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_left/2.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_left/21.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_left/3.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_left/31.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_left/4.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_left/41.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_left/5.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_left/51.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_left/6.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_left/61.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_left/7.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_left/71.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_left/8.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_move_left/81.png").convert_alpha(),
                    ]

player_shoot_left = [
                    pygame.image.load("game_data/player_set/player_shoot_left/1.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_shoot_left/1.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_shoot_left/2.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_shoot_left/2.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_shoot_left/3.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_shoot_left/3.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_shoot_left/4.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_shoot_left/4.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_shoot_left/5.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_shoot_left/5.png").convert_alpha(),
                    ]
player_shoot_right = [
                    pygame.image.load("game_data/player_set/player_shoot_right/1.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_shoot_right/1.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_shoot_right/2.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_shoot_right/2.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_shoot_right/3.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_shoot_right/3.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_shoot_right/4.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_shoot_right/4.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_shoot_right/5.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_shoot_right/5.png").convert_alpha(),
                    ]
player_die_left = [
                    pygame.image.load("game_data/player_set/player_die_left/1.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/1.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/2.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/2.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/3.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/3.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/4.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/4.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/5.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/5.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/6.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/6.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/7.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/7.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/8.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/8.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/8.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/8.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/8.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/8.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/8.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/8.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/8.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_left/8.png").convert_alpha()
                    
                    ]
player_die_right = [
                    pygame.image.load("game_data/player_set/player_die_right/1.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_right/1.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_right/2.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_right/2.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_right/3.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_right/3.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_right/4.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_right/4.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_right/5.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_right/5.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_right/6.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_right/6.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_right/7.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_right/7.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_right/8.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_right/8.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_right/8.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_right/8.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_right/8.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_right/8.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_right/8.png").convert_alpha(),
                    pygame.image.load("game_data/player_set/player_die_right/8.png").convert_alpha()
                    ]
dino_move_left = [
                pygame.image.load("game_data/player_set/dino_move_left/1.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_left/1.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_left/2.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_left/2.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_left/3.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_left/3.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_left/4.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_left/4.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_left/5.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_left/5.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_left/6.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_left/6.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_left/7.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_left/7.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_left/8.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_left/8.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_left/9.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_left/9.png").convert_alpha(),
                ]
dino_move_right = [
                pygame.image.load("game_data/player_set/dino_move_right/1.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_right/1.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_right/2.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_right/2.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_right/3.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_right/3.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_right/4.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_right/4.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_right/5.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_right/5.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_right/6.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_right/6.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_right/7.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_right/7.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_right/8.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_right/8.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_right/9.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_move_right/9.png").convert_alpha(),
                ]
dino_die_right = [
                pygame.image.load("game_data/player_set/dino_die_right/1.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_die_right/1.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_die_right/2.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_die_right/2.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_die_right/3.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_die_right/3.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_die_right/4.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_die_right/4.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_die_right/5.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_die_right/5.png").convert_alpha(),
                ]
dino_die_left = [
                pygame.image.load("game_data/player_set/dino_die_left/1.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_die_left/1.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_die_left/2.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_die_left/2.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_die_left/3.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_die_left/3.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_die_left/4.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_die_left/4.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_die_left/5.png").convert_alpha(),
                pygame.image.load("game_data/player_set/dino_die_left/5.png").convert_alpha(),
                ]

"""Настройки персонажей"""

kills = 0
moving_player_l = 0
moving_player_r = 0
moving_player_l_for_ws = 0
moving_player_r_for_ws = 0
staing_player_l = 0
staing_player_r = 0
shooting_l = 0
shooting_r = 0
anim_shoot_l = False
anim_shoot_r = False
player_die_anim_l = 0
player_die_anim_r = 0
player_die_list_l = []
player_die_list_r = []
player_x = 640
player_y = 600
dying_l = False
dying_r = False
bullet_move_l = False
bullet_move_r = False
bullet_speed_l = 0
bullet_speed_r = 0
bullets_r = []
bullets_l = []
anim_l = False
anim_r = False
keys = {
    pygame.K_a : False,
    pygame.K_d : False,
    pygame.K_s : False,
    pygame.K_w : False,
    pygame.K_e : False,
    pygame.K_q : False,
    }
dino_coord_x1 = -50
dino_coord_x2 = 1285
dino_coord_y1 = 500
dino_coord_y2 = 550
dino_coord_y3 = 600
dino_coord_y4 = 650
dino_coord_y5 = 700
dino_spawn = False
dino_spawn_l = False
dino_spawn_r = False
dino_anim_l = 0
dino_anim_r = 0
dino_die_anim_l = 0
dino_die_anim_r = 0
dino_die_list_l = []
dino_die_list_r = []

"""Настройки игры"""

def spawn_side(l,r):
    sides = [l,r]
    random_num = random.randrange(sides[0], sides[-1]+1)
    return sides[random_num]

def spawn_coord():
    coordinates_l = [(-50, 700),(-50, 650),(-50, 600),(-50, 550),(-50, 500)]
    coordinates_r = [(1230, 700),(1230, 650),(1230, 600),(1230, 550),(1230, 500)]
    num = [0,1,2,3,4]
    side = spawn_side(0,1)
    if side == 0:
        random_num = random.randrange(num[0], num[-1]+1)
        return coordinates_l[random_num]
    else:
        random_num = random.randrange(num[0], num[-1]+1)
        return coordinates_r[random_num]

restart_bot_rect = restart_bot[0].get_rect(topleft = (314,300))
quit_bot_rect = quit_bot[0].get_rect(topleft = (1003,702))
play_bot_rect = play_bot[0].get_rect(topleft = (326,308))
game_over_anim = 0
menu_anim = 0
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
bg = download_bg
bg_with_stone = download_bg_stone
stage_num = 1
last_key = [None]
game_run = True
staing = True
timer_stage_1 = 4000
timer_stage_2 = 2000
timer_stage_3 = 1000
timer_stage_4 = 600
timer_stage_5 = 300
timer_stage_6 = 180
timer_stage_7 = 100
dino_timer1 = pygame.USEREVENT+1
dino_in_game_l = []
dino_in_game_r = []
main_dino_spawn_1 = -50
main_dino_spawn_2 = 1230
#c_x = 1230
game_menu = True
game_play = False
restart_rect = pygame.Rect(314,300,653,112)
play_rect = pygame.Rect(314,300,1255,369)
invisible_color = (0,0,0,0)#

"""Игра"""

while game_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
            quit()
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_e or event.key == pygame.K_q) and anim_shoot_l == False and anim_shoot_r == False:
            if event.key == pygame.K_e:
                bullets_r.append(bullet_r.get_rect(topleft = (player_x+50,player_y+15)))
                anim_shoot_r = True
            if event.key == pygame.K_q:
                bullets_l.append(bullet_l.get_rect(topleft = (player_x-50,player_y+15)))
                anim_shoot_l = True

        elif event.type == pygame.KEYDOWN:
            if event.key in keys:
                keys[event.key] = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_c:
                dino_spawn = True
            if event.key in keys:
                keys[event.key] = False

        if event.type == dino_timer1:
            if kills>5 and kills <=10:
                pygame.time.set_timer(dino_timer1, timer_stage_2)
            if kills>10 and kills <=50:
                pygame.time.set_timer(dino_timer1, timer_stage_3)
            if kills>50 and kills <=100:
                pygame.time.set_timer(dino_timer1, timer_stage_4)
            if kills>100:
                pygame.time.set_timer(dino_timer1, timer_stage_5)
            if kills>200:
                pygame.time.set_timer(dino_timer1, timer_stage_6)
            if kills>300:
                pygame.time.set_timer(dino_timer1, timer_stage_7)
            coordinates = spawn_coord()
            c_x = coordinates[0]
            c_y = coordinates[1]
            if c_x == -50:
                dino_in_game_l.append(dino_move_right[0].get_rect(topleft=(c_x, c_y)))
            if c_x == 1230:
                dino_in_game_r.append(dino_move_left[0].get_rect(topleft=(c_x, c_y)))


    if game_menu:
        mouse1 = pygame.mouse.get_pos()
        screen.blit(menu_screen[menu_anim], (0,0))
        if menu_anim != 68:
            menu_anim+=1
        elif menu_anim == 68:
            screen.blit(play_bot[0], (326,308))
            if play_bot_rect.collidepoint(mouse1):
                screen.blit(play_bot[1], (326,308))
                if pygame.mouse.get_pressed()[0]:
                    pygame.time.set_timer(dino_timer1, timer_stage_1)
                    game_play = True
                    game_menu = False


    if game_play:
        screen.blit(bg, (0,0))
        screen.blit(dino_kill_logo, (5,5))
        kills_on_screen = myfont.render(f"= {kills}" , True, (0, 0, 0))
        screen.blit(kills_on_screen, (225,70))
        stage_on_screen = myfont.render(f"STAGE: {stage_num}" , True, (0, 0, 0))
        screen.blit(stage_on_screen, (20,200))
        player_rect = player_move_left[0].get_rect(topleft = (player_x, player_y))

        if kills == 5:
            stage_num=2
        if kills == 10:
            stage_num=3
        if kills == 50:
            stage_num=4
        if kills == 100:
            stage_num=5
        if kills == 200:
            stage_num=6
        if kills == 300:
            stage_num=7

        staing = True
        if anim_shoot_l == True and dying_l == False and dying_r == False:
            staing = False
            screen.blit(player_shoot_left[shooting_l], (player_x-30, player_y)) 
            shooting_l+=1
            if shooting_l == 10:
                shooting_l = 0
                anim_shoot_l = False
        if anim_shoot_r == True and dying_l == False and dying_r == False:
            if anim_shoot_l == False:
                staing = False
                screen.blit(player_shoot_right[shooting_r], (player_x, player_y)) 
                shooting_r+=1
                if shooting_r == 10:
                    shooting_r = 0
                    anim_shoot_r = False
        
        if dino_in_game_r:
            for i,el in enumerate(dino_in_game_r):
                screen.blit(dino_move_left[dino_anim_l], (el.x, el.y))
                #dino_anim_l+=1
                el.x-=2
                if player_rect.colliderect(el):
                    dying_r = True
        if dino_in_game_l:
            for i,el in enumerate(dino_in_game_l):
                screen.blit(dino_move_right[dino_anim_r], (el.x, el.y))
                el.x+=2
                if player_rect.colliderect(el):   
                    dying_l = True

        if dying_l == True:
            anim_shoot_r == False
            anim_shoot_l == False
            staing = False
            clock.tick(10)
            screen.blit(player_die_left[player_die_anim_l],(player_x, player_y))
            player_die_anim_l+=1
            if player_die_anim_l == 22:
                player_die_anim_l = 0
                game_play = False
        if dying_r == True:
            anim_shoot_r == False
            anim_shoot_l == False
            staing = False
            clock.tick(10)
            screen.blit(player_die_right[player_die_anim_r],(player_x, player_y))
            player_die_anim_r+=1
            if player_die_anim_r == 22:
                player_die_anim_r = 0
                game_play = False

        if keys[pygame.K_a] == True and keys[pygame.K_s] == True and keys[pygame.K_d] == True and keys[pygame.K_w] == True and dying_l == False and dying_r == False:
            if last_key[0] == 'a':
                screen.blit(player_stay_left[staing_player_l], (player_x,player_y))
                staing_player_l+=1
            if last_key[0] == 'd':
                screen.blit(player_stay_right[staing_player_r], (player_x,player_y))
                staing_player_r+=1
            if not(last_key[0] == 'd') and not(last_key[0] == 'a'):
                screen.blit(player_stay_left[staing_player_l], (player_x,player_y))
                staing_player_l+=1
            pass

        if keys[pygame.K_a] == True and keys[pygame.K_s] == True and keys[pygame.K_d] == True and keys[pygame.K_w] == False and dying_l == False and dying_r == False:
            staing = False
            if last_key[0] == 'a':
                    screen.blit(player_move_left[moving_player_l], (player_x, player_y))
                    moving_player_l+=1
            elif last_key[0] == 'd':
                    screen.blit(player_move_right[moving_player_r], (player_x, player_y))
                    moving_player_r+=1
            else:
                    screen.blit(player_move_left[moving_player_l], (player_x, player_y))
                    moving_player_l+=1
            pass

        if keys[pygame.K_a] == True and keys[pygame.K_s] == False and keys[pygame.K_d] == True and keys[pygame.K_w] == True and dying_l == False and dying_r == False:
            staing = False
            if last_key[0] == 'a':
                    screen.blit(player_move_left[moving_player_l], (player_x, player_y))
                    moving_player_l+=1
            elif last_key[0] == 'd':
                    screen.blit(player_move_right[moving_player_r], (player_x, player_y))
                    moving_player_r+=1
            else:
                    screen.blit(player_move_left[moving_player_l], (player_x, player_y))
                    moving_player_l+=1
            pass

        if keys[pygame.K_a] == True and dying_l == False and dying_r == False:
            if anim_shoot_l == False and anim_shoot_r == False:
                staing = False
                if keys[pygame.K_d] == False:
                    screen.blit(player_move_left[moving_player_l], (player_x, player_y))
                    moving_player_l+=1
                    last_key = ['a']
                else:
                    staing = True
                speed_x = 3
                if player_x < 0:
                    speed_x = 0
                player_x-=speed_x

        if keys[pygame.K_d] == True and dying_l == False and dying_r == False:
            if anim_shoot_l == False and anim_shoot_r == False:
                staing = False
                if keys[pygame.K_a] == False:
                    screen.blit(player_move_right[moving_player_r], (player_x, player_y))
                    moving_player_r+=1
                    last_key = ['d']
                else:
                    staing = True
                speed_x = 3
                if player_x > 1235:
                    speed_x = 0
                player_x+=speed_x
        
        if keys[pygame.K_s] == True and dying_l == False and dying_r == False:
            if anim_shoot_l == False and anim_shoot_r == False:
                staing = False
                if keys[pygame.K_w] == False and keys[pygame.K_a] == False and keys[pygame.K_d] == False:
                    if last_key[0] == 'a':
                        screen.blit(player_move_left[moving_player_l], (player_x, player_y))
                        moving_player_l+=1
                    elif last_key[0] == 'd':
                        screen.blit(player_move_right[moving_player_r], (player_x, player_y))
                        moving_player_r+=1
                    else:
                        screen.blit(player_move_left[moving_player_l], (player_x, player_y))
                        moving_player_l+=1
                elif keys[pygame.K_w] == True and keys[pygame.K_a] == False and keys[pygame.K_d] == False:
                    if last_key[0] == 'a':
                        screen.blit(player_move_left[moving_player_l], (player_x, player_y))
                        moving_player_l+=1
                    elif last_key[0] == 'd':
                        screen.blit(player_move_right[moving_player_r], (player_x, player_y))
                        moving_player_r+=1
                    else:
                        screen.blit(player_move_left[moving_player_l], (player_x, player_y))
                        moving_player_l+=1
                speed_y = 3
                if player_y > 735:
                    speed_y = 0
                player_y+=speed_y

        if keys[pygame.K_w] == True and dying_l == False and dying_r == False:
            if anim_shoot_l == False and anim_shoot_r == False:
                staing = False
                speed_y = 3
                if keys[pygame.K_s] == False and keys[pygame.K_a] == False and keys[pygame.K_d] == False:
                    if last_key[0] == 'a':
                        screen.blit(player_move_left[moving_player_l], (player_x, player_y))
                        moving_player_l+=1
                    elif last_key[0] == 'd':
                        screen.blit(player_move_right[moving_player_r], (player_x, player_y))
                        moving_player_r+=1
                    else:
                        screen.blit(player_move_left[moving_player_l], (player_x, player_y))
                        moving_player_l+=1
                if player_y < 500:
                    speed_y = 0
                player_y-= speed_y

        if staing and dying_l == False and dying_r == False:
            if last_key[0] == 'a':
                screen.blit(player_stay_left[staing_player_l], (player_x,player_y))
                staing_player_l+=1
            elif last_key[0] == 'd':
                screen.blit(player_stay_right[staing_player_r], (player_x,player_y))
                staing_player_r+=1
            else:
                screen.blit(player_stay_left[staing_player_l], (player_x,player_y))
                staing_player_l+=1
        
        if bullets_r and dying_l == False and dying_r == False:
            for i, el in enumerate(bullets_r):
                screen.blit(bullet_r, (el.x, el.y))
                el.x+=10
                if dino_in_game_l:
                    for (index, dev) in enumerate(dino_in_game_l):
                        if el.colliderect(dev):
                            kills+=1
                            dino_die_list_l.append(dino_die_right[0].get_rect(topleft = (dev.x,dev.y)))
                            dino_in_game_l.pop(index)
                            bullets_r.pop(i)
                if dino_in_game_r:
                    for (index, dev) in enumerate(dino_in_game_r):
                        if el.colliderect(dev):
                            kills+=1
                            dino_die_list_r.append(dino_die_left[0].get_rect(topleft = (dev.x,dev.y)))
                            dino_in_game_r.pop(index)
                            bullets_r.pop(i)
                if el.x>1300:
                    bullets_r.pop(i)
        if bullets_l and dying_l == False and dying_r == False:
            for i, el in enumerate(bullets_l):
                screen.blit(bullet_l, (el.x, el.y))
                el.x-=10
                if dino_in_game_l:
                    for (index, dev) in enumerate(dino_in_game_l):
                        if el.colliderect(dev):
                            kills+=1
                            dino_die_list_l.append(dino_die_right[0].get_rect(topleft = (dev.x,dev.y)))
                            bullets_l.pop(i)
                            dino_in_game_l.pop(index)       
                if dino_in_game_r:
                    for (index, dev) in enumerate(dino_in_game_r):
                        if el.colliderect(dev):
                            kills+=1
                            dino_die_list_r.append(dino_die_left[0].get_rect(topleft = (dev.x,dev.y)))
                            dino_in_game_r.pop(index)
                            bullets_l.pop(i)
                if el.x<-20:
                    bullets_l.pop(i)

        if dino_die_list_l and dying_l == False and dying_r == False:
            for i,el in enumerate(dino_die_list_l):
                screen.blit(dino_die_right[dino_die_anim_r], (el.x, el.y))
                dino_die_anim_r+=1
                if dino_die_anim_r == 10:
                    dino_die_anim_r = 0
                    dino_die_list_l.pop(i)
        if dino_die_list_r and dying_l == False and dying_r == False:
            for i,el in enumerate(dino_die_list_r):
                screen.blit(dino_die_left[dino_die_anim_l], (el.x, el.y))
                dino_die_anim_l+=1
                if dino_die_anim_l == 10:
                    dino_die_anim_l = 0
                    dino_die_list_r.pop(i)
                    
        dino_anim_l+=1
        if dino_anim_l == 18:
            dino_anim_l = 0
        dino_anim_r+=1
        if dino_anim_r == 18:
            dino_anim_r = 0
        if moving_player_l == 16:
            moving_player_l = 0
        if moving_player_r == 16:
            moving_player_r = 0
        if staing_player_l == 15:
            staing_player_l = 0
        if staing_player_r == 15:
            staing_player_r = 0
        screen.blit(bg_with_stone, (0,0))


    elif game_play == False and game_menu == False:
        mouse = pygame.mouse.get_pos()
        total_score = totalfont.render(f"{kills}" , True, (255, 255, 255))
        screen.blit(game_over_screen[game_over_anim], (0,0))

        if game_over_anim != 55:
            game_over_anim+=1

        elif game_over_anim == 55:
            screen.blit(restart_bot[0], (314,300))
            screen.blit(quit_bot[0], (1003,702))
            screen.blit(total_score, (550,706))

            if restart_bot_rect.collidepoint(mouse):
                screen.blit(restart_bot[1], (314,300))
                if pygame.mouse.get_pressed()[0]:
                    player_die_list_l.clear()
                    player_die_list_l.clear()
                    dino_die_list_l.clear()
                    dino_die_list_l.clear()
                    bullets_l.clear()
                    bullets_l.clear()
                    kills = 0
                    game_over_anim = 0
                    dino_in_game_l.clear()
                    dino_in_game_r.clear()
                    dying_l = False
                    dying_r = False
                    stage_num = 0
                    pygame.time.set_timer(dino_timer1, timer_stage_1)
                    game_play = True

            if quit_bot_rect.collidepoint(mouse):
                screen.blit(quit_bot[1], (1003,702))
                if pygame.mouse.get_pressed()[0]:
                    game_run = False
                    quit()


    pygame.display.update()
    if dying_l == False and dying_r == False and game_play == True:
        clock.tick(60)
    if game_play == False:
        clock.tick(60)
