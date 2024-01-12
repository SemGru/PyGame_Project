import pygame
from random import randrange as rnd
import pygame.mixer
import datetime

Image = '1.jpg'
SOUND = True
SCORE = -1


def Game(Running, IMG, sound_music, sound_effects):
    global SCORE
    Time_start = datetime.datetime.now()
    WIDTH, HEIGHT = 1200, 800
    fps = 60
    # font_style = pygame.font.SysFont("bahnschrift", 25)
    # score_font = pygame.font.SysFont("comicsansms", 35)
    # paddle settings
    paddle_w = 330
    paddle_h = 35
    paddle_speed = 15
    paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)
    # ball settings
    ball_radius = 20
    ball_speed = 6
    ball_rect = int(ball_radius * 2 ** 0.5)
    ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
    dx, dy = 1, -1
    # blocks settings
    block_list = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
    color_list = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(10) for j in range(4)]

    pygame.init()
    sc = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    # background image
    img = pygame.image.load(IMG).convert()
    pygame.display.set_caption("ARCANOID")
    Icon = pygame.image.load('Images/icon_game_2.png')
    pygame.display.set_icon(Icon)
    score_font = pygame.font.SysFont("comicsansms", 45)
    sound_game = pygame.mixer.Sound("Sounds/Worldmap_Theme.mp3")
    sound_lose = pygame.mixer.Sound("Sounds/Lose_sound.mp3")
    sound_burst = pygame.mixer.Sound("Sounds/burst_ballun.mp3")
    sound_win = pygame.mixer.Sound("Sounds/congrad.mp3")
    if sound_music:
        sound_game.play(-1)

    def Your_score(score):
        value = score_font.render("Your Score: " + str(score), True, (255, 69, 0))
        sc.blit(value, [0, 0])

    def detect_collision(dx, dy, ball, rect):
        if dx > 0:
            delta_x = ball.right - rect.left
        else:
            delta_x = rect.right - ball.left
        if dy > 0:
            delta_y = ball.bottom - rect.top
        else:
            delta_y = rect.bottom - ball.top

        if abs(delta_x - delta_y) < 10:
            dx, dy = -dx, -dy
        elif delta_x > delta_y:
            dy = -dy
        elif delta_y > delta_x:
            dx = -dx
        return dx, dy

    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
        sc.blit(img, (0, 0))
        # drawing world
        [pygame.draw.rect(sc, color_list[color], block) for color, block in enumerate(block_list)]
        pygame.draw.rect(sc, pygame.Color(190, 245, 116), paddle)
        pygame.draw.circle(sc, pygame.Color(190, 245, 116), ball.center, ball_radius)
        # ball movement
        ball.x += ball_speed * dx
        ball.y += ball_speed * dy
        # collision left right
        if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
            dx = -dx
        # collision top
        if ball.centery < ball_radius:
            dy = -dy
        # collision paddle
        if ball.colliderect(paddle) and dy > 0:
            dx, dy = detect_collision(dx, dy, ball, paddle)
            # if dx > 0:
            #     dx, dy = (-dx, -dy) if ball.centerx < paddle.centerx else (dx, -dy)
            # else:
            #     dx, dy = (-dx, -dy) if ball.centerx >= paddle.centerx else (dx, -dy)
        # collision blocks
        hit_index = ball.collidelist(block_list)
        if hit_index != -1:
            if sound_effects:
                sound_burst.play()
            hit_rect = block_list.pop(hit_index)
            hit_color = color_list.pop(hit_index)
            dx, dy = detect_collision(dx, dy, ball, hit_rect)
            # special effect
            hit_rect.inflate_ip(ball.width * 3, ball.height * 3)
            pygame.draw.rect(sc, hit_color, hit_rect)
            fps += 2
        # win, game over
        if ball.bottom > HEIGHT:
            if sound_effects:
                sound_game.stop()
                sound_lose.play()
                pygame.time.wait(3500)
            Time_end = datetime.datetime.now()
            Score_time = 120 - (Time_end - Time_start).seconds
            score((40 - len(block_list)) * 12)
            # score((40 - len(block_list)) * Score_time)
            Running = False
        elif not len(block_list):
            if sound_effects:
                sound_game.stop()
                sound_win.play()
                pygame.time.wait(3000)
            Time_end = datetime.datetime.now()
            Score_time = 120 - (Time_end - Time_start).seconds
            # score(40 * Score_time)
            score(40 * 12)
            Running = False
        # control
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddle_speed
        if key[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.right += paddle_speed

        Your_score(40 - len(block_list))
        pygame.display.update()
        # update screen
        clock.tick(fps)

    pygame.quit()


def score(sc):
    global SCORE
    SCORE = sc


def get_score():
    return SCORE
