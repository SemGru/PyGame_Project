import pygame as pg
from random import randrange
import pymunk.pygame_util

Running = False

# a = 0
def Game(Running):
    pymunk.pygame_util.positive_y_is_up = False

    RES = WIDTH, HEIGHT = 600, 500
    FPS = 60

    pg.init()
    surface = pg.display.set_mode(RES)
    pg.display.set_caption("BOXED FRUIT")
    Icon = pg.image.load('Images/Icon.png')
    pg.display.set_icon(Icon)
    clock = pg.time.Clock()
    draw_options = pymunk.pygame_util.DrawOptions(surface)

    space = pymunk.Space()
    space.gravity = 0, 2000
    space = pymunk.Space()
    space.gravity = 0, 2000

    def create_ball(space, pos):
        ball_mass, ball_radius = 1, 30
        ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
        ball_body = pymunk.Body(ball_mass, ball_moment)
        ball_body.position = [pos[0], 100]
        ball_shape = pymunk.Circle(ball_body, ball_radius)
        ball_shape.elasticity = 0.8
        space.add(ball_body, ball_shape)

    segment_shape = pymunk.Segment(space.static_body, (0, HEIGHT), (WIDTH, HEIGHT), 20)
    segment_shape.elasticity = 0.8
    space.add(segment_shape)

    segment_shape_left = pymunk.Segment(space.static_body, (0, 0), (0, HEIGHT), 20)
    segment_shape_left.elasticity = 0.8
    space.add(segment_shape_left)

    segment_shape_right = pymunk.Segment(space.static_body, (WIDTH, HEIGHT), (WIDTH, 0), 20)
    segment_shape_right.elasticity = 0.8
    space.add(segment_shape_right)

    while Running:
        surface.fill(pg.Color('black'))
        for i in pg.event.get():
            if i.type == pg.QUIT:
                Running = False
            if i.type == pg.MOUSEBUTTONDOWN:
                if i.button == 1:
                    create_ball(space, i.pos)

        space.step(1 / FPS)
        space.debug_draw(draw_options)

        clock.tick(FPS)
        pg.display.flip()

    pg.quit()

