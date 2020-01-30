import random
import pygame

screen = pygame.display.set_mode((720, 480))


image = pygame.Surface((32, 32))
image_bullet = pygame.Surface((20, 3))
bullet_x=0
bullet_y=0
x=10
y=10
running=True
timec=0
while running:
    screen.fill((100,100,100))  # Fill the screen with background color.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
              y=y-20
            elif event.key == pygame.K_s:
              y=y+20
            elif event.key == pygame.K_a:
              x=x-20
            elif event.key == pygame.K_d:
              x=x+20
            elif event.key == pygame.K_b:
              bullet_x= random.randint(0,100)
              bullet_y = random.randint(0,200)  
    
    timec+=1
    timed=int(timec)
    print(timed)
    screen.blit(image, (x,y,50,50))
    screen.blit(image_bullet,(bullet_x,bullet_y,5,5))
    bullet_x=bullet_x+.01
    

    pygame.display.flip()  # Or pygame.display.update(), but we need to update the screen

#quit()  # Not actually necessary since the script will exit anyway.