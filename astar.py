import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f

def heuristic(node, end):
    return abs(node.position[0] - end.position[0]) + abs(node.position[1] - end.position[1])

def astar(grid, start, end):
    open_list = []
    closed_list = set()

    start_node = Node(start)
    end_node = Node(end)
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        yield grid, current_node.position, "current"

        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            yield grid, path, "path"
            return path[::-1]

        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for new_position in neighbors:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if (0 <= node_position[0] < len(grid) and 
                0 <= node_position[1] < len(grid[0]) and
                grid[node_position[0]][node_position[1]] == 0):

                new_node = Node(node_position, current_node)

                if new_node.position in closed_list:
                    continue

                new_node.g = current_node.g + 1
                new_node.h = heuristic(new_node, end_node)
                new_node.f = new_node.g + new_node.h

                if any(open_node.position == new_node.position and open_node.g <= new_node.g for open_node in open_list):
                    continue

                heapq.heappush(open_list, new_node)
                yield grid, new_node.position, "open"

    yield grid, None, "no_path"
