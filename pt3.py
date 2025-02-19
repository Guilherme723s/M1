# Funções do jogo
def tela_game_over(pontos):
    tela.fill(PRETO)
    desenhar_texto("GAME OVER", LARGURA_TELA // 2 - 100, ALTURA_TELA // 2 - 50, VERMELHO)
    desenhar_texto(f"Pontuação Final: {pontos}", LARGURA_TELA // 2 - 120, ALTURA_TELA // 2, BRANCO)
    desenhar_texto("Pressione ENTER para jogar novamente", LARGURA_TELA // 2 - 200, ALTURA_TELA // 2 + 50, CINZA)
    desenhar_texto("Pressione ESC para sair", LARGURA_TELA // 2 - 150, ALTURA_TELA // 2 + 100, CINZA)
    pygame.display.update()
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    jogo()
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

def jogo():
    jogador = Jogador()
    tiros = []
    inimigos = []
    powerups = []
    pontos = 0
    vidas = jogador.vida
    tempo_tiro_duplo = 0
    tempo_super_velocidade = 0
    
    rodando = True
    while rodando:
        tela.fill(PRETO)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                if time.time() < tempo_tiro_duplo:
                    tiros.append(jogador.atirar())
                    tiros.append(jogador.atirar())
                else:
                    tiros.append(jogador.atirar())
        
        jogador.mover(pygame.key.get_pressed())
        
        if random.randint(1, 50) == 1:
            inimigos.append(Inimigo(random.choice(["quadrado_vermelho", "retangulo_laranja", "hexagono_rosa", "quadrado_roxo"]))))
        
        powerup = gerar_powerup()
        if powerup:
            powerups.append(powerup)
        
        for powerup in powerups[:]:
            powerup.desenhar(tela)
            if jogador.hitbox().colliderect(powerup.hitbox()):
                if powerup.tipo == "tiro_duplo":
                    tempo_tiro_duplo = time.time() + 8
                elif powerup.tipo == "super_velocidade":
                    tempo_super_velocidade = time.time() + 4
                powerups.remove(powerup)
        
        if time.time() < tempo_super_velocidade:
            jogador.velocidade = 10
        else:
            jogador.velocidade = 5
        
        for inimigo in inimigos[:]:
            inimigo.mover()
            inimigo.desenhar(tela)
            if jogador.hitbox().colliderect(inimigo.hitbox()):
                vidas -= inimigo.dano
                inimigos.remove(inimigo)
        
        for tiro in tiros[:]:
            tiro.mover()
            tiro.desenhar(tela)
            for inimigo in inimigos[:]:
                if tiro.hitbox().colliderect(inimigo.hitbox()):
                    inimigo.vida -= 1
                    if inimigo.vida <= 0:
                        pontos += inimigo.pontos
                        inimigos.remove(inimigo)
                    tiros.remove(tiro)
                    break
        
        jogador.desenhar(tela)
        desenhar_texto(f"Pontos: {pontos}", 10, 10)
        desenhar_texto(f"Vidas: {vidas}", 10, 50)
        
        pygame.display.update()
        clock.tick(60)
        
        if vidas <= 0:
            tela_game_over(pontos)

jogo()
pygame.quit()
