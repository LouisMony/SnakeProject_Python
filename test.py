#incrementer le score sans superposition
# 
# #pip install pygame
import pygame
import random

from pygame.constants import MOUSEBUTTONDOWN

#verifie si tous les modules sont chargés
pygame.init()

#creation ecran
ecran = pygame.display.set_mode((800,700))
pygame.display.set_caption("Pierre, Feuille, Ciseaux")

#affiche image
ecran.fill((255,255,255))
imagef = pygame.image.load("feuille.png")
ecran.blit(imagef, (50, 420))
imagec = pygame.image.load("ciseaux2.png")
ecran.blit(imagec, (600, 420))
imagep = pygame.image.load("pierre.png")
ecran.blit(imagep, (325, 420))
imagevs = pygame.image.load("vs.png")
ecran.blit(imagevs, (300, 70))

#style txt
font_style = pygame.font.SysFont("bahnschrift", 20)
text = (0, 0, 0)

#contenu txt
scorejoueur = 0

def ScoreJoueur(score):
    value = font_style.render("Joueur : " + str(score), True, text)
    ecran.blit(value, [100, 0])

def ScoreMachine(scoremachine):
    value = font_style.render("Machine : " + str(scoremachine), True, text)
    ecran.blit(value, [600, 0])

def Jouer(score):
    value = font_style.render("Choisissez un symbole pour jouer", True, text)
    ecran.blit(value, [250, 350])


#random choice de la machine
ChoixMachine = ["ciseaux", "feuille", "pierre"]
ChoixMachineFinal = random.choice(ChoixMachine)
if ChoixMachineFinal == "ciseaux":
    ecran.blit(imagec, (575, 90))
if ChoixMachineFinal == "feuille":
    ecran.blit(imagef, (575, 90))
if ChoixMachineFinal == "pierre":
    ecran.blit(imagep, (575, 90))


#boucle de jeu
loop = True
i= 0
while loop:
    
    #affichage des scores
    ScoreJoueur(scorejoueur)
    ScoreMachine("1")
    Jouer("")

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #ON RESTART AVEC C
            if event.key == pygame.K_c:
                pygame.quit()
                quit()

    
    for event in pygame.event.get():
        # event input clavier
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.k_j:
                loop = False
        if event.type == pygame.QUIT:
            loop = False


        #action de click
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            #affichage et actions des boutons restart et exit apres avoir jouer 1 fois
            restart_img = pygame.image.load("bouton_restart.png")
            ecran.blit(restart_img, (225, 620))
            exit_img = pygame.image.load("bouton_exit.png")
            ecran.blit(exit_img, (500, 620))

            clickrestart = pygame.Rect((225,620), (100, 40))
            clickexit = pygame.Rect((500,620), (100, 40))
            if clickrestart.collidepoint(pos):
                print('restart')
            if clickexit.collidepoint(pos):
                print('exit')


            #affichage et actions des boutons symboles
            clickfeuille = pygame.Rect((50,420), (150, 150))
            clickpierre = pygame.Rect((325,400), (150, 150))
            clickciseaux = pygame.Rect((600,400), (150, 150))

            if clickfeuille.collidepoint(pos):
                ecran.blit(imagef, (75, 90))
                ChoixHumainFinal = "feuille"

            if clickpierre.collidepoint(pos):
                ecran.blit(imagep, (75, 90))
                ChoixHumainFinal = "pierre"

            if clickciseaux.collidepoint(pos):
                ecran.blit(imagec, (75, 90))
                ChoixHumainFinal = "ciseaux"

            #regles et augmentation du score
            if ChoixMachineFinal == ChoixHumainFinal:
                print("match nul")

            if ChoixMachineFinal == "ciseaux" and ChoixHumainFinal == "pierre":
                scorejoueur = scorejoueur + 1
                print(scorejoueur)
                

            if ChoixMachineFinal == "feuille" and ChoixHumainFinal == "ciseaux":
                scorejoueur = scorejoueur + 1
                print(scorejoueur)
                
            if ChoixMachineFinal == "pierre" and ChoixHumainFinal == "feuille":
                scorejoueur = scorejoueur + 1
                print(scorejoueur)
            
            if ChoixMachineFinal == "ciseaux" and ChoixHumainFinal == "feuille":
                print("victoire machine")
               
            if ChoixMachineFinal == "feuille" and ChoixHumainFinal == "pierre":
                print("victoire machine")
                
            if ChoixMachineFinal == "pierre" and ChoixHumainFinal == "ciseaux":
                print("victoire machine")
      
        

    pygame.display.flip()

#vider le cache
pygame.quit()
