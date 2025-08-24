import pygame
import random
import sys
import time

pygame.init()

WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Falling Blocks")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


font = pygame.font.SysFont("Arial", 36)


player_size = 50
player = pygame.Rect(WIDTH // 2, HEIGHT - 2 * player_size, player_size, player_size)
player_speed = 8


block_size = 50
num_blocks = 10  
block_speed = 7
blocks = [pygame.Rect(random.randint(0, WIDTH - block_size), random.randint(-600, 0), block_size, block_size) for _ in range(num_blocks)]

clock = pygame.time.Clock()

lyrics = [
    (23, "Humingang malalim"),
    (26, "Pumikit na muna"),
    (32, "At baka-sakaling"),
    (35, "Namamalik mata lang"),
    (41, "Ba't nababahala?"),
    (45, "'Di ba't ako'y mag-isa"),
    (51, "'kala ko'y payapa"),
    (54, "Boses mo'y tumatawag na"),
    (60, "Binaon naman na ang lahat"),
    (64, "Tinakpan naman na 'king sugat"),
    (69, "Ngunit ba't ba andito pa rin"),
    (73, "Hirap na 'kong intindihin"),
    (78, "Tanging panalangin"),
    (82, "Lubayan na sana"),
    (86, "Dahil sa bawat tingin"),
    (91, "Mukha mo'y nakikita"),
    (96, "Kahit sa'n man mapunta ay anino mo'y"),
    (102, "Kumakapit sa'king kamay"),
    (106, "Ako ay dahan-dahang"),
    (109, "nililibang nang buhay pa"),
    (116, "Hindi na makalaya"),
    (119, "Dinadalaw mo'ko"),
    (123, "Bawa't gabi"),
    (125, "Wala mang nakikita"),
    (128, "Haplos mo'y"),
    (129, "Ramdam pa rin sa dilim"),
]

def play_song_with_black_screen():
    screen.fill(BLACK)
    pygame.display.flip()

    try:
        pygame.mixer.music.load("multo.mp3.mp3") 
    except:
        print("Error: Could not find 'multo.mp3.mp3'. Make sure it's in the same folder.")
        return

    pygame.mixer.music.play()
    start_time = time.time()
    current_line = ""

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        elapsed = time.time() - start_time

        
        for t, line in lyrics:
            if elapsed >= t:
                current_line = line

        
        screen.fill(BLACK)
        if current_line:
            text_surface = font.render(current_line, True, WHITE)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(30)

        
        if not pygame.mixer.music.get_busy():
            running = False

    pygame.quit()
    sys.exit()



running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.move_ip(-player_speed, 0)
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.move_ip(player_speed, 0)

   
    for block in blocks:
        block.move_ip(0, block_speed)
        if block.top > HEIGHT:
            block.topleft = (random.randint(0, WIDTH - block_size), random.randint(-100, 0))

        if player.colliderect(block):
            play_song_with_black_screen()

   
    pygame.draw.rect(screen, BLACK, player)
    for block in blocks:
        pygame.draw.rect(screen, RED, block)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
