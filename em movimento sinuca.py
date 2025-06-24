<<<<<<< HEAD
=======
import os
import sys

# Garante que o diretório de trabalho seja o mesmo do script
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

>>>>>>> d302c89 (Primeiro commit do projeto Sinuca Delícia)
import pygame
import sys
import math
import random
import os

# --- Inicialização --- 
pygame.init()
audio_enabled = False
try:
    pygame.mixer.init()
    audio_enabled = True
    print("Mixer de áudio inicializado.")
except pygame.error as e:
    print(f"Erro ao inicializar mixer: {e}. Sem som.")

pygame.font.init()

# --- Constantes --- 
LARGURA, ALTURA = 0, 0  # Será definido após setar tela cheia
LARGURA_MESA = 700
ALTURA_MESA = 350
RAIO_BOLA = 15
RAIO_BURACO = 20
RAIO_ATRACAO_BURACO = RAIO_BURACO * 2.5
FORCA_ATRACAO_BURACO = 0.18
VELOCIDADE_MIN = 0.15
FORCA_MAX = 28.0  # Aumenta a força máxima permitida (antes era 15.0)
ATRITO = 0.985
FADE_SPEED = 8  # Deixe o fade mais rápido (era 1)
ANIM_TACOS_DELAY = 1000
ANIM_TACOS_SPEED = 4
TACO_RECUO_MAX = 30
LIMITE_PUXADA_ESTILINGUE = 150
FATOR_FORCA_ESTILINGUE = FORCA_MAX / LIMITE_PUXADA_ESTILINGUE
DURACAO_IMAGEM_INICIAL = 2000
DELAY_SOM_ANIM = 500
DELAY_MUSICA_JOGO = 1000

# Cores
COR_MESA = (0, 100, 0)
COR_BORDA = (50, 25, 0)
COR_BRANCA = (255, 255, 255)
COR_PRETA = (0, 0, 0)
COR_VERMELHA = (255, 0, 0)
COR_AMARELA = (255, 255, 0)
COR_AZUL = (0, 0, 255)
COR_LARANJA = (255, 165, 0)
COR_VERDE = (0, 128, 0)
COR_ROXA = (128, 0, 128)
COR_MARROM = (139, 69, 19)
COR_TEXTO = (255, 255, 255)
COR_FUNDO = (20, 20, 20)
COR_BOTAO = (100, 100, 100)
COR_BOTAO_HOVER = (150, 150, 150)
COR_JOGADOR1 = (0, 0, 255)
COR_JOGADOR2 = (255, 0, 0)
COR_MIRA = (255, 255, 255, 150)

CORES_BOLAS = {
    1: COR_AMARELA, 2: COR_AZUL, 3: COR_VERMELHA, 4: COR_ROXA, 5: COR_LARANJA,
    6: COR_VERDE, 7: COR_MARROM, 8: COR_PRETA, 9: COR_AMARELA, 10: COR_AZUL,
    11: COR_VERMELHA, 12: COR_ROXA, 13: COR_LARANJA, 14: COR_VERDE, 15: COR_MARROM
}

# Estados do Jogo
MENU = 0
REGRAS = 1
MOSTRAR_IMAGEM_INICIAL = 2
ANIMACAO_TACOS = 3
JOGO = 4
PAUSA = 5
REPOSICIONAR = 6
FIM_JOGO = 7
DOACAO = 8

# --- Configuração Inicial --- 
pygame.display.set_caption("Sinuca Delicia vReescrita")
tela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Modo tela cheia
LARGURA, ALTURA = tela.get_size()  # Atualiza as dimensões

# Ajuste para mesa maior na altura
LARGURA_MESA = int(LARGURA * 0.74)
ALTURA_MESA = int(ALTURA * 0.52)  # aumentada de 0.44 para 0.52
# Centralizar a mesa verticalmente e horizontalmente
MESA_OFFSET_X = (LARGURA - LARGURA_MESA) // 2
MESA_OFFSET_Y = (ALTURA - ALTURA_MESA) // 2
clock = pygame.time.Clock()

