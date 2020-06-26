import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('First Game')

x = 50
y = 50
width = 40
height = 60
velocity = 5

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()


