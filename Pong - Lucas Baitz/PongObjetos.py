import pygame
from Settings import *

pygame.init()
FONTE = pygame.font.Font('freesansbold.ttf', 32)

class Raquete:

    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.centro = self.y + self.altura / 2
        self.cor = BRANCO
        self.velocidade = 5
        self.pontos = 0
        self.IAdirection = 1

    def desenharRaquete(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura))
    
    def controles(self):
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_w] and self.y - self.velocidade >= 0:
            self.y -= self.velocidade
        if tecla[pygame.K_s] and self.y + self.altura <= ALTURA:
            self.y += self.velocidade
    
    def controles2(self):
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_UP]and self.y - self.velocidade >= 0:
            self.y -= self.velocidade
        if tecla[pygame.K_DOWN] and self.y + self.altura <= ALTURA:
            self.y += self.velocidade
    
    def IA (self, bola):
         if self.centro != bola.y:
            self.y += self.velocidade * self.IAdirection
            if bola.y < self.y:
                self.IAdirection = -1
            elif bola.y > self.y:
                self.IAdirection = 1
            if self.y >= ALTURA - 120:
                self.y = ALTURA - 120
            
        


class PongBola():
    
    def __init__(self, x, y, tamanho):
        self.x = x
        self.y = y
        self.tamanho = tamanho
        self.x_velocidade = -7
        self.y_velocidade = 0

    def desenhaPongBola(self, janela):
        pygame.draw.circle(janela, BRANCO, (self.x, self.y), self.tamanho)
    
    def movimentoPongBola(self):
        self.x += self.x_velocidade
        self.y += self.y_velocidade
    
    def velocidadeY (self, raquete, player):
        
        raquete.centro = raquete.y + raquete.altura / 2
        distancia_y =  raquete.centro - self.y 
        velocidade = (raquete.altura / 2) / self.x_velocidade
        self.y_velocidade = player * (distancia_y / velocidade)
        print(f' Raquete meio == {raquete.centro} - BolaY == {self.y} ///// Distancia = {distancia_y}  / Velocidade = {velocidade} === VelocidadeY == {self.y_velocidade}')
        
        

    
    
    def colissaoPongBola(self, raquete1, raquete2):
        
        # Colisão com o Teto e o Chão
        if self.y + self.tamanho >= ALTURA:
            self.y_velocidade *= -1
        if self.y - self.tamanho <= 0:
            self.y_velocidade *= -1
        
        # Colisão com as raquetes
        # Raquete Player 1
        if self.x_velocidade < 0:
            if self.y >= raquete1.y and self.y <= raquete1.y + raquete1.altura:
                if self.x - self.tamanho <= raquete1.x + raquete1.largura:
                    self.x_velocidade *= -1 

                    self.velocidadeY(raquete1, -1)
                    
                    
        
        # Raquete Player 2
        else:
            if self.y >= raquete2.y and self.y <= raquete2.y + raquete2.altura:
                if self.x + self.tamanho >= raquete2.x:
                    self.x_velocidade *= -1

                    self.velocidadeY(raquete2, 1)

                   
def pontuacao(bola, raquete1, raquete2):
    if bola.x >= LARGURA:
        raquete1.pontos += 1
        bola.y_velocidade = 0
        bola.x_velocidade *= -1
        bola.x, bola.y = X_MEIO, Y_MEIO
    
    elif bola.x <= 0:
        raquete2.pontos += 1
        bola.x_velocidade *= -1
        bola.y_velocidade = 0
        bola.x, bola.y = X_MEIO, Y_MEIO


    




