import pygame
from random import randrange as rnd
import pygame.mixer

Image = '1.jpg'
SOUND = True
SCORE = -1


def Game(Running, IMG, sound_music, sound_effects):
    global SCORE
    WIDTH, HEIGHT = 1200, 800
    fps = 60
    # Праметры платформы
    paddle_w = 330
    paddle_h = 35
    paddle_speed = 15
    paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)
    # Праметры шарика
    ball_radius = 20
    ball_speed = 6
    ball_rect = int(ball_radius * 2 ** 0.5)
    ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
    # Движение шарика
    dx, dy = 1, -1
    # Создание блоков
    block_list = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
    color_list = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(10) for j in range(4)]
    # Создание окна
    pygame.init()
    sc = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    # Задний план/иконка
    img = pygame.image.load(IMG).convert()
    pygame.display.set_caption("ARCANOID")
    Icon = pygame.image.load('Images/icon_game_2.png')
    pygame.display.set_icon(Icon)

    # Звук
    score_font = pygame.font.SysFont("comicsansms", 45)
    sound_game = pygame.mixer.Sound("Sounds/Worldmap_Theme.mp3")
    sound_lose = pygame.mixer.Sound("Sounds/Lose_sound.mp3")
    sound_burst = pygame.mixer.Sound("Sounds/burst_ballun.mp3")
    sound_win = pygame.mixer.Sound("Sounds/congrad.mp3")
    # Звук на заднем плане
    if sound_music:
        sound_game.play(-1)

    def Your_score(score):
        # Отрисовка счёта очков, цвет зависит от фона
        if IMG == 'Images/space.jpg':
            value = score_font.render("Your Score: " + str(score), True, (255, 69, 0))
            sc.blit(value, [10, 800 - 65])
        elif IMG == 'Images/mars.jpg':
            value = score_font.render("Your Score: " + str(score), True, (255, 36, 0))
            sc.blit(value, [10, 800 - 65])
        elif IMG == 'Images/desert.jpg':
            value = score_font.render("Your Score: " + str(score), True, (13, 47, 250))
            sc.blit(value, [10, 800 - 65])

    # Площадь касания тел
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

    # ОСновной цикл игры
    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
        sc.blit(img, (0, 0))
        # Отрисовка всего
        [pygame.draw.rect(sc, color_list[color], block) for color, block in enumerate(block_list)]
        pygame.draw.rect(sc, pygame.Color(190, 245, 116), paddle)
        pygame.draw.circle(sc, pygame.Color(190, 245, 116), ball.center, ball_radius)
        # Движение шарика
        ball.x += ball_speed * dx
        ball.y += ball_speed * dy
        # Столкновение левой или правой частью и движение в обратную
        if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
            dx = -dx
        # Столкновение верхней частью
        if ball.centery < ball_radius:
            dy = -dy
        # Столкновение платформой
        if ball.colliderect(paddle) and dy > 0:
            dx, dy = detect_collision(dx, dy, ball, paddle)
        # Столкновение шариков и их исчезновение
        hit_index = ball.collidelist(block_list)
        if hit_index != -1:
            if sound_effects:
                sound_burst.play()
            # Исчезновение прямоугольников
            hit_rect = block_list.pop(hit_index)
            hit_color = color_list.pop(hit_index)
            dx, dy = detect_collision(dx, dy, ball, hit_rect)
            # Влияение исчезновения, то есть ускорение подвижных частей, для усложнения
            hit_rect.inflate_ip(ball.width * 3, ball.height * 3)
            pygame.draw.rect(sc, hit_color, hit_rect)
            fps += 2
        # Конце игры
        if ball.bottom > HEIGHT:
            # Проигрыш
            if sound_effects:
                sound_game.stop()
                sound_lose.play()
                pygame.time.wait(3500)
            score((40 - len(block_list)) * 12)
            Running = False
        elif not len(block_list):
            # Победа
            if sound_effects:
                sound_game.stop()
                sound_win.play()
                pygame.time.wait(3000)
            score(40 * 12)
            Running = False
        # управление стрелочками
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddle_speed
        if key[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.right += paddle_speed

        Your_score(40 - len(block_list))
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()


# Две функции для работы со счётом для его дальнейшего использования
def score(sc):
    global SCORE
    SCORE = sc


def get_score():
    return SCORE
