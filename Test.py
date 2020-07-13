import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('First Game')

x = 50
y = 100
width = 40
height = 60
velocity = 10

IsJump = True
Jumpcount = 10

screenWidth = 500
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < screenWidth - width - velocity:
        x += velocity
    if not IsJump:
        if keys[pygame.K_UP] and y > velocity:
            y -= velocity
        if keys[pygame.K_DOWN] and y < screenWidth - height - velocity:
            y += velocity
        if keys[pygame.K_SPACE]:
            IsJump = True
    else:
        if Jumpcount >= -10:
            neg = 1
            if Jumpcount < 0:
                neg = -1
            y -= Jumpcount ** 2 * 0.5 * neg
            Jumpcount -= 1
        else:
            IsJump = False
            Jumpcount = 10

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()


