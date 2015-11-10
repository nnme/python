import pygame
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption('hello pygame')

screen = pygame.Surface((400, 400))

square = pygame.Surface((40,40))
square.fill((0,255,0))
x = 0
y = 0
square_go_right = True
square_go_down = True

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
    
    screen.fill((250,250,50))
    
    if square_go_right == True:
        x += 5
        if x > 360:
            square_go_right = False
    else:
        x -= 4
        if x < 0:
            square_go_right = True

    if square_go_down == True:
        y += 7
        if y > 360:
            square_go_down = False
    else:
        y -= 5
        if y < 0:
            square_go_down = True

    screen.blit(square, (x, y))			
    window.blit(screen, (0,0))
    pygame.display.flip()
    pygame.time.delay(30)
