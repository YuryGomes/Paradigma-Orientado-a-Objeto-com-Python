# Importa as bibliotecas necessárias
import pygame  # Biblioteca para criação de jogos em Python
import os  # Biblioteca para interagir com o sistema operacional (manipulação de arquivos)
import random  # Biblioteca para geração de números aleatórios, usada para criar obstáculos e outros efeitos

# Inicializa o Pygame (necessário para o funcionamento da biblioteca)
pygame.init()

# Constantes Globais que definem a configuração da tela do jogo
SCREEN_HEIGHT = 600  # Define a altura da tela do jogo (600 pixels)
SCREEN_WIDTH = 1100  # Define a largura da tela do jogo (1100 pixels)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Cria a tela de jogo com as dimensões especificadas

# Carrega as imagens do personagem "Dino Guido" (as imagens de animação do personagem enquanto ele corre, pula e se agacha)
RUNNING = [pygame.image.load(os.path.join("Jogo/Dino", "DinoRun1.png")),  # Imagem do Dino correndo, quadro 1
           pygame.image.load(os.path.join("Jogo/Dino", "DinoRun2.png"))]  # Imagem do Dino correndo, quadro 2
JUMPING = pygame.image.load(os.path.join("Jogo/Dino", "DinoJump.png"))  # Imagem do Dino pulando
DUCKING = [pygame.image.load(os.path.join("Jogo/Dino", "DinoDuck1.png")),  # Imagem do Dino agachado, quadro 1
           pygame.image.load(os.path.join("Jogo/Dino", "DinoDuck2.png"))]  # Imagem do Dino agachado, quadro 2

# Carrega as imagens do personagem "Dino Python" (outro conjunto de animações do Dino)
RUNNING2 = [pygame.image.load(os.path.join("Jogo/Dino2", "DinoRun1.png")),  # Imagem do Dino2 correndo, quadro 1
            pygame.image.load(os.path.join("Jogo/Dino2", "DinoRun2.png"))]  # Imagem do Dino2 correndo, quadro 2
JUMPING2 = pygame.image.load(os.path.join("Jogo/Dino2", "DinoJump.png"))  # Imagem do Dino2 pulando
DUCKING2 = [pygame.image.load(os.path.join("Jogo/Dino2", "DinoDuck1.png")),  # Imagem do Dino2 agachado, quadro 1
            pygame.image.load(os.path.join("Jogo/Dino2", "DinoDuck2.png"))]  # Imagem do Dino2 agachado, quadro 2

# Carrega as imagens dos obstáculos (cactos e pássaros)
# Obstáculos pequenos (cactos de diferentes tamanhos)
SMALL = [pygame.image.load(os.path.join("Jogo/Obstaculos", "SmallObstaculos1.png")),  #  pequeno, variação 1
                pygame.image.load(os.path.join("Jogo/Obstaculos", "SmallObstaculos2.png")),  
                pygame.image.load(os.path.join("Jogo/Obstaculos", "SmallObstaculos3.png"))] 
# Obstáculos grandes (cactos maiores)
LARGE = [pygame.image.load(os.path.join("Jogo/Obstaculos", "LargeObstaculos1.png")),  #  grande, variação 1
                pygame.image.load(os.path.join("Jogo/Obstaculos", "LargeObstaculos2.png")),
                pygame.image.load(os.path.join("Jogo/Obstaculos", "LargeObstaculos3.png"))] 

# Carrega as imagens dos pássaros no jogo (obstáculo voador)
PYPASSARO = [pygame.image.load(os.path.join("Jogo/PYPASSARO", "Pypassaro1.png")),  # Pássaro, quadro 1
             pygame.image.load(os.path.join("Jogo/PYPASSARO", "Pypassaro2.png"))]  # Pássaro, quadro 2

# Carrega a imagem da nuvem (que será usada no fundo do jogo)
CLOUD = pygame.image.load(os.path.join("Jogo/Other", "Cloud.png"))  # Imagem da nuvem no jogo
# Carrega a imagem de fundo (a "pista" ou cenário por onde o Dino corre)
BG = pygame.image.load(os.path.join("Jogo/Other", "Track.png"))  # Imagem do fundo do jogo

