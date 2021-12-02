import sys, pygame
from typing import get_type_hints
from pygame import transform
pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
red = 255,0,0
black = 0, 0, 0
white = 255, 255, 255
x = 0
X_X = pygame.image.load("x.png")
O_O = pygame.image.load("o.png")
X_X = pygame.transform.scale(X_X, (100,100))
O_O = pygame.transform.scale(O_O, (100,100))
quadrante_linha = [50 , 250 , 450]
quadrante_coluna = [50 , 250 , 450]
players_paralelos = ["X","O"]
Cosmetico_XO = [O_O, X_X]
jogador_vez = 0
screen.fill(white)
Matriz_Posicions = [
    ['H','H','H'],
    ['H','H','H'],
    ['H','H','H']]
def tabuleiro():
    pygame.draw.line(screen, black, (200,50),(200,570),8)
    pygame.draw.line(screen, black, (400,50),(400,570),8)
    pygame.draw.line(screen, black, (50,195),(530,195),8)
    pygame.draw.line(screen, black, (50,415),(530,415),8)
def cria_jogadas(pos, vez_jogador):
    index_linha = int(pos[0]/200)  
    index_coluna = int(pos[1]/200) 
    if(Matriz_Posicions[index_coluna][index_linha] == 'H'):
        Matriz_Posicions[index_coluna][index_linha] = players_paralelos[vez_jogador]
        screen.blit(Cosmetico_XO[vez_jogador],(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
        return True
    else:
        print("posição ocupada")
        return False
while True:
    rodada = 0
    screen.fill(white)
    tabuleiro()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                click_pos = pygame.mouse.get_pos()
                fez_jogadas = cria_jogadas(click_pos, jogador_vez)
                if (fez_jogadas == True):
                    if (jogador_vez == 0):  
                        jogador_vez = 1
                        rodada = rodada + 1
                    elif (jogador_vez == 1): 
                        jogador_vez = 0
                        rodada = rodada + 1
        pygame.display.flip()
        if (rodada >= 9):     
            print('\n')
            Matriz_Posicions = [
                ['H','H','H'],
                ['H','H','H'],
                ['H','H','H']]
            break        