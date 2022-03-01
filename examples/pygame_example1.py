import pygame
import sys
import pygame_pathfinding as pf

g = pf.Graph(20, 20)
g.set_barrier(pygame.Vector2(4, 2))
g.set_barrier(pygame.Vector2(3, 2))
g.set_barrier(pygame.Vector2(2, 2))
g.set_barrier(pygame.Vector2(1, 2))
g.set_barrier(pygame.Vector2(12, 8))
g.set_barrier(pygame.Vector2(12, 9))
g.set_barrier(pygame.Vector2(12, 10))
g.set_barrier(pygame.Vector2(12, 11))
g.set_barrier(pygame.Vector2(12, 12))
g.set_barrier(pygame.Vector2(12, 13))
g.set_barrier(pygame.Vector2(12, 14))
g.set_barrier(pygame.Vector2(12, 15))

pygame.init()
screen = pygame.display.set_mode((640, 640))

block_pos = pygame.Vector2(2, 1)
path = g.get_path(pygame.Vector2(2, 1), pygame.Vector2(15, 17))
block_length = 25

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    for n in g.nodes:
        if n.barrier:
            color = (100, 0, 0)
        else:
            color = (255, 255, 255)
        
        if n in path:
            color = (0, 255, 0)
        
        pygame.draw.rect(
            screen,
            color,
            (
                n.pos.x * block_length,
                n.pos.y * block_length,
                block_length,
                block_length,
            ),
        )

    pygame.display.update()