# Carrega imagens de diferentes temas ou variações do fundo (cenários alternativos)
TEMAS = [pygame.image.load(os.path.join("Jogo/other", "Tema.png")),  # Tema padrão
         pygame.image.load(os.path.join("Jogo/other", "Tema0.png")),  # Tema alternativo 0
         pygame.image.load(os.path.join("Jogo/other", "Tema1.png")),  # Tema alternativo 1
         pygame.image.load(os.path.join("Jogo/other", "Tema3.png")),  # Tema alternativo 3
         pygame.image.load(os.path.join("Jogo/other", "Tema4.png"))]  # Tema alternativo 4

# Função para desenhar texto com múltiplas linhas na tela
def draw_text_multiline(text, font, surface, x, y, color, line_spacing=30):
    # Divide o texto em várias linhas (caso haja quebras de linha)
    lines = text.splitlines()
    for line in lines:
        # Renderiza cada linha de texto
        text_surface = font.render(line, True, color)  # Cria uma superfície para a linha de texto com a cor desejada
        # Obtém o retângulo da área onde o texto será desenhado
        text_rect = text_surface.get_rect()
        # Alinha a linha de texto ao centro horizontalmente (x) e define a posição vertical (y)
        text_rect.centerx = x
        text_rect.y = y
        # Desenha a linha de texto na tela
        surface.blit(text_surface, text_rect)
        # Move a posição Y para a próxima linha, considerando a altura da linha e o espaçamento entre as linhas
        y += text_rect.height + line_spacing  # Incrementa a posição Y para a próxima linha de texto com o espaçamento definido



def draw_gradient_background(surface, color1, color2):
    """Desenha um fundo com gradiente vertical utilizando cores do gradiente circular."""
    for y in range(SCREEN_HEIGHT):
        # Calcula a cor para cada linha
        ratio = y / SCREEN_HEIGHT
        color = (
            int(color1[0] * (1 - ratio) + color2[0] * ratio),
            int(color1[1] * (1 - ratio) + color2[1] * ratio),
            int(color1[2] * (1 - ratio) + color2[2] * ratio)
        )
        pygame.draw.line(surface, color, (0, y), (SCREEN_WIDTH, y))

def draw_text_with_shadow(surface, text, font, position, shadow_offset=(2, 2), shadow_color=(0, 0, 0), text_color=(255, 255, 255)):
    text_surface = font.render(text, True, text_color)
    shadow_surface = font.render(text, True, shadow_color)

    # Desenha a sombra
    shadow_rect = shadow_surface.get_rect(center=(position[0] + shadow_offset[0], position[1] + shadow_offset[1]))
    surface.blit(shadow_surface, shadow_rect)
    
    # Desenha o texto
    text_rect = text_surface.get_rect(center=position)
    surface.blit(text_surface, text_rect)

def draw_text_with_background(screen, text, font, position, background_color):
    # Renderiza o texto
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=position)

    # Desenha o fundo
    background_rect = pygame.Rect(text_rect.x - 10, text_rect.y - 10, text_rect.width + 20, text_rect.height + 20)
    pygame.draw.rect(screen, background_color, background_rect, border_radius=10)

    # Desenha o texto
    screen.blit(text_surface, text_rect)

def draw_character_with_name(screen, character_image, name, position, spacing):
    # Desenha a imagem do personagem
    screen.blit(character_image, position)
    
    # Calcula a posição do nome
    font_name = pygame.font.Font('freesansbold.ttf', 30)
    name_text = font_name.render(name, True, (255, 255, 255))
    name_x = position[0] + (character_image.get_width() // 2) - (name_text.get_width() // 2)
    name_y = position[1] - spacing  # Espaçamento acima da imagem

    # Desenha o nome
    screen.blit(name_text, (name_x, name_y))

class Dinossauro:
    # Posições e velocidades do Dinossauro
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self, run_img, duck_img, jump_img):
        # Inicializa as imagens e estados do Dinossauro
        self.duck_img = duck_img
        self.run_img = run_img
        self.jump_img = jump_img

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0  # Índice para animação
        self.jump_vel = self.JUMP_VEL  # Velocidade do salto
        self.image = self.run_img[0]  # Imagem inicial
        self.dino_rect = self.image.get_rect()  # Retângulo para colisão
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        # Atualiza o estado do Dinossauro com base na entrada do usuário
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:  # Reseta o índice de passos
            self.step_index = 0

        # Controle de movimentos
        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        # Atualiza a imagem e posição do Dinossauro quando agacha
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        # Atualiza a imagem e posição do Dinossauro enquanto corre
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        # Lógica de salto do Dinossauro
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        # Desenha o Dinossauro na tela
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


