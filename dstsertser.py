import pygame
from pygame.locals import *
from random import randrange

def load_level(level_number):
    """ Charge un niveau.
    Prend un entier en paramètre.
    Retourne un array de 15 sur 15. """
    filename = "Niveaux/Niveau_%d.txt"
    file = open(filename % level_number, "r")
    if file.mode == 'r':
        content = file.read()
        level_data = []
        for line in range(15):
            line_data = []
            for column in range(15):
                line_data.append(content[line*16+column])
                if content[line*16+column] != 'a' and content[line*16+column] !=  '0' and content[line*16+column] != 'd' and content[line*16+column] !='m':
                    print(content, "is invalid")
                    return None
            level_data.append(line_data)
        return level_data

def load_textures():
    """ Charge toutes les textures et les renvoie en tuple. """
    mur = pygame.image.load("Images/Mur.png").convert_alpha()
    fond = pygame.image.load("Images/Fond.jpg").convert_alpha()
    end = pygame.image.load("Images/Arrivee.png").convert_alpha()
    start = pygame.image.load("Images/Depart.png").convert_alpha()
    dk_down = pygame.image.load("Images/DK_bas.png").convert_alpha()
    dk_up = pygame.image.load("Images/DK_haut.png").convert_alpha()
    dk_left = pygame.image.load("Images/DK_droite.png").convert_alpha()
    dk_right = pygame.image.load("Images/DK_gauche.png").convert_alpha()
    accueil = pygame.image.load("Images/Selection.jpg").convert_alpha()
    niv0 = pygame.image.load("Images/Niv0.jpg").convert_alpha()
    niv1 = pygame.image.load("Images/Niv1.jpg").convert_alpha()
    niv2 = pygame.image.load("Images/Niv2.jpg").convert_alpha()
    niv3 = pygame.image.load("Images/Niv3.jpg").convert_alpha()
    w, h = pygame.display.get_surface().get_size()
    fond = pygame.transform.scale(fond, (w,h))
    accueil = pygame.transform.scale(accueil, (w,h))
    return (mur, fond, end, start, dk_down, dk_up, dk_left, dk_right, accueil, niv0, niv1, niv2, niv3)


def display_level(level, textures, window):
    """ Affiche un niveau sans actualiser. Prend les textures, la fenêtre et le niveau en paramètre. """

    for line in range(15):
        for column in range(15):
            if level[line][column] == 'm':
                window.blit(textures[0], (column*30,line*30))
            elif level[line][column] == 'd':
                window.blit(textures[3], (column*30,line*30))
            elif level[line][column] == 'a':
                window.blit(textures[2], (column*30,line*30))


pygame.init()
window = pygame.display.set_mode((450, 450))

menu = True
level_number = 2
level = load_level(level_number)
textures = load_textures()
dk_texture = textures[4]

x = 0
y = 0

continuer = 1
while continuer:
    if menu == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x-1 >= 0 and level[y][x-1] != 'm':
                        x -= 1
                        dk_texture = textures[7]
                elif event.key == pygame.K_RIGHT:
                    if x+1 < 15 and level[y][x+1] != 'm':
                        x += 1
                        dk_texture = textures[6]
                elif event.key == pygame.K_UP:
                    if y-1 >= 0 and level[y-1][x] != 'm':
                        y -= 1
                        dk_texture = textures[5]
                elif event.key == pygame.K_DOWN:
                    if y+1 < 15 and level[y+1][x] != 'm':
                        y += 1
                        dk_texture = textures[4]

        if level[y][x] == 'a':
            menu = True

        window.blit(textures[4], (x * 30, y * 30))
        window.blit(textures[1], (0, 0))
        display_level(level, textures, window)
        window.blit(dk_texture, (x * 30, y * 30))
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = 0

        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            ok = False
            if x < 200 and x > 50:
                if y < 200 and y > 50:
                    level_number = 0
                    level = load_level(level_number)
                    ok = True
                elif y < 400 and y > 250:
                    level_number = 2
                    level = load_level(level_number)
                    ok = True
            elif x < 400 and x > 250:
                if y < 200 and y > 50:
                    level_number = 1
                    level = load_level(level_number)
                    ok = True
                elif y < 400 and y > 250:
                    level_number = 3
                    level = load_level(level_number)
                    ok = True
            if ok == True:
                menu = False
                x = 0
                y = 0


        window.blit(textures[8], (0, 0))

        window.blit(textures[9], (50, 50))
        window.blit(textures[10], (250, 50))
        window.blit(textures[11], (50, 250))
        window.blit(textures[12], (250, 250))


    pygame.display.flip()
pygame.quit()