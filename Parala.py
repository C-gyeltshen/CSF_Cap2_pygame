# importing pygame 
import pygame 
from sys import exit

#initializing pygame 
pygame.init()
#setting the pygame display 
screen_display = pygame.display.set_mode((800,500))  # ((width,hight))
# Assigning the game name 
pygame.display.set_caption("Parala game")
# Creating a clock objest to control the Time and fram rate 
clock = pygame.time.Clock()
test_font = pygame.font.Font(None,50)

score_surface = test_font.render("Welcome to the game ","/Users/chimigyeltshen/Desktop/practice/PyGame/pixeltype/pixeltype.ttf" ,"Black")
score_rect = score_surface.get_rect(center = (400,50))

snail_surface = pygame.image.load("/Users/chimigyeltshen/Desktop/practice/PyGame/tools/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))


player_surface = pygame.image.load("/Users/chimigyeltshen/Desktop/practice/PyGame/tools/player_walk_1.png").convert_alpha()
player_rec = player_surface.get_rect(midbottom =(80,300)) # position of the rectangle 

background = pygame.image.load("/Users/chimigyeltshen/Desktop/practice/PyGame/tools/mountain.png").convert_alpha()
ground = pygame.image.load("/Users/chimigyeltshen/Desktop/practice/PyGame/tools/ground.png").convert_alpha()


while True:
    # finding all the possible user input 
    for event in pygame.event.get():
        # If the user input is quit then quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen_display.blit(background,(0,0))
    screen_display.blit(ground,(0,300))

    # rectangle arround the scoor text
    pygame.draw.rect(screen_display,"white",score_rect)
    screen_display.blit(score_surface,score_rect)

    snail_rect.x -= 4
    if snail_rect.right<= 0:
        snail_rect.left =800
    screen_display.blit(snail_surface,snail_rect)
    
    screen_display.blit(player_surface,player_rec)

    # Using while loop to update the display continuesly 
    pygame.display.update()
    # Calling the time object  
    clock.tick(60)  # The game will be runing with 60 frams per second

