import pygame
from Hero import Hero
from Arrow import Arrow
from BadGuy import BadGuy
from pygame.sprite import Group, groupcollide

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
bad_guy = BadGuy()
bad_guys = Group()
bad_guys.add(bad_guy)
arrows = Group()

pygame.mixer.music.load('bleepsgalore.mp3')
pygame.mixer.music.play(-1)

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
            if event.key == 32: #SPACEBAR
                new_arrow = Arrow(hero)
                arrows.add(new_arrow)
        elif event.type == pygame.KEYUP:
            if event.key == 276: #LEFT
                hero.go_move("left", False)
            elif event.key == 275: #RIGHT
                hero.go_move("right", False)
            if event.key == 273: #DOWN
                hero.go_move("down", False)
            elif event.key == 274: #UP
                hero.go_move("up", False)

    screen.blit(background_image,[0,0])
    hero.draw_me()
    bad_guy.update_me(hero)

    for arrow in arrows:
        arrow.update_me()
        screen.blit(arrow_image,[arrow.x,arrow.y])

    arrow_hit = groupcollide(arrows,bad_guys,True,True)

    for bad_guy in bad_guys:
        bad_guy.update_me(hero)
        screen.blit(monster_image,[bad_guy.x,bad_guy.y])

    screen.blit(hero_image,[hero.x, hero.y])
    screen.blit(goblin_image,[100,224])
    pygame.display.flip()