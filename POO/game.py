import pygame

# 🔧 Inicialização
pygame.init()

# 🪟 Configuração da janela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Movimento com teclado")

# 🎯 Posição inicial do objeto
x = 100
y = 100
velocidade = 1

# 🔄 Controle do loop
rodando = True

# 🎮 Loop principal
while rodando:
    # 📌 Captura eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # ⌨️ Captura teclado (tempo real)
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade

    # 🎨 Desenho
    tela.fill((0, 0, 0))  # fundo preto

    pygame.draw.rect(tela, (255, 0, 0), (x, y, 50, 50))  # quadrado

    # 🔄 Atualiza tela
    pygame.display.update()

# 🧹 Finalização
pygame.quit()