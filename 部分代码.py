# -*-coding:utf-8-*- s = '
#AoDaMiao Like Eating Fish
import sys, random, time, pygame
from pygame.locals import *

def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))
    

#main program begins
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("猫咪爱吃鱼！")
font1 = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 18)
font3 = pygame.font.Font(None, 34)
pygame.mouse.set_visible(False)
white = 255,255,255
red = 220, 50, 50
yellow = 230,230,50
black = 0,0,0
cat=pygame.image.load("aodamiao_2.png")
width,height=cat.get_size()
pic=pygame.transform.scale(cat,(width,height))
fish=pygame.image.load("fish.png")
width,height=fish.get_size()
fish=pygame.transform.smoothscale(fish,(width//3,height//3))
init=pygame.image.load("init.png")
lives = 10
score = 0
clock_start = 0
game_over = 1
mouse_x = mouse_y = 0
Round =1
mine=0
mine_png=pygame.image.load("mine.png")
cat2=pygame.image.load("aodamiao_3.png")
flag=0

pos_x = 300
pos_y = 410-40

bomb_x = random.randint(0,500)
mine_x=random.randint(0,500)
bomb_y = -50
vel_y = 0.4
vel_yy=0.6
mine_y=-100


