import pygame
import pygame_pathfinding as pf

g = pf.Graph(5, 4)
g.get_path(pygame.Vector2(2, 1), pygame.Vector2(4, 2))
g.set_barrier(pygame.Vector2(1, 1))

g.print_visual()
