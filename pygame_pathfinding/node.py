import math
import pygame


class Node:
    def __init__(self, pos: pygame.Vector2) -> None:
        self.pos = pos

        """
        G is the distance between the current node and the start node.
        H is the heuristic — estimated distance from the current node to the end node.
        """
        self.g = 0
        self.h = 0
        self.f = 0
        
        self.barrier = False

    def get_node_dist(self, node) -> None:
        return math.sqrt(
            (self.pos.x - node.pos.x) ** 2 + (self.pos.y - node.pos.y) ** 2
        )
    
    def __str__(self) -> str:
        return f"Node({self.pos.x}, {self.pos.y}, isbarrier: {self.barrier})"
    
    def __hash__(self):
        return hash(str(self))

    def __eq__(self, __o) -> bool:
        if __o is None:
            return False

        return self.pos.x == __o.pos.x and self.pos.y == __o.pos.y
