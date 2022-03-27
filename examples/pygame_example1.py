import pygame
import sys
import astarpy as pf

g = pf.Graph(20, 20)
g.set_barrier((9, 15))
g.set_barrier((10, 15))
g.set_barrier((11, 15))
g.set_barrier((12, 15))
g.set_barrier((13, 15))
g.set_barrier((14, 15))
g.set_barrier((15, 15))

pygame.init()
screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()

block_pos = (2, 1)
block_length = 25

rects = []

for n in g.nodes:
    rects.append(
        {
            "rect": pygame.Rect(
                n.pos[0] * block_length,
                n.pos[1] * block_length,
                block_length,
                block_length,
            ),
            "color": (255, 255, 255),
            "node": n,
        }
    )

path = g.get_path((2, 1), (15, 17))
next_path = 0
ms_to_next_path = 1000

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if pygame.time.get_ticks() > next_path:
        start = pygame.time.get_ticks()
        path = g.get_path((2, 1), (15, 17))
        end = pygame.time.get_ticks()
        print(f"it took {(end - start) / 1000}s to find a path")
        next_path = pygame.time.get_ticks() + ms_to_next_path

    for r in rects:
        if r["node"].barrier:
            color = (100, 0, 0)
        else:
            color = (255, 255, 255)

        if r["node"] in path:
            color = (0, 255, 0)

        pygame.draw.rect(
            screen,
            color,
            r["rect"],
        )

        if r["rect"].collidepoint(pygame.mouse.get_pos()):
            g.set_barrier(r["node"].pos)

    pygame.display.update()
    pygame.display.set_caption(f"astarpy (fps: {clock.get_fps()})")
    clock.tick(0)
