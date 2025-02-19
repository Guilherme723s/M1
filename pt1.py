import pygame
import random
import time

pygame.init()

# Definições de cores e constantes
DOURADO = (255, 215, 0)
MARROM = (139, 69, 19)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
CINZA = (169, 169, 169)
AMARELO = (255, 255, 0)
LARANJA = (255, 165, 0)
ROSA = (255, 20, 147)
ROXO = (128, 0, 128)

LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Mini Pistola")

clock = pygame.time.Clock()
fonte = pygame.font.Font(None, 36)

def desenhar_texto(texto, x, y, cor=BRANCO):
    render = fonte.render(texto, True, cor)
    tela.blit(render, (x, y))
