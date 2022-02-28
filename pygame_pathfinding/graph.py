from re import I
from tkinter import W
from typing import Tuple, List

from .node import Node

import pygame
import math


class Graph:
    def __init__(
        self, width: int, height: int, pygame_rects: List[pygame.Rect] = []
    ) -> None:
        self.width = width
        self.height = height
        self._nodes = []

        for h in range(height):
            for w in range(width):
                self._nodes.append(Node(pygame.Vector2(w, h)))

    @property
    def nodes(self) -> List[Node]:
        return self._nodes

    def set_barrier(self, pos: pygame.Vector2) -> None:
        self._nodes[self.get_node_index(pos)].barrier = True

    def get_node_index(self, pos: pygame.Vector2) -> Node:
        i = 0
        for n in self.nodes:
            if n.pos.x == pos.x and n.pos.y == pos.y:
                return i
            i += 1

        return None

    def get_node(self, pos: pygame.Vector2) -> Node:
        for n in self.nodes:
            if n.pos.x == pos.x and n.pos.y == pos.y:
                return n

        return None

    def get_neighbor_nodes(self, node: Node) -> List[Node]:
        possible_neighbors = [
            pygame.Vector2(-1, 0),
            pygame.Vector2(1, 0),
            pygame.Vector2(0, -1),
            pygame.Vector2(0, 1),
        ]
        neighbors = []

        for p in possible_neighbors:
            neighbor_node = self.get_node(p + node.pos)
            if neighbor_node is not None and not neighbor_node.barrier:
                neighbors.append(neighbor_node)

        return neighbors

    def _reconstruct_path(self, came_from, current) -> None:
        total_path = [current]

        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        return total_path

    def get_path(self, start: pygame.Vector2, end: pygame.Vector2):
        start = self.get_node(start)
        end = self.get_node(end)

        open_nodes = [start]
        closed_nodes = []
        came_from = {}

        start.f = 0
        start.g = 0

        while len(open_nodes) != 0:

            def compare(e: Node) -> float:
                return e.f

            open_nodes.sort(key=compare)
            current = open_nodes[0]
            if current == end:
                return self._reconstruct_path(came_from, current)

            open_nodes.remove(current)
            closed_nodes.append(current)

            for neighbor in self.get_neighbor_nodes(current):
                if neighbor in closed_nodes:
                    continue
                tentative_g_score = current.g + current.get_node_dist(neighbor)

                if neighbor not in open_nodes or tentative_g_score < neighbor.g:
                    came_from[neighbor] = current
                    neighbor.g = tentative_g_score
                    neighbor.f = neighbor.g + neighbor.h
                    if neighbor not in open_nodes:
                        open_nodes.append(neighbor)

        raise Exception("Cannot find path")

    def print_visual(self) -> None:
        lines = []

        for h in range(self.height):
            line = ""
            for w in range(self.width):
                node = self.get_node(pygame.Vector2(w, h))
                if node.barrier:
                    line += "# "
                if not node.barrier:
                    line += f"{math.ceil(node.g)} "

            lines.append(line)

        for l in lines:
            print(l)
