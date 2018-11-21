import pygame
from Hero import Hero

# Always needs to be initialized
pygame.init()

screen_size = (800,600)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Robin Hood")

# Variables
background_image = pygame.image.load('back.png')
hero_image = pygame.image.load('crymin.png')
goblin_image = pygame.image.load('vamp.png')
monster_image = pygame.image.load('criminal.png')
arrow_image = pygame.image.load('arrow.png')

hero = Hero()
# Main Game

game_on = True
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 276: #LEFT
                hero.go_move("left")
            elif event.key == 275: #RIGHT
                hero.go_move("right")
            if event.key == 273: #DOWN
                hero.go_move("down")
            elif event.key == 274: #UP
                hero.go_move("up")
            if event.key == 32:
                print("Hey dog!")

    screen.blit(background_image,[0,0])
    screen.blit(hero_image,[hero.x, hero.y])
    screen.blit(goblin_image,[100,224])
    screen.blit(monster_image, [611,100])
    pygame.display.flip()