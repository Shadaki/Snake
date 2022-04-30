from kandinsky import *
from ion import *
from random import *
from time import *

vitesse, cMode, t = 8, ("white", "black"), 10
if input("Default settings? [y|n] ") == "n":
    if input("Speed? [8] ") != "": vitesse = int(vitesse)
    if input("Light mode? [y|n] ") != "n":("black", "white")
    if input("Blocks' size? (4/5/8/<10>) ") != "": int(t)

grille = (320 // t, 200 // t)
vers = [(grille[1] // 2, n) for n in range(grille[0] // 2 - 2, grille[0] // 2 + 2)]
p, d = (vers[0][0], vers[0][1]), (0, 1)
score = 0

fill_rect(0, 0, 320, 222, cMode[0])
fill_rect(0, 200, 320, 1, cMode[1])
while True:
    draw_string("Score: "+str(score), 5, 203, cMode[1], cMode[0])

    while p in vers: p = (randint(0, grille[1] - 1), randint(0, grille[0] - 1))
    fill_rect(p[1] * t, p[0] * t, t, t, "red")

    t1 = monotonic()
    while monotonic() - t1 < 1 / vitesse:
        for dir in [[0, 0, -1], [1, -1, 0], [2, 1, 0], [3, 0, 1]]:
            if keydown(dir[0]): d = (dir[1], dir[2])

    first, last = vers[0], vers[-1]
    n = (last[0] + d[0], last[1] + d[1])
    if 0 <= n[0] < grille[1] and 0 <= n[1] < grille[0] and n not in vers:
        vers.append((n[0], n[1]))
        fill_rect(n[1] * t, n[0] * t, t, t, "green")
    else: break
    if n == p: score += 1
    else:
        del vers[0]
        fill_rect(first[1] * t, first[0] * t, t, t, cMode[0])
