from kandinsky import *
from ion import *
from random import *
from time import *

vers = [[9, 14], [10, 14], [10, 15], [10, 16], [10, 17]]
pommes = []
perdu = False
fill_rect(0, 0, 320, 222, color(0, 0, 0))
direc = 4

while not perdu:
    fill_rect(vers[0][1] * 6, vers[0][0] * 6, 6, 6, color(0, 0, 0))
    del vers[0]
    for c in vers:
        fill_rect(c[1] * 6, c[0] * 6, 6, 6, color(0, 255, 0))
    for c in pommes:
        fill_rect(c[1] * 6, c[0] * 6, 6, 6, color(255, 0, 0))
    t1 = monotonic()
    touches, t = [0] * 4, 0
    while monotonic() - t1 < 0.2:
        a = 1
        if t == 0:
            if keydown(1):
                touches[0] = 1
            elif keydown(2):
                touches[1] = 1
            elif keydown(0):
                touches[2] = 1
            elif keydown(3):
                touches[3] = 1
        try:
            t = touches.index(1) + 1
        except:
            pass
    last = vers[-1]
    diff = [[[-1, 0], [1, 0], [0, -1], [0, 1]],
            [[-1, 0], [1, 0], [-1, 0], [-1, 0]],
            [[-1, 0], [1, 0], [1, 0], [1, 0]],
            [[0, -1], [0, -1], [0, -1], [0, -1]],
            [[0, 1], [0, 1], [0, -1], [0, -1]]]
    mouv = diff[t][direc - 1]
    vers.append([last[0] + mouv[0], last[1] + mouv[1]])
    direc = diff[t].index(mouv) + 1
