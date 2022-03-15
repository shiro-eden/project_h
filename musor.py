import pygame as pg
import sys


BLACK = (0,0,0)
WHITE = (100,100,100)
RED = (230, 0, 0)
dots = []
curve = []
press = 0

sc = pg.display.set_mode((800, 800))
sc.fill(WHITE)
pg.display.update()

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    pressed = pg.mouse.get_pressed()
    pos = pg.mouse.get_pos()
    if pressed[0]:
        dots = [pos, pos, pos]
    elif dots:
        dots[2] = pos
        if dots[0][0] < pos[0]:
            m = dots[0][0] + (pos[0] - dots[0][0]) // 2
        else:
            m = pos[0] + (dots[0][0] - pos[0]) // 2
        if dots[0][1] < pos[1]:
            n = dots[0][1] - 40
        else:
            n = pos[1] - 40
        dots[1] = (m, n)
    if dots:
        pg.draw.aalines(sc, WHITE, False, dots)
        for dot in dots:
            pg.draw.circle(sc, WHITE, dot, 5, 1)
        curve = []
        for i in map(lambda x: x / 100.0, range(0, 105, 5)):
            x = (1.0 - i) ** 2 * dots[0][0] + 2 * (1.0 - i) * i * dots[1][0] + i ** 2 * dots[2][0]
            y = (1.0 - i) ** 2 * dots[0][1] + 2 * (1.0 - i) * i * dots[1][1] + i ** 2 * dots[2][1]
            curve.append([x, y])
        pg.draw.lines(sc, RED, False, curve, 3)

    pg.display.update()
    sc.fill(WHITE)

    pg.time.delay(20)