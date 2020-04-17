from kandinsky import *
from ion import *
from random import *
from time import *

mRapide = input("Default settings? [Y/n] ")
if mRapide == "n":
    vitesse = input("Speed? [8] ")
    if vitesse == "":
        vitesse = 8
    else:
        vitesse = int(vitesse)
    cMode = input("Light mode? [Y/n] ")
    if cMode == "n":
        cMode = "black"
    else:
        cMode = "white"
    t = input("Blocks' size? (4/5/8/<10>) ")
    if t = "":
        t = 10
    else:
        t = int(t)
else:
    vitesse, cMode, t = 8, "white", 10
L, l = 320 // t, 200 // t

noir, blanc, rouge, vert = (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 230, 0)
vers = [[l // 2, n] for n in range(L // 2 - 2, L // 2 + 2)]
px, py = vers[0][0], vers[0][1]
dx, dy = 0, 1
score = 0

if cMode == "white":
    fill_rect(0, 200, 320, 1, noir)
else:
    fill_rect(0, 0, 320, 222, noir)
    fill_rect(0, 200, 320, 1, blanc)

while True:
    if cMode == "white":
            draw_string("Score: "+str(score), 5, 203)
        else:
            draw_string("Score: "+str(score), 5, 203, blanc, noir)

    while [px, py] in vers:
        px, py = randint(0, l - 1), randint(0, L - 1)
    fill_rect(py * t, px * t, t, t, rouge)

    t1 = monotonic()
    while monotonic() - t1 < 1 / vitesse:
        for dir in [[0, 0, -1], [1, -1, 0], [2, 1, 0], [3, 0, 1]]:
            if keydown(dir[0]):
                dx, dy = dir[1], dir[2]

    first, last = vers[0], vers[-1]
    nx, ny = last[0] + dx, last[1] + dy
    if 0 <= nx < l and 0 <= ny < L and [nx, ny] not in vers:
        vers.append([nx, ny])
        fill_rect(ny * t, nx * t, t, t, vert)
    else:
        break
    if [nx, ny] == [px, py]:
        score += 1
    else:
        del vers[0]
        if cMode == "white":
            fill_rect(first[1] * t, first[0] * t, t, t, blanc)
        else:
            fill_rect(first[1] * t, first[0] * t, t, t, noir)
