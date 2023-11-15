import pygame

# Initialize the game
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("snake game")
#set the background 
background=pygame.image.load("green grass.png")
screen.blit(background,(0,0))
#set snake
test_surface = pygame.Surface((100,200))
test_surface.fill((128,0,128))
x_pos = 200
# Game loop
running = True                      
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x_pos+=1

    # Update game logic here

    # Render graphics here
    screen.blit(test_surface,(x_pos,250))
    pygame.display.update()
    
# Quit the game
pygame.quit()