class Nuvem:
    def __init__(self):
        # Inicializa a nuvem
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        # Atualiza a posição da nuvem
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        # Desenha a nuvem na tela
        SCREEN.blit(self.image, (self.x, self.y))

class Obstaculo:
    def __init__(self, image, type):
        # Inicializa o obstáculo
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

        # Ajusta o retângulo de colisão
        self.adjust_collision_rect()

    def adjust_collision_rect(self):
        # Diminui a largura e a altura do retângulo de colisão
        self.rect.inflate_ip(-self.rect.width * 0.5, -self.rect.height * 0.5)  # Ajuste conforme necessário

    def update(self):
        # Atualiza a posição do obstáculo
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstaculos.pop()  # Remove o obstáculo se sair da tela

    def draw(self, SCREEN):
        # Desenha o obstáculo na tela
        SCREEN.blit(self.image[self.type], self.rect)

class CactoPequeno(Obstaculo):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325  # Posição vertical do cacto pequeno

class CactoGrande(Obstaculo):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300  # Posição vertical do cacto grande

class Passaro(Obstaculo):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250  # Posição vertical do pássaro
        self.index = 0

    def draw(self, SCREEN):
        # Animação do pássaro
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1



def menu_personagens():
    run = True
    spacing = 50  # Espaçamento entre o nome e a imagem
    while run:
        # Desenha o fundo com gradiente
        draw_gradient_background(SCREEN, (255, 100, 0), (255, 150, 50))  # Gradiente de laranja escuro para claro

        # Fonte e título
        font_title = pygame.font.Font('freesansbold.ttf', 50)
        title_text = "Escolha seu Personagem:"
        draw_text_with_background(SCREEN, title_text, font_title, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 250), (50, 50, 50))

        # Carregar e aumentar o tamanho das imagens dos personagens
        character1_image = pygame.image.load(os.path.join("Jogo/Dino", "DinoRun1.png"))
        character2_image = pygame.image.load(os.path.join("Jogo/Dino2", "DinoRun1.png"))
        character1_image = pygame.transform.scale(character1_image, (character1_image.get_width() * 2, character1_image.get_height() * 2))
        character2_image = pygame.transform.scale(character2_image, (character2_image.get_width() * 2, character2_image.get_height() * 2))

        # Posições dos personagens (centralizadas)
        character1_x = SCREEN_WIDTH // 2 - 300
        character2_x = SCREEN_WIDTH // 2 + 150
        character_y = SCREEN_HEIGHT // 2 - 100

        # Desenha os personagens
        SCREEN.blit(character1_image, (character1_x, character_y))
        SCREEN.blit(character2_image, (character2_x, character_y))

        # Nomes dos personagens
        font_name = pygame.font.Font('freesansbold.ttf', 30)
        name1_text = "Dino Guido"
        name2_text = "Dino Python"

        # Desenha os nomes com sombra
        draw_text_with_shadow(SCREEN, name1_text, font_name, (character1_x + (character1_image.get_width() // 2), character_y - spacing))
        draw_text_with_shadow(SCREEN, name2_text, font_name, (character2_x + (character2_image.get_width() // 2), character_y - spacing))

        # Identificações das opções
        font_option = pygame.font.Font('freesansbold.ttf', 30)
        option1_text = "Opção 1"
        option2_text = "Opção 2"
        
        # Desenha as opções com sombra
        draw_text_with_shadow(SCREEN, option1_text, font_option, (character1_x + (character1_image.get_width() // 2), SCREEN_HEIGHT // 2 + 150))
        draw_text_with_shadow(SCREEN, option2_text, font_option, (character2_x + (character2_image.get_width() // 2), SCREEN_HEIGHT // 2 + 150))

        pygame.display.update()

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.unicode == '1':
                    Corpo_do_Jogo(game_speed, character='dino1')  # Passa o personagem escolhido
                elif event.unicode == '2':
                    Corpo_do_Jogo(game_speed, character='dino2')  # Passa o personagem escolhido



def Corpo_do_Jogo(game_speed, character='dino1'):
    if character == 'dino1':
        player_images = (RUNNING, DUCKING, JUMPING)  # Imagens do primeiro dinossauro
    else:
        player_images = (RUNNING2, DUCKING2, JUMPING2)  # Imagens do segundo dinossauro

    player = Dinossauro(player_images[0], player_images[1], player_images[2])  # Passa as imagens corretamente

    global x_pos_bg, y_pos_bg, points, obstaculos
    run = True
    clock = pygame.time.Clock()  # Controla o frame rate
    nuvem = Nuvem()  # Cria a Nuvem
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0  # Pontuação inicial
    font = pygame.font.Font('freesansbold.ttf', 25)  # Fonte para a pontuação
    obstaculos = []  # Lista de obstáculos
    death_count = 0  # Contador de mortes

    # Variável de controle para alternar temas
    current_theme_index = 0
    BG = TEMAS[current_theme_index]  # Começa com o primeiro tema
    BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Redimensiona para o tamanho da tela
    theme_change_interval = 500  # Define o intervalo em pontos para mudança de tema

    def score():
        global points, game_speed
        points += 1  # Aumenta a pontuação
        if points % 100 == 0:  # Aumenta a velocidade do jogo a cada 100 pontos
            game_speed += 1

        # Alterna para o próximo tema após alcançar o intervalo de pontuação definido
        nonlocal current_theme_index, BG
        if points % theme_change_interval == 0:
            current_theme_index = (current_theme_index + 1) % len(TEMAS)
            BG = TEMAS[current_theme_index]
            BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Define o retângulo de fundo atrás da pontuação
        text_background_rect = pygame.Rect(950, 30, 150, 40)  # Ajuste conforme necessário
        pygame.draw.rect(SCREEN, (255, 100, 0), text_background_rect)  # Retângulo preto de fundo
       

        # Exibe a pontuação na tela
        text = font.render("Pontos: " + str(points), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (1025, 50)  # Ajusta a posição central do texto
        SCREEN.blit(text, textRect)


    
    def background():
        # Desenha a imagem de fundo
        SCREEN.blit(BG, (0, 0))  # Desenha a imagem de fundo na posição (0, 0)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Encerra o jogo se a janela for fechada

        # Desenha o fundo primeiro para que fique atrás dos outros elementos
        background()

        userInput = pygame.key.get_pressed()  # Captura a entrada do usuário

        # Atualiza e desenha o Dinossauro
        player.draw(SCREEN)
        player.update(userInput)

        # Cria obstáculos aleatoriamente
        if len(obstaculos) == 0:
            if random.randint(0, 2) == 0:
                obstaculos.append(CactoPequeno(SMALL))
            elif random.randint(0, 2) == 1:
                obstaculos.append(CactoGrande(LARGE))
            elif random.randint(0, 2) == 2:
                obstaculos.append(Passaro(PYPASSARO))

        # Atualiza e desenha os obstáculos, verifica colisão
        for obstaculo in obstaculos:
            obstaculo.draw(SCREEN)
            obstaculo.update()

            # Verifica colisão com uma margem
            if player.dino_rect.colliderect(obstaculo.rect.inflate(-10, -10)):  # Adiciona margem negativa
                pygame.time.delay(2000)  # Delay para reiniciar
                death_count += 1
                menu(death_count)

        # Atualiza e desenha a nuvem
        nuvem.draw(SCREEN)
        nuvem.update()

        score()  # Atualiza a pontuação

        clock.tick(30)  # Controla a taxa de frames
        pygame.display.update()  # Atualiza a tela


def menu_dificuldade():
    global game_speed
    run = True
    while run:
        # Desenha o fundo com gradiente
        draw_gradient_background(SCREEN, (255, 100, 0), (255, 150, 50))  # Gradiente de laranja escuro para claro

        font_title = pygame.font.Font('freesansbold.ttf', 40)
        title_text = "Selecione a Dificuldade:"

        # Desenha o fundo para o título
        draw_text_with_background(SCREEN, title_text, font_title, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200), (50, 50, 50))

        # Não desenha o título com sombra novamente
        # Se precisar de sombra, faça isso aqui:
        draw_text_with_shadow(SCREEN, title_text, font_title, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200))  # Agora a sombra é aplicada na mesma posição

        options_text = (
            "-> 1. Fácil ('Foco na História') <-\n"
            "-> 2. Médio ('Equilíbrio entre História/Desafio') <-\n"
            "-> 3. Difícil ('Teste suas Habilidades') <-"
        )
        # Divide as opções para aplicar a sombra em cada linha individualmente
        option_lines = options_text.split('\n')
        for i, line in enumerate(option_lines):
            draw_text_with_shadow(SCREEN, line, font_title, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50 + i * 70))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.unicode in '123':
                    game_speed = [10, 20, 30][int(event.unicode) - 1]
                    menu_personagens()  # Chama o menu de seleção de personagens

def Historia_Dica():
    # Função para exibir a história
    run = True
    font = pygame.font.Font('freesansbold.ttf', 20)
    title_font = pygame.font.Font('freesansbold.ttf', 30)

    

    # Título da história
    title = title_font.render("A História do jogo", True, (255, 255, 255))
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 50))

    # Fundo do título
    title_background_rect = pygame.Rect(title_rect.x - 10, title_rect.y - 10, title_rect.width + 20, title_rect.height + 20)
    
    # Conteúdo da história
    story = [
        "-- Jogo possui 2 personagens (Dino Python e o Dino Guido) ambos baseados no autor Guido Van Rossum",
        "-- Possui 05 Temas Intuitivo resumido sobre os passos do Guido Van rossum.",
        "-- 01 Tema fala sobre Onde ele nasceu e o ano junto com sua formação academica.",
        "-- 02 Tema relata seu tempo na faculdade de Amsterdam e as linguagens que conheceu na Epoca. ",
        "-- 03 Tema transcreve seu envolvimento na Empresa CWI e o começo do projeto Python.",
        "-- 04 Tema Mostra sua passagem na Googleplex e o envolvimento com a linguagem Python.  ",
        "-- 05 Tema Mostra sua passagem apos sair da google e os acontecimentos a seguir.",
          "--------------------------------------------------------------------------------------------------------------------------------------------------",
        "Jogo possui 5 Obstaculos durante o percurso",
        "01 Temos a grande criação de Guido Van Rossum Python",
        "02 O Famoso combustivel de todo programador (Cafe)",
        "03 Sua coleção atual de Conjunto Estereo Vintage da Sony",
        "04 IBM 370 que provavelmente Guido possa ter acessado na Epoca",
        "05 CP/M (um sistema operacional para microcomputadores da época) que o guido teve acesso na ",
        "Faculdade",
        "",
        "Pressione 'H' novamente para voltar ao menu."
    ]

    while run:
        # Desenha o fundo com gradiente
        draw_gradient_background(SCREEN, (255, 100, 0), (255, 150, 50))  # Gradiente de laranja escuro para claro 

        # Desenha o fundo do título
        pygame.draw.rect(SCREEN, (50, 50, 50), title_background_rect)  # Cor do fundo

        # Desenha o título
        SCREEN.blit(title, title_rect)

        # Desenha cada linha da história
        for i, line in enumerate(story):
            text_surface = font.render(line, True, (255, 255, 255))
            SCREEN.blit(text_surface, (50, 100 + i * 30))

        pygame.display.update()  # Atualiza a tela

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:  # Pressiona 'H' para voltar
                    run = False

def Menudica():
    run = True
    font = pygame.font.Font('freesansbold.ttf', 20)
    title_font = pygame.font.Font('freesansbold.ttf', 30)

    # Título da história
    title = title_font.render("Dica de Jogo", True, (255, 255, 255))
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 50))

    # Fundo do título
    title_background_rect = pygame.Rect(title_rect.x - 10, title_rect.y - 10, title_rect.width + 20, title_rect.height + 20)

    # Conteúdo da história
    story = [
       "O jogo consiste em 3 Modos de Dificuldades.",
        "-- 01 Modo 1. Fácil ('Foco na História')- consiste no aprendizado dos temas ao fundo para uma melhor",
        "experiencia",
        "-- 02 Modo 2. Médio ('Equilíbrio entre História/Desafio') Uma opção intermediaria entre Desafio e",
        "Historia",
        "-- 03 Modo  3. Difícil ('Teste suas Habilidades') modo focado em jogabilidade e Obtenção de pontos",
        "--------------------------------------------------------------------------------------------------------------------------------------------------",
        "Como jogar:",
        "Para (Pular) Utiliza-se a Seta pra cima no teclado",
        "Para (Agachar) Utiliza-se a Seta para baixo no Teclado",
        "O Personagem se movimenta sozinho não há necessidade de utilizar outras teclas.",
        "",
        "Pressione 'H' novamente para voltar ao menu."
    ]

    while run:
        # Desenha o fundo com gradiente
        draw_gradient_background(SCREEN, (255, 100, 0), (255, 150, 50))

        # Desenha o fundo do título
        pygame.draw.rect(SCREEN, (50, 50, 50), title_background_rect)

        # Desenha o título
        SCREEN.blit(title, title_rect)

        # Desenha cada linha da história
        for i, line in enumerate(story):
            text_surface = font.render(line, True, (255, 255, 255))
            SCREEN.blit(text_surface, (50, 100 + i * 30))

        pygame.display.update()  # Atualiza a tela

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:  # Pressiona 'H' para voltar
                    run = False  # Sai do menu de dicas

def menu(death_count):
    global points
    run = True

    while run:
        # Desenha o fundo com gradiente
        draw_gradient_background(SCREEN, (255, 100, 0), (255, 150, 50))

        # Texto "História" e "Dica de Jogo"
        history_font = pygame.font.Font('freesansbold.ttf', 15)
        history_texts = [
             "Dica de Jogo = Pressione P",
            "História = Pressione H"
            
        ]

        # Desenha os textos na tela
        for i, text in enumerate(history_texts):
            text_surface = history_font.render(text, True, (255, 255, 255))
            history_background_color = (50, 50, 50)
            # Centraliza horizontalmente
            history_width = text_surface.get_width()
            history_position = ((SCREEN_WIDTH - history_width) // 8, 30 + i * 50)  # Ajusta a posição Y
            
            draw_text_with_background(SCREEN, text, history_font, history_position, history_background_color)

        # Texto principal
        if death_count == 0:
            text = "Pressione qualquer tecla para começar"
        else:
            text = "Pressione qualquer tecla para reiniciar"
            score = "Sua Pontuação: " + str(points)

        main_font = pygame.font.Font('freesansbold.ttf', 50)
        draw_text_with_shadow(SCREEN, text, main_font, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))

        if death_count > 0:
            draw_text_with_shadow(SCREEN, score, main_font, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

        # Aumenta a imagem
        dino_image = RUNNING[0]
        scaled_dino_image = pygame.transform.scale(dino_image, (dino_image.get_width() * 2, dino_image.get_height() * 2))
        SCREEN.blit(scaled_dino_image, (SCREEN_WIDTH // 2 - scaled_dino_image.get_width() // 2, SCREEN_HEIGHT // 2 - 170))

        # Assinatura do autor no canto inferior direito
        author_font = pygame.font.Font('freesansbold.ttf', 15)
        author_text = "Autor: Luke | Lucas araujo ramos "
        author_surface = author_font.render(author_text, True, (255, 255, 255))
        SCREEN.blit(author_surface, (SCREEN_WIDTH - author_surface.get_width() - 10, SCREEN_HEIGHT - author_surface.get_height() - 10))

        pygame.display.update()

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    Historia_Dica()  # Chama a função display_story
                elif event.key == pygame.K_p:
                    Menudica()  # Chama a função Menudica
                else:
                    menu_dificuldade()  # Chama o menu de dificuldade

menu(death_count=0)