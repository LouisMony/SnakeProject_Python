#pip install pygame
import pygame
import time
import random

#Verifie si tous les modules sont chargés
module_charge = pygame.init()
print(module_charge)

#COULEURS UTILISE DANS LE JEU
fond = (206,221,255)
serpent = (171,214,140)
nourriture = (214, 147,140)
text = (0,0,0)

#DEFINTION DU STYLE DES TEXTES
font_style = pygame.font.SysFont("bahnschrift", 20)

#TAILLE DE LA FENETRE
ecran_largeur = 500
ecran_hauteur = 500
snake_block = 10

#AFFICHAGE DE LA FENETRE
ecran = pygame.display.set_mode((ecran_largeur,ecran_hauteur))
pygame.display.set_caption("Snake")


#FONCTION D'AFFICHAGE DU SCORE
def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, text)
    ecran.blit(value, [0, 0])

#FONCTION D'AFFICHAGE DU MESSAGE DE FIN
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    ecran.blit(mesg, [ecran_largeur / 6, ecran_hauteur / 3])

#Boucle de jeu

loop = True
while loop:
    #ecran.blit(image, (250,250))
    #pygame event
    
    foodx = round(random.randrange(0, ecran_largeur - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, ecran_hauteur - snake_block) / 10.0) * 10.0
    
    ecran.fill(fond)
    pygame.draw.rect(ecran, serpent, [foodx, foody, snake_block, snake_block])
    
    message("You Lost! Press C-Play Again or Q-Quit", text)
    Your_score(1)
    for event in pygame.event.get():
        # event input clavier
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.k_j:
                loop = False
        if event.type == pygame.QUIT:
            loop = False
        
    pygame.display.flip()

#vider le cache
pygame.quit()

    


