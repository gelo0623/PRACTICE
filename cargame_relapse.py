import pygame
import random
import sys
import time

pygame.init()

w, h = 500, 700
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

car = pygame.Rect(w//2 - 20, h - 100, 40, 80)
road_lines = [pygame.Rect(w//2 - 5, i, 10, 40) for i in range(0, h, 100)]
pygame.display.set_caption("Car Dodge with Lyrics")

enemy_cars = []
speed = 3
distance = 0
score = 0
font = pygame.font.SysFont("Courier", 30, bold=True)
retro_font = pygame.font.SysFont("Courier", 60, bold=True)

game_over = False
running = True

lanes = [80, 160, 240, 320, 400]
last_spawn_lane = None

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Lyrics
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
    (96, "Kahit sa’n man mapunta ay anino mo'y"),
    (102, "Kumakapit sa'king kamay"),
    (106, "Ako ay dahan-dahang"),
    (109, "nililibang nang buhay pa"),
    (116, "Hindi na makalaya"),
    (119, "Dinadalaw mo'ko"),
    (123, "Bawa’t gabi"),
    (125, "Wala mang nakikita"),
    (128, "Haplos mo’y"),
    (129, "Ramdam pa rin sa dilim"),
]


def draw_tv_effect():
    for y in range(0, h, 4):
        pygame.draw.line(screen, (10, 10, 10), (0, y), (w, y))


def play_song_with_black_screen():
    screen.fill(BLACK)
    pygame.display.flip()

    try:
        pygame.mixer.music.load("multo.mp3.mp3")
    except:
        print("Error: Could not find 'multo.mp3.mp3'.")
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
            text_rect = text_surface.get_rect(center=(w // 2, h // 2))
            screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(30)

        if not pygame.mixer.music.get_busy():
            running = False

    pygame.quit()
    sys.exit()


# -------- MAIN GAME LOOP --------
while True:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (20, 20, 20), (50, 0, 400, h))
    for line in road_lines:
        pygame.draw.rect(screen, (180, 180, 180), line)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car.left > 60:
            car.x -= 7
        if keys[pygame.K_RIGHT] and car.right < 440:
            car.x += 7

        distance += speed / 10
        score = int(distance)
        speed = 3 + distance / 150

        if random.randint(1, 40) == 1:
            lane = random.choice(lanes)
            if lane != last_spawn_lane:
                enemy_cars.append(pygame.Rect(lane, -100, 40, 80))

        new_enemies = []
        occupied_lanes = []
        for enemy in enemy_cars:
            enemy.y += speed
            if enemy.y < h:
                if enemy.x not in occupied_lanes:
                    new_enemies.append(enemy)
                    occupied_lanes.append(enemy.x)
        enemy_cars = new_enemies

        for enemy in enemy_cars:
            # Enemy car (yellow body + black wheels)
            pygame.draw.rect(screen, (150, 150, 0), enemy)
            pygame.draw.rect(screen, (0, 0, 0),
                             (enemy.x-8, enemy.y+20, 12, 15))
            pygame.draw.rect(screen, (0, 0, 0),
                             (enemy.x+36, enemy.y+20, 12, 15))
            pygame.draw.rect(screen, (0, 0, 0),
                             (enemy.x-8, enemy.y+50, 12, 15))
            pygame.draw.rect(screen, (0, 0, 0),
                             (enemy.x+36, enemy.y+50, 12, 15))

            if enemy.colliderect(car):
                game_over = True

        # Player car (green body + black wheels)
        pygame.draw.rect(screen, (0, 200, 150), car)
        pygame.draw.rect(screen, (0, 0, 0), (car.x-8, car.y+20, 12, 15))
        pygame.draw.rect(screen, (0, 0, 0), (car.x+36, car.y+20, 12, 15))
        pygame.draw.rect(screen, (0, 0, 0), (car.x-8, car.y+50, 12, 15))
        pygame.draw.rect(screen, (0, 0, 0), (car.x+36, car.y+50, 12, 15))

        for line in road_lines:
            line.y += speed
            if line.y > h:
                line.y = -100

        score_text = font.render(f"SCORE: {score}", True, (255, 255, 0))
        screen.blit(score_text, (10, 10))

        draw_tv_effect()

    else:
        # Instead of "GAME OVER" text/video → start lyrics sequence
        play_song_with_black_screen()

    pygame.display.flip()
    clock.tick(60)
