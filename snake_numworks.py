from kandinsky import *
from ion import *
from random import *
from time import *

noir, rouge, vert = (0, 0, 0), (255, 0, 0), (0, 255, 0)
vers = [[10, 14], [10, 15], [10, 16], [10, 17]]
pomme = False
dx, dy = 0, 1
px, py = 10, 14
score = 0

fill_rect(0, 0, 320, 200, noir)
draw_string("NumSnake !", 5, 200)
draw_string("Score : 0", 200, 200)


def remplir(x, y, coul):
    fill_rect(x * 10, y * 10, 10, 10, coul)

while True:
    if not pomme:
        while [px, py] in vers:
            px, py = randint(0, 19), randint(0, 31)
        remplir(py, px, rouge)
        pomme = True
    t1 = monotonic()
    while monotonic() - t1 < 0.2:
        if keydown(0):
            dx, dy = 0, -1
        elif keydown(1):
            dx, dy = -1, 0
        elif keydown(2):
            dx, dy = 1, 0
        elif keydown(3):
            dx, dy = 0, 1
    nx, ny = vers[-1][0] + dx, vers[-1][1] + dy
    if [nx, ny] == [px, py]:
        pomme = False
        score += 1
        draw_string(str(score), 280, 200)
    else:
        del vers[0]
        remplir(vers[0][1], vers[0][0], noir)
    if 0 <= nx < 20 and 0 <= ny < 32 and [nx, ny] not in vers:
        vers.append([nx, ny])
        remplir(ny, nx, vert)
    else:
        break
