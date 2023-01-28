import pygame
from PongObjetos import *
from Settings import *

pygame.init()

# Nome do Jogo e Criando a janela, relogio
pygame.display.set_caption('Pong - Lucas Baitz')
JANELA = pygame.display.set_mode((LARGURA, ALTURA))
FONTE = pygame.font.Font('freesansbold.ttf', 32)
relogio = pygame.time.Clock()

# Criando os jogadores e determinando suas posições
player_1 = Raquete(25, ALTURA // 2 - RAQUETE_ALTURA // 2, RAQUETE_LARGURA, RAQUETE_ALTURA)
player_2 = Raquete(LARGURA - 25 - RAQUETE_LARGURA, ALTURA // 2 - RAQUETE_ALTURA // 2, RAQUETE_LARGURA, RAQUETE_ALTURA)
bola = PongBola(X_MEIO,  Y_MEIO, TAMANHO_BOLA) # Criamos a bola, passamos argumentos X = Centro da tela horizontal e Y = Centro da tela vertical





def display(janela):
    janela.fill(PRETO)
    # Campo desenhado no meio da tela sempre (largura da tela // 2 - (5 // 2), no meio, grossura de 5px e altura da tela
    campo = pygame.draw.rect(janela, CINZA, (LARGURA // 2 - (5 // 2), ALTURA // 2 - (ALTURA // 2), 1, ALTURA))
    raquete1Placar = FONTE.render(f'{player_1.pontos}', 1, CINZA)
    raquete2Placar = FONTE.render(f'{player_2.pontos}', 1, CINZA)
    
    if player_1.pontos >= PLACAR_VENCEDOR or player_2.pontos >= PLACAR_VENCEDOR:
        if player_1.pontos >= PLACAR_VENCEDOR:
            VENCEDOR = 'Jogador - 1'
        elif player_2.pontos >= PLACAR_VENCEDOR:
            VENCEDOR = 'Jogador - 2'
        texto_gameover = FONTE.render(f'{VENCEDOR} VENCEU!', 1, CINZA)  
        janela.blit(texto_gameover, (X_MEIO - 150, Y_MEIO - 40))
    
    janela.blit(raquete2Placar, (X_MEIO + 5, Y_MEIO))
    janela.blit(raquete1Placar, (X_MEIO - 22, Y_MEIO))
    pontuacao(bola, player_1, player_2)
    
    player_1.desenharRaquete(janela)
    player_2.desenharRaquete(janela)
   
    player_1.controles()
    player_2.controles2()
    # player_2.IA(bola)

    bola.desenhaPongBola(janela)
    bola.movimentoPongBola()
    bola.colissaoPongBola(player_1, player_2)
    


    pygame.display.update()

def Jogo():
    rodando = True
    while rodando:
        relogio.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
                break
        
        display(JANELA)
        

    pygame.quit()


Jogo()