import pygame
import time
import random

pygame.init()

#DECLARATION COULEUR
white = (255, 255, 255)
black = (0, 0, 0)
couleurserpent = (0,0,0)

#DIMENSION ECRAN
ecran_largeur = 300
ecran_hauteur = 300

#AFFICHAGE DE LA FENETRE
ecran = pygame.display.set_mode((ecran_largeur, ecran_hauteur))
pygame.display.set_caption('Snake')
 
clock = pygame.time.Clock()

#DIMENSIONS DES BLOCS
dimension_block = 10
 
#DEFINTION DU STYLE DES TEXTES
font_style = pygame.font.SysFont("bahnschrift", 15)
 
#FONCTION D'AFFICHAGE DU SERPENT
def our_snake(dimension_block, snake_list):
    #UN BLOC POUR CHAQUE VALEUR DU TABLEAU SNAKELIST
    for x in snake_list:
        pygame.draw.rect(ecran, couleurserpent, [x[0], x[1], dimension_block, dimension_block])
  
def gameLoop():

    couleurfood = (213, 50, 80)
    game_over = False
    game_fin = False
 
    #POINT DE DEPART DU SERPENT AU CENTRE DE L'ECRAN
    x1 = 100
    y1 = 100
 
    #AU DEPART LE SERPENT NE SE DEPLACE PAS
    x1_change = 0
    y1_change = 0
 
    snake_list = []
    Length_of_snake = 1
 
    #ON CREE LES COORDONNEES DE LA PREMIERE FOOD
    foodx = round(random.randrange(0, ecran_largeur - dimension_block) / 10.0) * 10.0
    foody = round(random.randrange(0, ecran_hauteur - dimension_block) / 10.0) * 10.0
 
    while not game_over:
        
        #Lorsqu'on perd on affiche le message de fin
        while game_fin == True:

            ecran.fill(white) 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    #ON QUITTE AVEC Q
                    if event.key == pygame.K_q:
                        game_over = True
                        game_fin = False
                    #ON RESTART AVEC C
                    if event.key == pygame.K_r:
                        gameLoop()
 
        #DIRECTION DU SERPENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -dimension_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = dimension_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -dimension_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = dimension_block
            
        #CHANGEMENT DE COORDONNEES LORS D'UN D2PLACEMENT
        x1 += x1_change
        y1 += y1_change

        #FOND BLANC
        ecran.fill(white)

        #AFFICHADE DU PREMIER BLOC FOOD
        pygame.draw.rect(ecran, couleurfood, [foodx, foody, dimension_block, dimension_block])
        
        #CREATION DE LA TETE DU SERPENT (PREMIER BLOC)
            #TABLEAU CONTENANT LES COORDONNEE DE LA TETE
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
            #TABLEAU CONTENANT DES TABLEAUX CONTENANT LES CORDONNEES DE CHAUQE BLOC
        snake_list.append(snake_head)
        
        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        #AFFICHAGE DU SERPENT
        our_snake(dimension_block, snake_list)

        pygame.display.update()
    
        #SI COORDONNEES DE LA TET DU SERPENT = CELLE DE LA FOOD : 
        if x1 == foodx and y1 == foody:
            couleurfood = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            print(couleurfood)
            #ALORS ON CREE DE NOUVELLES COORDONNEE A LA FOOD
            foodx = round(random.randrange(0, ecran_largeur - dimension_block) / 10.0) * 10.0
            foody = round(random.randrange(0, ecran_hauteur - dimension_block) / 10.0) * 10.0
            #AJOUTE 1 A LA LONGUEUR DU SERPENT
            Length_of_snake += 3
            print(Length_of_snake)

        #RELANCEMENT DE LA BOUCLE
        vitesse = 10
        vitesse +=10
        clock.tick(vitesse)
        
    pygame.quit()
    quit()

#ON LANCE LE JEU
gameLoop()