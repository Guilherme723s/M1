# Classes para o jogo
class Jogador:
    def __init__(self):
        self.x = LARGURA_TELA // 2
        self.y = ALTURA_TELA - 50
        self.velocidade = 5
        self.largura = 40
        self.altura = 40
        self.image = pygame.Surface((self.largura, self.altura))
        self.image.fill(AZUL)
        self.vida = 3
    
    def mover(self, keys):
        if keys[pygame.K_a] and self.x > 0:  # Movendo para a esquerda
            self.x -= self.velocidade
        if keys[pygame.K_d] and self.x < LARGURA_TELA - self.largura:  # Movendo para a direita
            self.x += self.velocidade
        if keys[pygame.K_w] and self.y > 0:  # Movendo para cima
            self.y -= self.velocidade
        if keys[pygame.K_s] and self.y < ALTURA_TELA - self.altura:  # Movendo para baixo
            self.y += self.velocidade
    
    def desenhar(self, tela):
        tela.blit(self.image, (self.x, self.y))
    
    def atirar(self):
        return Tiro(self.x + self.largura // 2, self.y)
    
    def hitbox(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)

class Tiro:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = -10
        self.image = pygame.Surface((5, 10))
        self.image.fill(BRANCO)
    
    def mover(self):
        self.y += self.velocidade
    
    def desenhar(self, tela):
        tela.blit(self.image, (self.x, self.y))
    
    def hitbox(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

class Inimigo:
    def __init__(self, tipo):
        self.tipo = tipo
        self.x = random.randint(0, LARGURA_TELA - 50)
        self.y = -50
        if tipo == "quadrado_vermelho":
            self.velocidade = 7
            self.vida = 1
            self.pontos = 15
            self.dano = 1
            self.image = pygame.Surface((40, 40))
            self.image.fill(VERMELHO)
        elif tipo == "retangulo_laranja":
            self.velocidade = 3
            self.vida = 5
            self.pontos = 40
            self.dano = 3
            self.image = pygame.Surface((60, 80))
            self.image.fill(LARANJA)
        elif tipo == "hexagono_rosa":
            self.velocidade = 5
            self.vida = 2
            self.pontos = 25
            self.dano = 2
            self.image = pygame.Surface((50, 50))
            self.image.fill(ROSA)
            self.direcao = random.choice([-1, 1])
        elif tipo == "quadrado_roxo":
            self.velocidade = 2
            self.vida = 10
            self.pontos = 50
            self.dano = 4
            self.image = pygame.Surface((60, 60))
            self.image.fill(ROXO)
            self.direcao = random.choice([-1, 1])
    
    def mover(self):
        self.y += self.velocidade
        if self.tipo in ["hexagono_rosa", "quadrado_roxo"]:
            self.x += self.direcao * 2
            if self.x <= 0 or self.x >= LARGURA_TELA - 50:
                self.direcao *= -1
    
    def desenhar(self, tela):
        tela.blit(self.image, (self.x, self.y))
    
    def hitbox(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

class PowerUp:
    def __init__(self, tipo):
        self.tipo = tipo
        self.x = random.randint(50, LARGURA_TELA - 50)
        self.y = random.randint(50, ALTURA_TELA - 200)
        self.largura = 30
        self.altura = 30
        self.image = pygame.Surface((self.largura, self.altura))
        self.image.fill(DOURADO if tipo == "tiro_duplo" else MARROM)

    def desenhar(self, tela):
        tela.blit(self.image, (self.x, self.y))

    def hitbox(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)

def gerar_powerup():
    if random.randint(1, 300) == 1:  # Pequena chance de spawn
        return PowerUp(random.choice(["tiro_duplo", "super_velocidade"]))
    return None
