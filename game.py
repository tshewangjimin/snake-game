import pygame

# Initialize the game
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("snake game")
#set the background 
background=pygame.image.load("green grass.png")
screen.blit(background,(0,0))
# Game loop
running = True                      
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic here

    # Render graphics here

    pygame.display.update()

# Quit the game
pygame.quit()



