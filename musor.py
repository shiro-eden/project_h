import pygame as pg
import sys
from random import randrange

WHITE = (255, 255, 255)
BLUE = (randrange(255), randrange(255), randrange(255))

sc = pg.display.set_mode((400, 300))
sc.fill(WHITE)
pg.display.update()

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    pressed = pg.mouse.get_pressed()
    pos = pg.mouse.get_pos()
    if pressed[0]:
        pg.draw.circle(sc, [randrange(255), randrange(255), randrange(255)], pos, randrange(100))
        pg.display.update()

    pg.time.delay(20)