# Atualize as fontes para tamanhos proporcionais à tela
fonte_pequena = pygame.font.SysFont("Arial", max(16, LARGURA // 60))
fonte_media = pygame.font.SysFont("Arial", max(24, LARGURA // 40))
fonte_grande = pygame.font.SysFont("Arial", max(36, LARGURA // 25), bold=True)

# Diretório base para os assets
try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    base_dir = os.path.abspath(".")
assets_dir = os.path.join(base_dir, "assets")
print(f"Diretório de assets: {assets_dir}")

# --- Função para mostrar intro GIF ---
def mostrar_intro_gif():
    try:
        import PIL.Image
    except ImportError:
        print("Pillow não instalado. Instale com 'pip install pillow'.")
        pygame.time.delay(9000)
        return
    gif_path = os.path.join(assets_dir, "carregar.gif")
    try:
        gif = PIL.Image.open(gif_path)
        frames = []
        try:
            while True:
                frame = gif.convert("RGBA")
                mode = frame.mode
                size = frame.size
                data = frame.tobytes()
                py_image = pygame.image.fromstring(data, size, mode)
                frames.append(py_image)
                gif.seek(gif.tell() + 1)
        except EOFError:
            pass

        if not frames:
            raise Exception("Nenhum frame encontrado no GIF.")

        # Exibe o GIF a 30fps por 9 segundos
<<<<<<< HEAD
        fps = 30
=======
        fps = 40
>>>>>>> d302c89 (Primeiro commit do projeto Sinuca Delícia)
        total_intro_duration = 9000  # milissegundos
        total_frames = fps * 9
        frame_duration = 1000 // fps  # ms por frame

        # Se o GIF tem menos frames que o necessário, repete os frames
        extended_frames = []
        for i in range(total_frames):
            extended_frames.append(frames[i % len(frames)])

        start_time = pygame.time.get_ticks()
        elapsed = 0
        frame_idx = 0
        while elapsed < total_intro_duration:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            tela.fill((0, 0, 0))
            frame = pygame.transform.scale(extended_frames[frame_idx], (LARGURA, ALTURA))
            tela.blit(frame, (0, 0))
            pygame.display.flip()
            pygame.time.delay(frame_duration)
            elapsed = pygame.time.get_ticks() - start_time
            frame_idx += 1
            if frame_idx >= total_frames:
                frame_idx = 0  # Loop até completar 9 segundos
    except Exception as e:
        print(f"Erro ao exibir intro GIF: {e}")
        pygame.time.delay(9000)

def desenhar_gif_loop(nome_gif, largura, altura):
    try:
        import PIL.Image
    except ImportError:
        print("Pillow não instalado. Instale com 'pip install pillow'.")
        tela.fill((0, 0, 0))
        return None, None, None
    gif_path = os.path.join(assets_dir, nome_gif)
    try:
        gif = PIL.Image.open(gif_path)
        frames = []
        durations = []
        try:
            while True:
                frame = gif.convert("RGBA")
                mode = frame.mode
                size = frame.size
                data = frame.tobytes()
                py_image = pygame.image.fromstring(data, size, mode)
                frames.append(py_image)
                durations.append(9)  
                gif.seek(gif.tell() + 1)
        except EOFError:
            pass
        if not frames:
            raise Exception("Nenhum frame encontrado no GIF.")
        return frames, durations, len(frames)
    except Exception as e:
        print(f"Erro ao exibir GIF de fundo: {e}")
        tela.fill((0, 0, 0))
        return None, None, None

# --- Funções Utilitárias --- 

def carregar_imagem(nome_arquivo, tamanho=None, alpha=False):
    caminho = os.path.join(assets_dir, nome_arquivo)
    try:
        if alpha:
            imagem = pygame.image.load(caminho).convert_alpha()
        else:
            imagem = pygame.image.load(caminho).convert()
        if tamanho:
            imagem = pygame.transform.scale(imagem, tamanho)
        print(f"Imagem {nome_arquivo} carregada.")
        return imagem
    except Exception as e:
        print(f"Erro ao carregar imagem {nome_arquivo}: {e}")
        surf = pygame.Surface(tamanho if tamanho else (50, 50), pygame.SRCALPHA)
        surf.fill((255, 0, 255, 100))
        try:
            texto_erro = fonte_pequena.render("Erro", True, (255, 255, 255))
            surf.blit(texto_erro, (5,5))
        except Exception:
            pass
        return surf

def carregar_som(nome_arquivo):
    if not audio_enabled:
        return None
    caminho = os.path.join(assets_dir, nome_arquivo)
    try:
        som = pygame.mixer.Sound(caminho)
        som.set_volume(0.3)
        print(f"Som {nome_arquivo} carregado.")
        return som
    except Exception as e:
        print(f"Erro ao carregar som {nome_arquivo}: {e}")
        return None

def carregar_musica(nome_arquivo):
    if not audio_enabled:
        return
    caminho = os.path.join(assets_dir, nome_arquivo)
    try:
        pygame.mixer.music.load(caminho)
        pygame.mixer.music.set_volume(0.5)
        print(f"Música {nome_arquivo} carregada.")
    except Exception as e:
        print(f"Erro ao carregar música {nome_arquivo}: {e}")

def desenhar_linha_pontilhada(surf, color, start_pos, end_pos, width=1, dash_length=5):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dl = dash_length

    if (x1 == x2 and y1 == y2): return

    dx = x2 - x1
    dy = y2 - y1
    distance = math.hypot(dx, dy)
    if distance == 0: return
    dx /= distance
    dy /= distance

    for i in range(0, int(distance / (2 * dl)), 1):
        start = (x1 + dx * i * 2 * dl, y1 + dy * i * 2 * dl)
        end = (x1 + dx * (i * 2 * dl + dl), y1 + dy * (i * 2 * dl + dl))
        pygame.draw.line(surf, color, start, end, width)

# --- Classes --- 

class Bola:
    def __init__(self, x, y, cor, listrada=False, numero=0):
        self.x = float(x)
        self.y = float(y)
        self.cor = cor
        self.vx = 0.0
        self.vy = 0.0
        self.raio = RAIO_BOLA
        self.listrada = listrada
        self.numero = numero
        self.na_mesa = True
        self.massa = 1.0

    def mover(self):
        if not self.na_mesa:
            return
        self.x += self.vx
        self.y += self.vy
        self.vx *= ATRITO
        self.vy *= ATRITO

        if self.vx**2 + self.vy**2 < VELOCIDADE_MIN**2:
            self.vx = 0
            self.vy = 0

    def colisao_parede(self, x_min, y_min, x_max, y_max):
        if not self.na_mesa:
            return
        restituicao_parede = 0.8

        # Lista dos buracos (deve ser igual à usada no jogo)
        buracos = [
            (x_min, y_min),
            (x_min + (x_max - x_min) // 2, y_min - 5),
            (x_max, y_min),
            (x_min, y_max),
            (x_min + (x_max - x_min) // 2, y_max + 5),
            (x_max, y_max)
        ]

        # Função auxiliar para saber se está perto de algum buraco
        def perto_de_buraco(x, y):
            for bx, by in buracos:
                if (x - bx) ** 2 + (y - by) ** 2 < (RAIO_BURACO + self.raio) ** 2:
                    return True
            return False

        # Parede esquerda
        if self.x - self.raio < x_min and not perto_de_buraco(x_min, self.y):
            self.x = x_min + self.raio
            self.vx = -self.vx * restituicao_parede
        # Parede direita
        elif self.x + self.raio > x_max and not perto_de_buraco(x_max, self.y):
            self.x = x_max - self.raio
            self.vx = -self.vx * restituicao_parede

        # Parede superior
        if self.y - self.raio < y_min and not perto_de_buraco(self.x, y_min):
            self.y = y_min + self.raio
            self.vy = -self.vy * restituicao_parede
        # Parede inferior
        elif self.y + self.raio > y_max and not perto_de_buraco(self.x, y_max):
            self.y = y_max - self.raio
            self.vy = -self.vy * restituicao_parede

    def aplicar_atracao_buraco(self, buracos):
        if not self.na_mesa:
            return
        for buraco in buracos:
            bx, by = buraco
            dx = bx - self.x
            dy = by - self.y
            dist_sq = dx*dx + dy*dy
            if RAIO_BURACO**2 < dist_sq < RAIO_ATRACAO_BURACO**2:
                dist = math.sqrt(dist_sq)
                if dist == 0: continue
                nx = dx / dist
                ny = dy / dist
                forca = FORCA_ATRACAO_BURACO
                self.vx += nx * forca
                self.vy += ny * forca
                break

    def colisao_buraco(self, buracos):
        if not self.na_mesa:
            return False
        for buraco in buracos:
            bx, by = buraco
            dx = self.x - bx
            dy = self.y - by
            if dx*dx + dy*dy < RAIO_BURACO**2:
                self.x = bx  # Centraliza a bola no buraco
                self.y = by
                self.na_mesa = False
                self.vx = 0
                self.vy = 0
                return True
        return False

    def colisao_bola(self, outra_bola):
        if not outra_bola.na_mesa or not self.na_mesa or self == outra_bola:
            return False

        dx = self.x - outra_bola.x
        dy = self.y - outra_bola.y
        dist_sq = dx*dx + dy*dy
        raio_total = self.raio + outra_bola.raio

        if dist_sq < raio_total**2:
            dist = math.sqrt(dist_sq)
            if dist == 0:
                dist = 0.001
                nx, ny = 1.0, 0.0
            else:
                nx = dx / dist
                ny = dy / dist

            overlap = (raio_total - dist) * 0.5
            self.x += nx * overlap
            self.y += ny * overlap
            outra_bola.x -= nx * overlap
            outra_bola.y -= ny * overlap

            vx_rel = self.vx - outra_bola.vx
            vy_rel = self.vy - outra_bola.vy
            vel_normal = vx_rel * nx + vy_rel * ny

            if vel_normal > 0:
                return True

            e = 0.9
            j = -(1 + e) * vel_normal
            inv_massa_total = (1 / self.massa) + (1 / outra_bola.massa)
            if inv_massa_total == 0: return True
            j /= inv_massa_total

            self.vx += (j * nx) / self.massa
            self.vy += (j * ny) / self.massa
            outra_bola.vx -= (j * nx) / outra_bola.massa
            outra_bola.vy -= (j * ny) / outra_bola.massa
            return True
        return False

    def desenhar(self, tela):
        if not self.na_mesa:
            return
        pos_int = (int(self.x), int(self.y))
        raio_int = int(self.raio)
        # Desenho sólido da bola
        pygame.draw.circle(tela, self.cor, pos_int, raio_int)
        # Faixa listrada
        if self.listrada and raio_int > 8:
            rect_faixa = pygame.Rect(0, 0, raio_int * 2 - 12, raio_int * 2 - 8)
            rect_faixa.center = pos_int
            pygame.draw.rect(tela, (245, 245, 245), rect_faixa, border_radius=raio_int - 4)
            pygame.draw.circle(tela, self.cor, pos_int, raio_int - 7)
        # Número da bola
        if self.numero > 0:
            font_num = pygame.font.SysFont("Arial", max(raio_int, 12), bold=True)
            num_surf = font_num.render(str(self.numero), True, (0,0,0))
            num_rect = num_surf.get_rect(center=pos_int)
            tela.blit(num_surf, num_rect)

class JogoBilhar:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.estado = MENU
        self.fade_alpha = 0
        self.fading_in = True
        self.fading_out = False
        self.proximo_estado = JOGO

        # Centraliza a mesa para encaixar com a borda.png
        self.x_mesa = MESA_OFFSET_X
        self.y_mesa = MESA_OFFSET_Y

        # Carregar imagens da mesa e borda já no __init__ para uso em todas as telas
        self.img_mesa_feltro = carregar_imagem("mesa.jpg", (LARGURA_MESA, ALTURA_MESA), alpha=True)
        self.img_borda = carregar_imagem("borda.png", (LARGURA_MESA + 40, ALTURA_MESA + 40), alpha=True)

        # Buracos ajustados para ficarem do lado de fora do feltro, alinhados com a borda.png
        offset = 20  # distância do feltro até o centro do buraco
        self.buracos = [
            (self.x_mesa, self.y_mesa),  # canto superior esquerdo
            (self.x_mesa + LARGURA_MESA // 2, self.y_mesa - 5),  # meio superior
            (self.x_mesa + LARGURA_MESA, self.y_mesa),  # canto superior direito
            (self.x_mesa, self.y_mesa + ALTURA_MESA),  # canto inferior esquerdo
            (self.x_mesa + LARGURA_MESA // 2, self.y_mesa + ALTURA_MESA + 5),  # meio inferior
            (self.x_mesa + LARGURA_MESA, self.y_mesa + ALTURA_MESA)  # canto inferior direito
        ]

        # Variável para controlar o tempo de início do jogo (para parar a música do menu)
        self.tempo_inicio_jogo = 0
        self.musica_menu_tocando = False
        self.musica_menu_parada = False

        # Assets (inicializados no reiniciar)
        self.imagem_inicial_bg = None
        self.texto_imagem_inicial = None
        self.texto_imagem_inicial_rect = None
        self.taco_anim_img = None
        self.taco1_rot = None
        self.taco2_rot = None
        self.personagem_mecanico_img = None
        self.personagem_bebendo_img = None
        self.taco_jogo_original = None
        self.chao_bar = None
        self.menu_background = None
        self.menu_overlay = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
        self.sons_tacada = []
        self.sons_acerto = []
        self.som_sequencia = None
        self.som_encacapar = None
        self.som_animacao_tacos = None
        self.som_animacao_tacos_duracao = 0
        
        # Imagem de fundo para a tela de regras
        self.regras_background = None
        self.regras_fade_alpha = 0
        self.regras_fading_in = False

        # Botões
        self.botao_jogar_rect = pygame.Rect(50, 250, 200, 50)
        self.botao_regras_rect = pygame.Rect(50, 320, 200, 50)
        self.botao_sair_rect = pygame.Rect(50, 390, 200, 50)
        self.botao_voltar_rect = pygame.Rect(LARGURA - 250, ALTURA - 80, 200, 50)
        self.botao_doacao_rect = pygame.Rect(50, 460, 200, 50)

        # Buracos
        self.buracos = [
            (self.x_mesa, self.y_mesa),
            (self.x_mesa + LARGURA_MESA // 2, self.y_mesa - 5),
            (self.x_mesa + LARGURA_MESA, self.y_mesa),
            (self.x_mesa, self.y_mesa + ALTURA_MESA),
            (self.x_mesa + LARGURA_MESA // 2, self.y_mesa + ALTURA_MESA + 5),
            (self.x_mesa + LARGURA_MESA, self.y_mesa + ALTURA_MESA)
        ]

        # Variáveis de estado do jogo (resetadas no reiniciar)
        self.bolas = []
        self.bola_branca = None
        self.jogador_atual = 1
        self.jogador1_tipo = None
        self.jogador2_tipo = None
        self.puxando_estilingue = False
        self.pos_inicial_puxada_estilingue = None
        self.distancia_puxada_estilingue = 0.0
        self.angulo_tacada = 0.0
        self.todas_paradas = True
        self.bola_branca_encacapada = False
        self.bola_8_encacapada = False
        self.vencedor = 0
        self.mensagem = ""
        self.tempo_mensagem = 0
        self.primeira_tacada = False
        self.falta_na_tacada = False
        self.bolas_encacapadas_na_tacada = []
        
        # Contador para verificar se o jogo está travado
        self.contador_verificacao_travamento = 0
        self.ultima_verificacao_estado = None

        # Variáveis de animação e estado inicial
        self.tempo_inicio_imagem_inicial = 0
        self.fading_out_imagem_inicial = False
        self.fade_alpha_imagem_inicial = 255
        self.animacao_tacos_iniciada = False
        self.tempo_inicio_anim_tacos = 0
        self.taco1_pos = pygame.Vector2(0,0)
        self.taco2_pos = pygame.Vector2(0,0)
        self.taco1_rect = None
        self.taco2_rect = None
        self.taco1_alvo_x = 0
        self.taco2_alvo_x = 0
        self.animacao_tacos_completa = False
        self.mecanico_pos = pygame.Vector2(0,0)
        self.bebendo_pos = pygame.Vector2(0,0)
        self.mecanico_rect = None
        self.bebendo_rect = None
        self.mecanico_alvo = pygame.Vector2(0,0)
        self.bebendo_alvo = pygame.Vector2(0,0)
        self.personagens_atingiram_alvo = False
        self.volume_musica_reduzido = False
        self.tempo_inicio_som_anim = 0
        self.som_animacao_tacos_tocado = False
        self.musica_iniciada = False

        # Garante que textura_mesa sempre existe, mesmo que não seja usada
        self.textura_mesa = None

        self.reiniciar()

    def reiniciar(self):
        print("Reiniciando Jogo...")
        # Carregar Assets
        self.chao_bar = carregar_imagem("Cenadebarcomdetalhesdepiso.png", (LARGURA, ALTURA))
        self.menu_background = carregar_imagem("menu_background_edited.png", (LARGURA, ALTURA), alpha=True)
        self.imagem_inicial_bg = carregar_imagem("ChatGPTImage5dejun.de2025,13_33_29.png", (LARGURA, ALTURA))
        self.texto_imagem_inicial = fonte_grande.render("sinuca delicia", True, COR_BRANCA)
        self.texto_imagem_inicial_rect = self.texto_imagem_inicial.get_rect(center=(LARGURA // 2, ALTURA // 2))
        
        # Carregar imagem de fundo para a tela de regras
        self.regras_background = carregar_imagem("regras_sinuca.jpg", (LARGURA, ALTURA))
        
        self.taco_anim_img = carregar_imagem("taco_animacao.png", alpha=True)
        if self.taco_anim_img:
            taco_altura_original = self.taco_anim_img.get_height()
            taco_largura_original = self.taco_anim_img.get_width()
            if taco_largura_original > 0:
                fator_escala_taco_anim = ALTURA_MESA * 0.8 / taco_largura_original
                self.taco_anim_img = pygame.transform.scale(self.taco_anim_img, (int(taco_largura_original * fator_escala_taco_anim), int(taco_altura_original * fator_escala_taco_anim)))
                self.taco1_rot = pygame.transform.rotate(self.taco_anim_img, 90)
                self.taco2_rot = pygame.transform.rotate(self.taco_anim_img, 90)
            else:
                print("Aviso: Imagem do taco de animação com largura zero.")
                self.taco_anim_img = None # Invalida a imagem

        self.personagem_mecanico_img = carregar_imagem("personagem_mecanico.png", alpha=True)
        self.personagem_bebendo_img = carregar_imagem("personagem_bebendo.png", alpha=True)
        if self.personagem_mecanico_img and self.personagem_bebendo_img:
            escala_personagem = 0.15
            if self.personagem_mecanico_img.get_width() > 0 and self.personagem_bebendo_img.get_width() > 0:
                self.personagem_mecanico_img = pygame.transform.scale(self.personagem_mecanico_img, (int(self.personagem_mecanico_img.get_width() * escala_personagem), int(self.personagem_mecanico_img.get_height() * escala_personagem)))
                self.personagem_bebendo_img = pygame.transform.scale(self.personagem_bebendo_img, (int(self.personagem_bebendo_img.get_width() * escala_personagem), int(self.personagem_bebendo_img.get_height() * escala_personagem)))
            else:
                 print("Aviso: Imagem de personagem com largura zero.")
                 self.personagem_mecanico_img = None
                 self.personagem_bebendo_img = None

        self.taco_jogo_original = carregar_imagem("taco_jogo.png", alpha=True)
        if self.taco_jogo_original:
            taco_altura_original = self.taco_jogo_original.get_height()
            taco_largura_original = self.taco_jogo_original.get_width()
            if taco_largura_original > 0:
                fator_escala_taco = 200 / taco_largura_original
                self.taco_jogo_original = pygame.transform.scale(self.taco_jogo_original, (int(taco_largura_original * fator_escala_taco), int(taco_altura_original * fator_escala_taco)))
            else:
                print("Aviso: Imagem do taco de jogo com largura zero.")
                self.taco_jogo_original = None # Invalida a imagem

        # Carregar sons
        self.sons_tacada = [
            carregar_som("forceful-hit-sound.mp3"),
            carregar_som("metal-pipe-go-bonk.mp3")
        ]
        self.sons_acerto = [
            carregar_som("bonk_BEtiM8g.mp3"),
            carregar_som("yuri22-niceeeeee-krl.mp3")
        ]
        self.som_encacapar = carregar_som("pai-de-familia-delicia-cara.mp3")
        self.som_animacao_tacos = carregar_som("era-essa-peca_novo.mp3")
        if self.som_animacao_tacos:
            self.som_animacao_tacos_duracao = int(self.som_animacao_tacos.get_length() * 1000)
        else:
            self.som_animacao_tacos_duracao = 2000 # Fallback

        # Inicializar bolas
        self.bolas = []
        self.bola_branca = Bola(self.x_mesa + LARGURA_MESA // 4, self.y_mesa + ALTURA_MESA // 2, COR_BRANCA, False, 0)
        self.bolas.append(self.bola_branca)

        # Criar bolas coloridas
        bolas_triangulo = [
            Bola(0, 0, CORES_BOLAS[1], False, 1),
            Bola(0, 0, CORES_BOLAS[9], True, 9),
            Bola(0, 0, CORES_BOLAS[2], False, 2),
            Bola(0, 0, CORES_BOLAS[10], True, 10),
            Bola(0, 0, CORES_BOLAS[8], False, 8),
            Bola(0, 0, CORES_BOLAS[11], True, 11),
            Bola(0, 0, CORES_BOLAS[3], False, 3),
            Bola(0, 0, CORES_BOLAS[12], True, 12),
            Bola(0, 0, CORES_BOLAS[4], False, 4),
            Bola(0, 0, CORES_BOLAS[13], True, 13),
            Bola(0, 0, CORES_BOLAS[5], False, 5),
            Bola(0, 0, CORES_BOLAS[14], True, 14),
            Bola(0, 0, CORES_BOLAS[6], False, 6),
            Bola(0, 0, CORES_BOLAS[15], True, 15),
            Bola(0, 0, CORES_BOLAS[7], False, 7)
        ]

        # Posicionar bolas em triângulo
        x_foot_spot = self.x_mesa + LARGURA_MESA * 3 // 4
        y_foot_spot = self.y_mesa + ALTURA_MESA // 2
        dist_h = RAIO_BOLA * 2 + 1.0
        dist_v = RAIO_BOLA * math.sqrt(3) + 1.0
        idx_bola_lista = 0
        current_col = 0
        balls_in_col = 1
        col_x = x_foot_spot

        for i in range(15):
            bola_atual = bolas_triangulo[i]
            if bola_atual:
                start_y_col = y_foot_spot - (balls_in_col - 1) * RAIO_BOLA
                pos_y = start_y_col + (idx_bola_lista % balls_in_col) * dist_h
                pos_x = col_x
                bola_atual.x = pos_x
                bola_atual.y = pos_y
                bola_atual.vx = 0
                bola_atual.vy = 0
                bola_atual.na_mesa = True
                self.bolas.append(bola_atual)

            idx_bola_lista += 1
            if idx_bola_lista == sum(range(1, balls_in_col + 1)):
                current_col += 1
                balls_in_col += 1
                col_x += dist_v

        # Resetar variáveis de jogo
        self.jogador_atual = 1
        self.jogador1_tipo = None
        self.jogador2_tipo = None
        self.puxando_estilingue = False
        self.pos_inicial_puxada_estilingue = None
        self.distancia_puxada_estilingue = 0.0
        self.angulo_tacada = 0.0
        self.todas_paradas = True
        self.bola_branca_encacapada = False
        self.bola_8_encacapada = False
        self.vencedor = 0
        self.mensagem = ""
        self.tempo_mensagem = 0
        self.primeira_tacada = False
        self.falta_na_tacada = False
        self.bolas_encacapadas_na_tacada = []
        
        # Resetar contador de verificação de travamento
        self.contador_verificacao_travamento = 0
        self.ultima_verificacao_estado = None

        # Resetar animação
        self.tempo_inicio_imagem_inicial = 0
        self.fading_out_imagem_inicial = False
        self.fade_alpha_imagem_inicial = 255
        self.animacao_tacos_iniciada = False
        self.tempo_inicio_anim_tacos = 0
        self.taco1_pos = pygame.Vector2(LARGURA // 2, ALTURA // 2)
        self.taco2_pos = pygame.Vector2(LARGURA // 2, ALTURA // 2)
        self.taco1_rect = None
        self.taco2_rect = None
        self.taco1_alvo_x = 0
        self.taco2_alvo_x = 0
        self.animacao_tacos_completa = False
        self.mecanico_pos = pygame.Vector2(LARGURA // 2 - 50, ALTURA // 2)
        self.bebendo_pos = pygame.Vector2(LARGURA // 2 + 50, ALTURA // 2)
        if self.personagem_mecanico_img: self.mecanico_rect = self.personagem_mecanico_img.get_rect(center=self.mecanico_pos)
        if self.personagem_bebendo_img: self.bebendo_rect = self.personagem_bebendo_img.get_rect(center=self.bebendo_pos)
        offset_canto = 30
        self.mecanico_alvo = pygame.Vector2(self.x_mesa + offset_canto, self.y_mesa + offset_canto)
        self.bebendo_alvo = pygame.Vector2(self.x_mesa + LARGURA_MESA - offset_canto, self.y_mesa + ALTURA_MESA - offset_canto)
        self.personagens_atingiram_alvo = False
        self.volume_musica_reduzido = False
        self.tempo_inicio_som_anim = 0
        self.som_animacao_tacos_tocado = False
        self.musica_iniciada = False
        self.estado = MENU
        self.fading_in = True
        self.fade_alpha = 0
        
        # Resetar variáveis de música do menu
        self.tempo_inicio_jogo = 0
        self.musica_menu_tocando = False
        self.musica_menu_parada = False
        
        # Iniciar música do menu
        if audio_enabled:
            try:
                pygame.mixer.music.stop()
                carregar_musica("musica_menu.mp3")
                pygame.mixer.music.play(-1)
                self.musica_menu_tocando = True
            except Exception as e:
                print(f"Erro ao tocar música do menu: {e}")

    def processar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if self.estado == MENU:
                if self.fading_in or self.fading_out: continue
                
                # Verificar hover nos botões para efeito visual
                mouse_pos = pygame.mouse.get_pos()
                botao_jogar_hover = self.botao_jogar_rect.collidepoint(mouse_pos)
                botao_regras_hover = self.botao_regras_rect.collidepoint(mouse_pos)
                botao_sair_hover = self.botao_sair_rect.collidepoint(mouse_pos)
                botao_doacao_hover = self.botao_doacao_rect.collidepoint(mouse_pos)
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.botao_jogar_rect.collidepoint(event.pos):
                        print("Botão Jogar")
                        self.tempo_inicio_jogo = pygame.time.get_ticks()
                        if audio_enabled:
                            try:
                                # A música do menu será parada após 1 segundo no método atualizar
                                carregar_musica("Promotech.mp3")
                            except Exception as e:
                                print(f"Erro ao carregar música: {e}")
                        self.fading_out = True
                        self.proximo_estado = MOSTRAR_IMAGEM_INICIAL
                    elif self.botao_regras_rect.collidepoint(event.pos):
                        print("Botão Regras")
                        self.estado = REGRAS
                        self.regras_fade_alpha = 0
                        self.regras_fading_in = True
                    elif self.botao_sair_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                    elif self.botao_doacao_rect.collidepoint(event.pos):
                        print("Botão Doação")
                        self.estado = DOACAO
            
            elif self.estado == REGRAS:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.botao_voltar_rect.collidepoint(event.pos):
                        print("Botão Voltar das Regras")
                        self.estado = MENU

            elif self.estado == JOGO:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.estado = PAUSA
                    # Tecla para forçar verificação de estado (debug)
                    elif event.key == pygame.K_v:
                        self.verificar_estado_jogo()

                if self.todas_paradas and not self.bola_branca_encacapada and self.bola_branca and self.bola_branca.na_mesa:
                    mouse_pos = pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        dist_sq_clique = (mouse_pos[0] - self.bola_branca.x)**2 + (mouse_pos[1] - self.bola_branca.y)**2
                        if dist_sq_clique < (RAIO_BOLA * 3)**2:
                            self.puxando_estilingue = True
                            self.pos_inicial_puxada_estilingue = pygame.Vector2(self.bola_branca.x, self.bola_branca.y)
                            self.distancia_puxada_estilingue = 0.0
                        else:
                             dx = mouse_pos[0] - self.bola_branca.x
                             dy = mouse_pos[1] - self.bola_branca.y
                             if dx != 0 or dy != 0:
                                 self.angulo_tacada = math.atan2(dy, dx)

                    elif event.type == pygame.MOUSEMOTION:
                        if self.puxando_estilingue and self.pos_inicial_puxada_estilingue:
                            pos_atual_mouse = pygame.Vector2(mouse_pos)
                            vetor_puxada = pos_atual_mouse - self.pos_inicial_puxada_estilingue
                            self.distancia_puxada_estilingue = min(vetor_puxada.length(), LIMITE_PUXADA_ESTILINGUE)
                            if vetor_puxada.length() > 0:
                                # Invertendo a direção do ângulo para corrigir a orientação do taco
                                self.angulo_tacada = math.atan2(-vetor_puxada.y, -vetor_puxada.x)
                        else:
                            dx = mouse_pos[0] - self.bola_branca.x
                            dy = mouse_pos[1] - self.bola_branca.y
                            if dx != 0 or dy != 0:
                                self.angulo_tacada = math.atan2(dy, dx)

                    elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        if self.puxando_estilingue:
                            self.puxando_estilingue = False
                            if self.distancia_puxada_estilingue > 5:
                                self.dar_tacada()
                            self.pos_inicial_puxada_estilingue = None
                            self.distancia_puxada_estilingue = 0.0

            elif self.estado == PAUSA:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.estado = JOGO
                    elif event.key == pygame.K_m:
                        self.reiniciar()

            elif self.estado == REPOSICIONAR:
                 if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if self.posicao_valida_reposicionar(mouse_x, mouse_y):
                        if self.bola_branca:
                            self.bola_branca.x = mouse_x
                            self.bola_branca.y = mouse_y
                            self.bola_branca.vx = 0
                            self.bola_branca.vy = 0
                            self.bola_branca.na_mesa = True
                        self.bola_branca_encacapada = False
                        self.estado = JOGO
                        self.todas_paradas = True
                        self.mensagem = ""
                        self.trocar_jogador() # Falta sempre troca o turno
                        print("[DEBUG] Bola branca reposicionada, voltando para JOGO")
                    else:
                        self.mensagem = "Posição inválida!"
                        self.tempo_mensagem = 60

            elif self.estado == FIM_JOGO:
                 if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.reiniciar()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

            elif self.estado == DOACAO:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.botao_voltar_rect.collidepoint(event.pos):
                        self.estado = MENU

    def atualizar(self):
        current_time = pygame.time.get_ticks()
        
        # Verificar se o jogo está travado
        if self.estado == JOGO:
            estado_atual = (self.todas_paradas, self.bola_branca_encacapada, 
                           self.jogador_atual, self.estado)
            
            if estado_atual == self.ultima_verificacao_estado:
                self.contador_verificacao_travamento += 1
                if self.contador_verificacao_travamento > 600:  # 10 segundos a 60 FPS
                    print("[WARN] Possível travamento detectado, forçando verificação de estado")
                    self.verificar_estado_jogo()
                    self.contador_verificacao_travamento = 0
            else:
                self.ultima_verificacao_estado = estado_atual
                self.contador_verificacao_travamento = 0
        
        # Controle da música do menu
        if self.tempo_inicio_jogo > 0 and not self.musica_menu_parada and self.musica_menu_tocando:
            if current_time - self.tempo_inicio_jogo >= DELAY_MUSICA_JOGO:
                if audio_enabled:
                    try:
                        pygame.mixer.music.stop()
                        self.musica_menu_parada = True
                        pygame.mixer.music.play(-1)
                        self.musica_iniciada = True
                    except Exception as e:
                        print(f"Erro ao parar música do menu: {e}")

        # Lógica de Fade Global
        if self.fading_in:
            self.fade_alpha += FADE_SPEED
            if self.fade_alpha >= 255:
                self.fade_alpha = 255
                self.fading_in = False
            return
        if self.fading_out:
            self.fade_alpha -= FADE_SPEED
            if self.fade_alpha <= 0:
                self.fade_alpha = 0
                self.fading_out = False
                self.estado = self.proximo_estado
                self.fading_in = True
                if self.estado == MOSTRAR_IMAGEM_INICIAL:
                    self.tempo_inicio_imagem_inicial = current_time
                    self.fade_alpha_imagem_inicial = 255
                    self.fading_out_imagem_inicial = False
                elif self.estado == ANIMACAO_TACOS:
                    self.tempo_inicio_anim_tacos = current_time
                    self.animacao_tacos_iniciada = False
                    self.som_animacao_tacos_tocado = False
                    self.animacao_tacos_completa = False
                    self.personagens_atingiram_alvo = False
                    # Resetar posições visuais
                    self.taco1_pos = pygame.Vector2(LARGURA // 2, ALTURA // 2)
                    self.taco2_pos = pygame.Vector2(LARGURA // 2, ALTURA // 2)
                    if self.taco1_rot and self.taco1_rect: self.taco1_rect.center = self.taco1_pos
                    if self.taco2_rot and self.taco2_rect: self.taco2_rect.center = self.taco2_pos
                    self.mecanico_pos = pygame.Vector2(LARGURA // 2 - 50, ALTURA // 2)
                    self.bebendo_pos = pygame.Vector2(LARGURA // 2 + 50, ALTURA // 2)
                    if self.personagem_mecanico_img and self.mecanico_rect: self.mecanico_rect.center = self.mecanico_pos
                    if self.personagem_bebendo_img and self.bebendo_rect: self.bebendo_rect.center = self.bebendo_pos
            return
            
        # Fade da tela de regras
        if self.estado == REGRAS and self.regras_fading_in:
            self.regras_fade_alpha += FADE_SPEED
            if self.regras_fade_alpha >= 255:
                self.regras_fade_alpha = 255
                self.regras_fading_in = False

        # Atualização por Estado
        if self.estado == MOSTRAR_IMAGEM_INICIAL:
            if self.tempo_inicio_imagem_inicial == 0:
                 self.tempo_inicio_imagem_inicial = current_time

            tempo_decorrido = current_time - self.tempo_inicio_imagem_inicial
            if not self.fading_out_imagem_inicial and tempo_decorrido >= DURACAO_IMAGEM_INICIAL:
                self.fading_out_imagem_inicial = True

            if self.fading_out_imagem_inicial:
                self.fade_alpha_imagem_inicial -= FADE_SPEED * 1
                if self.fade_alpha_imagem_inicial <= 0:
                    self.fade_alpha_imagem_inicial = 0
                    self.estado = ANIMACAO_TACOS
                    # Resetar timers para o próximo estado
                    self.tempo_inicio_anim_tacos = current_time
                    self.animacao_tacos_iniciada = False
                    self.som_animacao_tacos_tocado = False
                    self.animacao_tacos_completa = False
                    self.personagens_atingiram_alvo = False
                    # Resetar posições visuais
                    self.taco1_pos = pygame.Vector2(LARGURA // 2, ALTURA // 2)
                    self.taco2_pos = pygame.Vector2(LARGURA // 2, ALTURA // 2)
                    if self.taco1_rot and self.taco1_rect: self.taco1_rect.center = self.taco1_pos
                    if self.taco2_rot and self.taco2_rect: self.taco2_rect.center = self.taco2_pos
                    self.mecanico_pos = pygame.Vector2(LARGURA // 2 - 50, ALTURA // 2)
                    self.bebendo_pos = pygame.Vector2(LARGURA // 2 + 50, ALTURA // 2)
                    if self.personagem_mecanico_img and self.mecanico_rect: self.mecanico_rect.center = self.mecanico_pos
                    if self.personagem_bebendo_img and self.bebendo_rect: self.bebendo_rect.center = self.bebendo_pos

        elif self.estado == ANIMACAO_TACOS:
            if not self.animacao_tacos_iniciada and current_time >= self.tempo_inicio_anim_tacos + ANIM_TACOS_DELAY:
                self.animacao_tacos_iniciada = True
                # Não resetar tempo_inicio_som_anim aqui, ele é relativo ao inicio da animação visual

            if self.animacao_tacos_iniciada:
                # Tocar som após DELAY_SOM_ANIM do início da animação visual
                if audio_enabled and self.som_animacao_tacos and not self.som_animacao_tacos_tocado and \
                   current_time >= self.tempo_inicio_anim_tacos + ANIM_TACOS_DELAY + DELAY_SOM_ANIM:
                    if self.musica_iniciada:
                        try:
                            pygame.mixer.music.set_volume(0.15) # Reduz volume da música
                            self.volume_musica_reduzido = True
                        except Exception as e: print(f"Erro ao reduzir volume: {e}")
                    try:
                        self.som_animacao_tacos.play()
                        self.som_animacao_tacos_tocado = True
                        self.tempo_inicio_som_anim = current_time # Marca quando o som começou a tocar
                    except Exception as e: print(f"Erro ao tocar som anim: {e}")

                # Mover Tacos
                atingiu_taco1, atingiu_taco2 = False, False
                if self.taco1_rect and self.taco1_pos.x > self.taco1_alvo_x:
                    self.taco1_pos.x -= ANIM_TACOS_SPEED
                    self.taco1_rect.centerx = int(self.taco1_pos.x)
                else: atingiu_taco1 = True
                if self.taco2_rect and self.taco2_pos.x < self.taco2_alvo_x:
                    self.taco2_pos.x += ANIM_TACOS_SPEED
                    self.taco2_rect.centerx = int(self.taco2_pos.x)
                else: atingiu_taco2 = True
                if atingiu_taco1 and atingiu_taco2: self.animacao_tacos_completa = True

                # Mover Personagens
                atingiu_mecanico, atingiu_bebendo = False, False
                PERSONAGEM_SPEED = ANIM_TACOS_SPEED * 0.8
                if self.mecanico_rect and self.mecanico_pos.distance_to(self.mecanico_alvo) > PERSONAGEM_SPEED:
                    try:
                        direction = (self.mecanico_alvo - self.mecanico_pos).normalize()
                        self.mecanico_pos += direction * PERSONAGEM_SPEED
                        self.mecanico_rect.center = self.mecanico_pos
                    except ValueError: atingiu_mecanico = True # Se normalize falhar (vetor zero)
                else: atingiu_mecanico = True
                if self.bebendo_rect and self.bebendo_pos.distance_to(self.bebendo_alvo) > PERSONAGEM_SPEED:
                    try:
                        direction = (self.bebendo_alvo - self.bebendo_pos).normalize()
                        self.bebendo_pos += direction * PERSONAGEM_SPEED
                        self.bebendo_rect.center = self.bebendo_pos
                    except ValueError: atingiu_bebendo = True
                else: atingiu_bebendo = True
                if atingiu_mecanico and atingiu_bebendo: self.personagens_atingiram_alvo = True

                # Verificar se o som terminou
                som_terminou = False
                if not self.som_animacao_tacos_tocado:
                    som_terminou = True # Se não tocou, considera terminado
                elif current_time - self.tempo_inicio_som_anim > self.som_animacao_tacos_duracao:
                    som_terminou = True

                # Restaurar volume da música após o som terminar
                if som_terminou and self.volume_musica_reduzido and self.musica_iniciada:
                    try:
                        pygame.mixer.music.set_volume(0.5)
                        self.volume_musica_reduzido = False
                    except Exception as e: print(f"Erro ao restaurar volume: {e}")

                # Verificar se a animação completa terminou
                if self.animacao_tacos_completa and self.personagens_atingiram_alvo and som_terminou:
                    self.estado = JOGO
                    print("[DEBUG] Animação completa, iniciando jogo")

        elif self.estado == JOGO:
            # Atualizar tempo da mensagem
            if self.tempo_mensagem > 0:
                self.tempo_mensagem -= 1

            # Verificar se todas as bolas estão paradas
            todas_paradas_anterior = self.todas_paradas
            self.todas_paradas = True
            for bola in self.bolas:
                if bola.na_mesa and (bola.vx != 0 or bola.vy != 0):
                    self.todas_paradas = False
                    break

            # Se as bolas acabaram de parar, verificar encaçapamentos e turnos
            if self.todas_paradas and not todas_paradas_anterior:
                print("[DEBUG] Todas as bolas pararam, verificando estado do jogo")
                self.verificar_troca_turno()

            # Atualizar física das bolas
            if not self.todas_paradas:
                # Mover bolas
                for bola in self.bolas:
                    bola.mover()

                # Verificar colisões com paredes
                for bola in self.bolas:
                    bola.colisao_parede(self.x_mesa, self.y_mesa, self.x_mesa + LARGURA_MESA, self.y_mesa + ALTURA_MESA)

                # Aplicar atração dos buracos
                for bola in self.bolas:
                    bola.aplicar_atracao_buraco(self.buracos)

                # Verificar colisões entre bolas
                for i in range(len(self.bolas)):
                    for j in range(i+1, len(self.bolas)):
                        self.bolas[i].colisao_bola(self.bolas[j])

                # Verificar encaçapamentos e remover bolas encaçapadas
                bolas_para_remover = []
                for bola in self.bolas:
                    if bola.colisao_buraco(self.buracos):
                        print(f"[DEBUG] Bola {bola.numero} encaçapada")
                        if bola != self.bola_branca:
                            self.bolas_encacapadas_na_tacada.append(bola)
                        self.bola_encacapada(bola)
                        if bola != self.bola_branca:
                            bolas_para_remover.append(bola)
                # Remove bolas encaçapadas da lista principal (exceto branca, que é tratada em REPOSICIONAR)
                self.bolas = [b for b in self.bolas if b.na_mesa or b == self.bola_branca]

    def verificar_estado_jogo(self):
        """Verifica e corrige possíveis estados inconsistentes do jogo"""
        print("[DEBUG] Verificando estado do jogo...")
        
        # Verificar se a bola branca está na mesa
        if self.bola_branca and not self.bola_branca.na_mesa and not self.bola_branca_encacapada:
            print("[WARN] Bola branca não está na mesa mas não foi marcada como encaçapada")
            self.bola_branca_encacapada = True
            self.estado = REPOSICIONAR
            self.mensagem = "Reposicione a bola branca."
            self.tempo_mensagem = 120
            return
            
        # Verificar se todas as bolas estão realmente paradas
        alguma_em_movimento = False
        for bola in self.bolas:
            if bola.na_mesa and (abs(bola.vx) > 0.01 or abs(bola.vy) > 0.01):
                alguma_em_movimento = True
                break
                
        if alguma_em_movimento and self.todas_paradas:
            print("[WARN] Detectadas bolas em movimento mas todas_paradas=True")
            self.todas_paradas = False
        elif not alguma_em_movimento and not self.todas_paradas:
            print("[WARN] Todas as bolas paradas mas todas_paradas=False")
            self.todas_paradas = True
            self.verificar_troca_turno()
            
        # Verificar se o jogo está no estado correto
        if self.bola_branca_encacapada and self.estado != REPOSICIONAR:
            print("[WARN] Bola branca encaçapada mas estado não é REPOSICIONAR")
            self.estado = REPOSICIONAR
            self.mensagem = "Reposicione a bola branca."
            self.tempo_mensagem = 120
            
        # Verificar se a bola 8 foi encaçapada
        if self.bola_8_encacapada and self.estado != FIM_JOGO:
            print("[WARN] Bola 8 encaçapada mas estado não é FIM_JOGO")
            self.estado = FIM_JOGO
            
        print("[DEBUG] Verificação de estado concluída")

    def desenhar(self):
        if self.estado == MENU:
            self.desenhar_menu()
        elif self.estado == REGRAS:
            self.desenhar_regras()
        elif self.estado == MOSTRAR_IMAGEM_INICIAL:
            self.desenhar_imagem_inicial()
        elif self.estado == ANIMACAO_TACOS:
            self.desenhar_animacao_tacos()
        elif self.estado == JOGO:
            self.desenhar_jogo()
        elif self.estado == PAUSA:
            self.desenhar_pausa()
        elif self.estado == REPOSICIONAR:
            self.desenhar_reposicionar()
        elif self.estado == FIM_JOGO:
            self.desenhar_fim_jogo()
        elif self.estado == DOACAO:
            self.desenhar_doacao()

        # Aplicar fade global
        if self.fading_in or self.fading_out:
            fade_surf = pygame.Surface((self.largura, self.altura), pygame.SRCALPHA)
            fade_surf.fill((0, 0, 0, 255 - self.fade_alpha))
            tela.blit(fade_surf, (0, 0))

    def desenhar_menu(self):
        # Desenhar fundo
        if self.menu_background:
            tela.blit(self.menu_background, (0, 0))
        else:
            tela.fill(COR_FUNDO)

        # Título com efeito neon e sombra
        titulo_texto = "SINUCA DELÍCIA"
        fonte_titulo = pygame.font.SysFont("Arial Black", max(60, LARGURA // 12), bold=True)
        titulo = fonte_titulo.render(titulo_texto, True, (0, 255, 180))
        titulo_sombra = fonte_titulo.render(titulo_texto, True, (0, 0, 0))
        glow = pygame.Surface(titulo.get_size(), pygame.SRCALPHA)
        for i in range(1, 8):
            pygame.draw.rect(glow, (0, 255, 180, 18), glow.get_rect(), border_radius=30+i*2)
        titulo_rect = titulo.get_rect(center=(self.largura // 2, 120))
        tela.blit(titulo_sombra, (titulo_rect.x + 5, titulo_rect.y + 5))
        tela.blit(glow, titulo_rect)
        tela.blit(titulo, titulo_rect)

        # Botões
        mouse_pos = pygame.mouse.get_pos()
        botoes = [
            (self.botao_jogar_rect, "JOGAR"),
            (self.botao_regras_rect, "REGRAS"),
            (self.botao_sair_rect, "SAIR"),
<<<<<<< HEAD
            (self.botao_doacao_rect, "DOAÇÃO"),
=======
            (self.botao_doacao_rect, "SOBRE"),
>>>>>>> d302c89 (Primeiro commit do projeto Sinuca Delícia)
        ]
        for rect, texto in botoes:
            hover = rect.collidepoint(mouse_pos)
            cor_botao = COR_BOTAO_HOVER if hover else COR_BOTAO

            # Sombra do botão
            sombra_rect = rect.move(4, 4)
            pygame.draw.rect(tela, (30, 30, 30), sombra_rect, border_radius=18)

            # Gradiente simples (brilho no topo)
            grad = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
            for y in range(rect.height):
                alpha = 60 if y < rect.height // 2 else 0
                pygame.draw.line(grad, (255, 255, 255, alpha), (0, y), (rect.width, y))
            pygame.draw.rect(tela, cor_botao, rect, border_radius=18)
            tela.blit(grad, rect.topleft)

            # Borda
            pygame.draw.rect(tela, COR_TEXTO, rect, 3, border_radius=18)

            # Texto centralizado com sombra
            fonte_btn = pygame.font.SysFont("Arial", 30, bold=True)
            texto_surf = fonte_btn.render(texto, True, COR_TEXTO)
            texto_sombra = fonte_btn.render(texto, True, (0, 0, 0))
            texto_rect = texto_surf.get_rect(center=rect.center)
            tela.blit(texto_sombra, (texto_rect.x + 2, texto_rect.y + 2))
            tela.blit(texto_surf, texto_rect)

        # Fade global (já existente)
        if self.fading_in or self.fading_out:
            fade_surf = pygame.Surface((self.largura, self.altura), pygame.SRCALPHA)
            fade_surf.fill((0, 0, 0, 255 - self.fade_alpha))
            tela.blit(fade_surf, (0, 0))

    def desenhar_regras(self, sem_fundo=False):
        # Desenhar fundo animado com regras.gif se disponível
        if not sem_fundo and hasattr(self, 'regras_gif_frames') and self.regras_gif_frames:
            now = pygame.time.get_ticks()
            frame_idx = (now // 16) % self.regras_gif_total
            frame = pygame.transform.scale(self.regras_gif_frames[frame_idx], (LARGURA, ALTURA))
            tela.blit(frame, (0, 0))
            # Overlay escuro transparente para facilitar leitura
            overlay = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 120))
            tela.blit(overlay, (0, 0))
        elif not sem_fundo and self.regras_background:
            fundo_transparente = self.regras_background.copy()
            overlay = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            fundo_transparente.blit(overlay, (0, 0))
            tela.blit(fundo_transparente, (0, 0))
        else:
            tela.fill(COR_FUNDO)

        # Título
        titulo = fonte_grande.render("REGRAS DO JOGO", True, COR_TEXTO)
        titulo_rect = titulo.get_rect(center=(self.largura // 2, 50))
        tela.blit(titulo, titulo_rect)

        # Regras do jogo com fundo escuro para melhor legibilidade
        regras = [
            "OBJETIVO: Encaçapar todas as suas bolas (lisas ou listradas) e por último a bola 8.",
            "",
            "REGRAS BÁSICAS:",
            "- O primeiro jogador que encaçapara uma bola define seu tipo (lisas ou listradas).",
            "- O outro jogador fica com o tipo restante.",
            "- Encaçapar a bola branca é falta e o adversário reposiciona a bola.",
            "- Encaçapar a bola 8 antes de todas as suas bolas resulta em derrota.",
            "- Encaçapar a bola 8 após todas as suas bolas resulta em vitória.",
            "- Após encaçapara uma bola do seu tipo, você continua jogando.",
            "- Se não encaçapara nenhuma bola ou encaçapara do adversário, passa a vez.",
            "",
            "CONTROLES:",
            "- Clique perto da bola branca e arraste para trás para definir força e direção.",
            "- Solte o botão para dar a tacada.",
            "- Pressione P para pausar o jogo."
        ]

        y_pos = 120
        for linha in regras:
            if linha:
                texto = fonte_media.render(linha, True, COR_TEXTO)
                texto_rect = texto.get_rect(left=60, top=y_pos)
                # Fundo escuro mais transparente para o texto
                padding = 5
                fundo_rect = texto_rect.inflate(padding * 2, padding * 2)
                fundo_surf = pygame.Surface((fundo_rect.width, fundo_rect.height), pygame.SRCALPHA)
                fundo_surf.fill((0, 0, 0, 100))  # Fundo preto mais transparente
                tela.blit(fundo_surf, fundo_rect)
                tela.blit(texto, texto_rect)
            y_pos += 30

        # Botão Voltar
        mouse_pos = pygame.mouse.get_pos()
        botao_voltar_hover = self.botao_voltar_rect.collidepoint(mouse_pos)
        cor_botao_voltar = COR_BOTAO_HOVER if botao_voltar_hover else COR_BOTAO
        pygame.draw.rect(tela, cor_botao_voltar, self.botao_voltar_rect, border_radius=10)
        pygame.draw.rect(tela, COR_TEXTO, self.botao_voltar_rect, 2, border_radius=10)
        texto_voltar = fonte_media.render("VOLTAR", True, COR_TEXTO)
        texto_voltar_rect = texto_voltar.get_rect(center=self.botao_voltar_rect.center)
        tela.blit(texto_voltar, texto_voltar_rect)

        # Aplicar fade-in
        if self.regras_fading_in:
            fade_surf = pygame.Surface((self.largura, self.altura), pygame.SRCALPHA)
            fade_surf.fill((0, 0, 0, 255 - self.regras_fade_alpha))
            tela.blit(fade_surf, (0, 0))

    def desenhar_imagem_inicial(self):
<<<<<<< HEAD
        if self.imagem_inicial_bg:
            tela.blit(self.imagem_inicial_bg, (0, 0))
        else:
            tela.fill(COR_FUNDO)

        # Título centralizado com efeito neon durante a transição
        alpha = int(self.fade_alpha_imagem_inicial)
        fonte_titulo = pygame.font.SysFont("Arial Black", max(60, LARGURA // 12), bold=True)
        texto = "SINUCA DELÍCIA"
        titulo = fonte_titulo.render(texto, True, (0, 255, 180))
        glow = pygame.Surface(titulo.get_size(), pygame.SRCALPHA)
        for i in range(1, 10):
            pygame.draw.rect(glow, (0, 255, 180, 15), glow.get_rect(), border_radius=30+i*2)
        titulo_rect = titulo.get_rect(center=(self.largura // 2, self.altura // 2))
        # Sombra
        tela.blit(titulo, (titulo_rect.x + 6, titulo_rect.y + 6))
        # Glow
        tela.blit(glow, titulo_rect)
        # Texto principal
        tela.blit(titulo, titulo_rect)

        # Fade-out
        if self.fading_out_imagem_inicial:
            fade_surf = pygame.Surface((self.largura, self.altura), pygame.SRCALPHA)
            fade_surf.fill((0, 0, 0, 255 - alpha))
=======
        # Exibe a imagem de transição correta na tela de carregamento
        try:
            img_path = os.path.join(assets_dir, "da4e9168-ee9e-4475-81a5-38f7b30c0425 (1).png")
            if os.path.exists(img_path):
                img = pygame.image.load(img_path).convert_alpha()
                img = pygame.transform.scale(img, (self.largura, self.altura))
                tela.blit(img, (0, 0))
            else:
                tela.fill(COR_FUNDO)
        except Exception as e:
            tela.fill(COR_FUNDO)
        # Fade-out se necessário
        if self.fading_out_imagem_inicial:
            fade_surf = pygame.Surface((self.largura, self.altura), pygame.SRCALPHA)
            fade_surf.fill((0, 0, 0, 255 - int(self.fade_alpha_imagem_inicial)))
>>>>>>> d302c89 (Primeiro commit do projeto Sinuca Delícia)
            tela.blit(fade_surf, (0, 0))

    def desenhar_animacao_tacos(self):
        # Fundo
        if self.chao_bar:
            tela.blit(self.chao_bar, (0, 0))
        else:
            tela.fill(COR_FUNDO)

<<<<<<< HEAD
        # --- Mesa sempre por baixo da animação ---
        # Feltro
=======
        # Mesa e feltro
>>>>>>> d302c89 (Primeiro commit do projeto Sinuca Delícia)
        if self.img_mesa_feltro:
            tela.blit(self.img_mesa_feltro, (self.x_mesa, self.y_mesa))
        else:
            mesa_rect = pygame.Rect(self.x_mesa, self.y_mesa, LARGURA_MESA, ALTURA_MESA)
            pygame.draw.rect(tela, COR_MESA, mesa_rect, border_radius=20)

<<<<<<< HEAD
        # Funil dos buracos (opcional, pode remover se não quiser durante animação)
        for buraco in self.buracos:
            for i in range(8, 0, -1):
                raio = RAIO_BURACO + i * 4
                alpha = int(60 * (i / 8))
                cor_funil = (30, 30, 30, alpha)
                funil_surf = pygame.Surface((raio*2, raio*2), pygame.SRCALPHA)
                pygame.draw.circle(funil_surf, cor_funil, (raio, raio), raio)
                tela.blit(funil_surf, (buraco[0] - raio, buraco[1] - raio), special_flags=pygame.BLEND_RGBA_ADD)

        # Borda por cima do feltro
=======
        # Borda
>>>>>>> d302c89 (Primeiro commit do projeto Sinuca Delícia)
        if self.img_borda:
            borda_rect = self.img_borda.get_rect(center=(self.x_mesa + LARGURA_MESA // 2, self.y_mesa + ALTURA_MESA // 2))
            tela.blit(self.img_borda, borda_rect)
        else:
            borda_rect = pygame.Rect(self.x_mesa - 20, self.y_mesa - 20, LARGURA_MESA + 40, ALTURA_MESA + 40)
            pygame.draw.rect(tela, COR_BORDA, borda_rect, border_radius=30)

<<<<<<< HEAD
        # Buracos por cima de tudo (removido)

        # --- Animação dos tacos e personagens ---
        if self.animacao_tacos_iniciada:
            if self.taco1_rot and self.taco1_rect:
                tela.blit(self.taco1_rot, self.taco1_rect)
            if self.taco2_rot and self.taco2_rect:
                tela.blit(self.taco2_rot, self.taco2_rect)
            if self.personagem_mecanico_img and self.mecanico_rect:
                tela.blit(self.personagem_mecanico_img, self.mecanico_rect)
            if self.personagem_bebendo_img and self.bebendo_rect:
                tela.blit(self.personagem_bebendo_img, self.bebendo_rect)
=======
        # --- Animação dos tacos e personagens ---
        # Tacos devem seguir os personagens
        if self.animacao_tacos_iniciada:
            # TACO 1 (segue mecanico)
            if self.taco1_rot and self.mecanico_rect:
                taco1_rect = self.taco1_rot.get_rect(center=self.mecanico_rect.center)
                tela.blit(self.taco1_rot, taco1_rect)
            # TACO 2 (segue bebendo)
            if self.taco2_rot and self.bebendo_rect:
                taco2_rect = self.taco2_rot.get_rect(center=self.bebendo_rect.center)
                tela.blit(self.taco2_rot, taco2_rect)
            # Personagem mecânico
            if self.personagem_mecanico_img and self.mecanico_rect:
                # Aumenta o tamanho do personagem
                img = pygame.transform.scale(self.personagem_mecanico_img, (int(self.personagem_mecanico_img.get_width()*1.7), int(self.personagem_mecanico_img.get_height()*1.7)))
                rect = img.get_rect(center=self.mecanico_rect.center)
                tela.blit(img, rect)
            # Personagem bebendo
            if self.personagem_bebendo_img and self.bebendo_rect:
                img = pygame.transform.scale(self.personagem_bebendo_img, (int(self.personagem_bebendo_img.get_width()*1.7), int(self.personagem_bebendo_img.get_height()*1.7)))
                rect = img.get_rect(center=self.bebendo_rect.center)
                tela.blit(img, rect)
>>>>>>> d302c89 (Primeiro commit do projeto Sinuca Delícia)

    def desenhar_jogo(self):
        # Fundo
        if self.chao_bar:
            tela.blit(self.chao_bar, (0, 0))
        else:
            tela.fill(COR_FUNDO)

        # Feltro
        if self.img_mesa_feltro:
            tela.blit(self.img_mesa_feltro, (self.x_mesa, self.y_mesa))
        else:
            mesa_rect = pygame.Rect(self.x_mesa, self.y_mesa, LARGURA_MESA, ALTURA_MESA)
            pygame.draw.rect(tela, COR_MESA, mesa_rect, border_radius=20)

        # Borda por cima do feltro
        if self.img_borda:
            borda_rect = self.img_borda.get_rect(center=(self.x_mesa + LARGURA_MESA // 2, self.y_mesa + ALTURA_MESA // 2))
            tela.blit(self.img_borda, borda_rect)
        else:
            borda_rect = pygame.Rect(self.x_mesa - 20, self.y_mesa - 20, LARGURA_MESA + 40, ALTURA_MESA + 40)
            pygame.draw.rect(tela, COR_BORDA, borda_rect, border_radius=30)

        # Desenhar bolas
        for bola in self.bolas:
            bola.desenhar(tela)

        # Desenhar indicador de jogador atual
        cor_indicador = COR_JOGADOR1 if self.jogador_atual == 1 else COR_JOGADOR2
        texto_jogador = f"Jogador {self.jogador_atual}"
        if self.jogador1_tipo and self.jogador_atual == 1:
            texto_jogador += f" ({self.jogador1_tipo})"
        elif self.jogador2_tipo and self.jogador_atual == 2:
            texto_jogador += f" ({self.jogador2_tipo})"
        texto_surf = fonte_media.render(texto_jogador, True, COR_TEXTO)
        texto_rect = texto_surf.get_rect(center=(self.largura // 2, 20))
        fundo_rect = texto_rect.inflate(10, 5)
        pygame.draw.rect(tela, cor_indicador, fundo_rect, border_radius=5)
        tela.blit(texto_surf, texto_rect)

        # Linha pontilhada de mira invertida e linha de força
        if self.todas_paradas and not self.bola_branca_encacapada and self.bola_branca and self.bola_branca.na_mesa:
            start = (int(self.bola_branca.x), int(self.bola_branca.y))
            mouse_pos = pygame.mouse.get_pos()
            dx = mouse_pos[0] - self.bola_branca.x
            dy = mouse_pos[1] - self.bola_branca.y
            if dx != 0 or dy != 0:
                angulo = math.atan2(dy, dx)
            else:
                angulo = self.angulo_tacada
            comprimento = 300
            # Linha pontilhada invertida (oposta ao mouse)
<<<<<<< HEAD
            end_inv = (int(self.bola_branca.x - math.cos(angulo) * comprimento), int(self.bola_branca.y - math.sin(angulo) * comprimento))
            desenhar_linha_pontilhada(tela, (255,255,255), start, end_inv, width=2, dash_length=10)
            # Linha sólida de força (da bola até o ponteiro)
            pygame.draw.line(tela, (0,255,0), start, mouse_pos, 4)

        # Mensagem de estado
=======
            end_inv = (int(self.bola_branca.x - math.cos(angulo) * comprimento)), int(self.bola_branca.y - math.sin(angulo) * comprimento)
            desenhar_linha_pontilhada(tela, COR_BRANCA, start, end_inv, 2)

            # Linha de força
            forca_linha = 50 + 200 * (self.distancia_puxada_estilingue / LIMITE_PUXADA_ESTILINGUE)
            end_forca = (int(self.bola_branca.x + math.cos(angulo) * forca_linha), int(self.bola_branca.y + math.sin(angulo) * forca_linha))
            desenhar_linha_pontilhada(tela, COR_VERMELHA, start, end_forca, 2)

        # Mensagens na tela
>>>>>>> d302c89 (Primeiro commit do projeto Sinuca Delícia)
        if self.mensagem and self.tempo_mensagem > 0:
            texto_msg = fonte_media.render(self.mensagem, True, COR_AMARELA)
            texto_rect = texto_msg.get_rect(center=(self.largura // 2, self.altura - 20))
            tela.blit(texto_msg, texto_rect)

    def desenhar_reposicionar(self):
        self.desenhar_jogo()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        valido = self.posicao_valida_reposicionar(mouse_x, mouse_y)
        cor_fantasma = (*(COR_VERDE if valido else COR_VERMELHA), 150)
        temp_surf = pygame.Surface((RAIO_BOLA*2, RAIO_BOLA*2), pygame.SRCALPHA)
       
        pygame.draw.circle(temp_surf, cor_fantasma, (RAIO_BOLA, RAIO_BOLA), RAIO_BOLA)
        tela.blit(temp_surf, (mouse_x - RAIO_BOLA, mouse_y - RAIO_BOLA))
        if self.mensagem and self.tempo_mensagem > 0:
            texto_msg = fonte_media.render(self.mensagem, True, COR_AMARELA)
            texto_rect = texto_msg.get_rect(center=(self.largura // 2, self.altura - 20))
            tela.blit(texto_msg, texto_rect)

    def desenhar_fim_jogo(self):
        self.desenhar_jogo()
        overlay = pygame.Surface((self.largura, self.altura), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        tela.blit(overlay, (0, 0))
        texto_fim = fonte_grande.render("FIM DE JOGO", True, COR_TEXTO)
        texto_rect = texto_fim.get_rect(center=(self.largura // 2, self.altura // 2 - 100))
        tela.blit(texto_fim, texto_rect)
        texto_vencedor = fonte_media.render(self.mensagem, True, COR_AMARELA)
       
        vencedor_rect = texto_vencedor.get_rect(center=(self.largura // 2, self.altura // 2))
        tela.blit(texto_vencedor, vencedor_rect)
        texto_inst1 = fonte_media.render("Pressione 'M' para Menu", True, COR_TEXTO)
        inst1_rect = texto_inst1.get_rect(center=(self.largura // 2, self.altura // 2 + 60))
        tela.blit(texto_inst1, inst1_rect)
        texto_inst2 = fonte_media.render("Pressione 'Q' para Sair", True, COR_TEXTO)
        inst2_rect = texto_inst2.get_rect(center=(self.largura // 2, self.altura // 2 + 100))
        tela.blit(texto_inst2, inst2_rect)

    def desenhar_doacao(self):
        # Fundo com a imagem de doação
        img = carregar_imagem("sobre.jpeg", (LARGURA, ALTURA))
        tela.blit(img, (0, 0))
        # Botão voltar
        mouse_pos = pygame.mouse.get_pos()
        cor_botao_voltar = COR_BOTAO_HOVER if self.botao_voltar_rect.collidepoint(mouse_pos) else COR_BOTAO
        pygame.draw.rect(tela, cor_botao_voltar, self.botao_voltar_rect, border_radius=10)
        pygame.draw.rect(tela, COR_TEXTO, self.botao_voltar_rect, 2, border_radius=10)
        texto_voltar = fonte_media.render("VOLTAR", True, COR_TEXTO)
        texto_voltar_rect = texto_voltar.get_rect(center=self.botao_voltar_rect.center)
        tela.blit(texto_voltar, texto_voltar_rect)

    # --- Métodos de Lógica ---
    def dar_tacada(self):
        if not self.bola_branca or not self.bola_branca.na_mesa:
            return
        forca_aplicada = self.distancia_puxada_estilingue * FATOR_FORCA_ESTILINGUE
        angulo_aplicado = self.angulo_tacada
        self.bola_branca.vx = math.cos(angulo_aplicado) * forca_aplicada
        self.bola_branca.vy = math.sin(angulo_aplicado) * forca_aplicada
        self.todas_paradas = False
        self.primeira_tacada = False
        self.bolas_encacapadas_na_tacada = []
        self.falta_na_tacada = False

        if audio_enabled and self.sons_tacada:
            try:
                som = random.choice(self.sons_tacada)
                if som:
                    volume = 0.08 + 0.2 * (forca_aplicada / FORCA_MAX)  # Volume reduzido
                    som.set_volume(min(0.25, volume))
                    som.play()
            except Exception as e: print(f"Erro ao tocar som tacada: {e}")

    def verificar_troca_turno(self):
        print("[DEBUG] Verificando troca de turno...") # Log Adicionado
        jogador_continua = False
        falta_ocorrida = self.falta_na_tacada

        if falta_ocorrida:
            print("[DEBUG] Falta detectada na tacada.") # Log Adicionado
            self.mensagem = "Falta!" + (" Bola branca encaçapada." if self.bola_branca_encacapada else "")
            self.tempo_mensagem = 120
            if not self.bola_branca_encacapada:
                 print("[DEBUG] Falta sem bola branca encaçapada, trocando jogador.") # Log Adicionado
                 self.trocar_jogador()
            else:
                 print("[DEBUG] Falta COM bola branca encaçapada, esperando reposicionamento.") # Log Adicionado
            # Se bola branca foi encaçapada, já está no estado REPOSICIONAR e o turno será trocado ao sair dele
            return

        if not self.bolas_encacapadas_na_tacada:
            print("[DEBUG] Nenhuma bola encaçapada, trocando jogador.") # Log Adicionado
            self.trocar_jogador()
            return

        print(f"[DEBUG] Bolas encaçapadas nesta tacada: {[b.numero for b in self.bolas_encacapadas_na_tacada]}") # Log Adicionado
        tipo_jogador_atual = self.jogador1_tipo if self.jogador_atual == 1 else self.jogador2_tipo

        for bola in self.bolas_encacapadas_na_tacada:
            if bola.numero == 0: continue # Ignora bola branca aqui
            if bola.numero == 8: continue # Bola 8 tratada em bola_encacapada

            # Definição de tipo na primeira bola válida encaçapada
            if tipo_jogador_atual is None:
                tipo_bola = "listradas" if bola.listrada else "lisas"
                print(f"[DEBUG] Primeira bola válida ({bola.numero}-{tipo_bola}) define o tipo.") # Log Adicionado
                if self.jogador_atual == 1:
                    self.jogador1_tipo = tipo_bola
                    self.jogador2_tipo = "lisas" if tipo_bola == "listradas" else "listradas"
                else:
                    self.jogador2_tipo = tipo_bola
                    self.jogador1_tipo = "lisas" if tipo_bola == "listradas" else "listradas"
                print(f"[DEBUG] Tipos definidos - J1: {self.jogador1_tipo}, J2: {self.jogador2_tipo}") # Log Adicionado
                jogador_continua = True
                tipo_jogador_atual = self.jogador1_tipo if self.jogador_atual == 1 else self.jogador2_tipo # Atualiza para a lógica seguinte
            else:
                # Tipos já definidos, verificar se a bola é do jogador atual
                tipo_bola = "listradas" if bola.listrada else "lisas"
                if tipo_bola == tipo_jogador_atual:
                    print(f"[DEBUG] Jogador {self.jogador_atual} encaçapou bola válida ({bola.numero}-{tipo_bola}). Continua jogando.") # Log Adicionado
                    jogador_continua = True
                else:
                    print(f"[DEBUG] Jogador {self.jogador_atual} encaçapou bola do adversário ({bola.numero}-{tipo_bola}). Não continua.") # Log Adicionado
                    # Não seta jogador_continua = False aqui, pois pode ter encaçapado uma válida antes/depois

        # Decide se troca o turno baseado se *alguma* bola válida foi encaçapada
        if not jogador_continua:
            print("[DEBUG] Nenhuma bola válida do jogador foi encaçapada nesta tacada. Trocando jogador.") # Log Adicionado
            self.trocar_jogador()
        else:
            print(f"[DEBUG] Jogador {self.jogador_atual} continua o turno.") # Log Adicionado
            if audio_enabled and self.sons_acerto:
                 try:
                     som = random.choice(self.sons_acerto)
                     if som: som.play()
                 except Exception as e: print(f"Erro ao tocar som acerto: {e}")

    def bola_encacapada(self, bola):
        tipo_bola_str = 'Listrada' if bola.listrada else 'Lisa' if bola.numero != 0 else 'Branca'
        print(f"Processando encaçapamento: Bola {bola.numero} ({tipo_bola_str})")

        if bola == self.bola_branca:
            self.bola_branca_encacapada = True
            self.falta_na_tacada = True
            self.estado = REPOSICIONAR
            self.mensagem = "Reposicione a bola branca."
            self.tempo_mensagem = 120
            print("Bola branca encaçapada. Estado -> REPOSICIONAR")
            if audio_enabled and self.som_encacapar: self.som_encacapar.play()
            return

        if bola.numero == 8:
            self.bola_8_encacapada = True
            tipo_jogador_atual = self.jogador1_tipo if self.jogador_atual == 1 else self.jogador2_tipo
            vitoria = False
            if tipo_jogador_atual is None or self.primeira_tacada:
                self.vencedor = 3 - self.jogador_atual
                self.mensagem = f"Jogador {self.vencedor} vence! Bola 8 ilegal."
            else:
                todas_do_jogador_foram = True
                for b in self.bolas:
                    if b.na_mesa and b.numero != 8 and b.numero != 0:
                        tipo_b = "listradas" if b.listrada else "lisas"
                        if tipo_b == tipo_jogador_atual:
                            todas_do_jogador_foram = False
                            break
                if todas_do_jogador_foram:
                    self.vencedor = self.jogador_atual
                    self.mensagem = f"Jogador {self.vencedor} vence! Bola 8 legal."
                    vitoria = True
                else:
                    self.vencedor = 3 - self.jogador_atual
                    self.mensagem = f"Jogador {self.vencedor} vence! Bola 8 antes da hora."

            print(self.mensagem)
            self.estado = FIM_JOGO
            if audio_enabled and self.som_encacapar: self.som_encacapar.play()
            return

        # Tocar som de encaçapamento normal
        if audio_enabled and self.som_encacapar: self.som_encacapar.play()

    def trocar_jogador(self):
        self.jogador_atual = 3 - self.jogador_atual
        print(f"--- Vez do Jogador {self.jogador_atual} ---")

    def posicao_valida_reposicionar(self, x, y):
        if not (self.x_mesa + RAIO_BOLA < x < self.x_mesa + LARGURA_MESA - RAIO_BOLA and
                self.y_mesa + RAIO_BOLA < y < self.y_mesa + ALTURA_MESA - RAIO_BOLA):
            return False
        for bola in self.bolas:
            if bola != self.bola_branca and bola.na_mesa:
                dist_sq = (x - bola.x)**2 + (y - bola.y)**2
                if dist_sq < (RAIO_BOLA * 2)**2:
                    return False
        return True

# --- Loop Principal --- 
def main():
    try:
        if not os.path.exists(assets_dir):
            try:
                os.makedirs(assets_dir)
                print(f"Pasta assets criada em: {assets_dir}")
            except OSError as e:
                print(f"Erro ao criar pasta assets: {e}")

        mostrar_intro_gif()
        jogo = JogoBilhar(LARGURA, ALTURA)
        # Pré-carregar frames do regras.gif para fundo das regras
        regras_gif_frames, regras_gif_durations, regras_gif_total = desenhar_gif_loop("regras.gif", LARGURA, ALTURA)
        # Salva os frames na instância do jogo para uso em desenhar_regras
        jogo.regras_gif_frames = regras_gif_frames
        jogo.regras_gif_durations = regras_gif_durations
        jogo.regras_gif_total = regras_gif_total if regras_gif_total else 1
        while True:
            jogo.processar_eventos()
            jogo.atualizar()
            # --- Desenho customizado para regras e doação ---
            if jogo.estado == REGRAS and regras_gif_frames:
                jogo.desenhar_regras(sem_fundo=False)
            elif jogo.estado == DOACAO:
                jogo.desenhar_doacao()
            else:
                jogo.desenhar()
            pygame.display.flip()
            clock.tick(60)
    except Exception as e:
        print("\n--- ERRO FATAL NO JOGO ---")
        print(f"Tipo de Erro: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        print("-------------------------")
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()
