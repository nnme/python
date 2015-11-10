import pygame
import random

window = pygame.display.set_mode((400, 400))
pygame.display.set_caption('hello pygame')

screen = pygame.Surface((400, 400))

class Sprite:
    def __init__(self,xpos,ypos,filename):
        self.x=xpos
        self.y=ypos
        self.bitmap=pygame.image.load(filename)
        self.bitmap.set_colorkey((0,0,0))
    def render(self):
        screen.blit(self.bitmap,(self.x,self.y))


hero = Sprite(10, 10,'1.png')
s_hero = Sprite(320, 10, '151.gif')
hero.go_right = True
hero.go_down = True
s_hero.go_right = True
s_hero.go_down = True

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
    
    screen.fill((250,250,50))
    hero.render()
    s_hero.render()

#x x x x x x x x

    if hero.go_right == True:
        hero.x +=1
        if hero.x > 360:
            hero.go_right = False
    else:
        hero.x -=1
        if hero.x <0:
            hero.go_right = True

#down down down down   y y y y         

    if hero.go_down == True:
        hero.y +=1
        if hero.y > 360:
            hero.go_down = False
    else:
        hero.y -=1
        if hero.y <0:
            hero.go_down = True

#hero 2 
    if s_hero.go_right == True:
        s_hero.x +=1
        if s_hero.x > 360:
            s_hero.go_right = False
    else:
        s_hero.x -=1
        if s_hero.x <0:
            s_hero.go_right = True

#down down down down   y y y y         

    if s_hero.go_down == True:
        s_hero.y +=1
        if s_hero.y > 360:
            s_hero.go_down = False
    else:
        s_hero.y -=1
        if s_hero.y <0:
            s_hero.go_down = True

#square = pygame.Surface((40,40))
#square.fill((0,255,0))
# x = 0
# y = 0

# square_go_right = True
# square_go_down = True

# done = True
# while done:
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             done = False
    
#     screen.fill((250,250,50))
    
#     if square_go_right == True:
#         rand = random.randint(10,40)
#         x += rand
#         if x > 360:
#             square_go_right = False
#     else:
#         rand = random.randint(10,40)
#         x -= rand
#         if x < 0:
#             square_go_right = True

#     if square_go_down == True: 
#         rand = random.randint(10,40)
#         y += rand
#         if y > 360:
#             square_go_down = False
#     else:
#         rand = random.randint(10,40)
#         y -= rand
#         if y < 0:
#             square_go_down = True

#    screen.blit(square, (x, y))			
    window.blit(screen, (0,0))
    pygame.display.flip()
    pygame.time.delay(30)
