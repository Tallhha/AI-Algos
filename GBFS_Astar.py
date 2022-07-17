# Name: Talha Mustafa
# Roll No: 18I-0573
# Section: D

# Function To Print Maze
def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end="\t")
        print("")


# Check if a neigbour should be added to arr list
def in_open(arr, neigbour):
    for node in arr:
        if neigbour == node and neigbour.f >= node.f:
            return False
    return True


# This Function is taken from sample function given in Lab-06
# This class represent a node
class Node:

    # Initialize the class
    def __init__(self, index, parent, cost):
        self.index = index
        self.parent = parent
        self.cost = cost
        self.g = 0  # Distance to start node
        self.h = 0  # Distance to goal node
        self.f = 0  # Total cost

    # Compare nodes
    def __eq__(self, other):
        return self.index == other.index

    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f

    # Print node
    def __repr__(self):
        return '({0},{1})'.format(self.index, self.f)


# Function to Check Maze Neighbours if the provided position in within the maze
def check_neighbours(current, maze, visited):
    i, j = current.index
    rows = len(maze)
    cols = len(maze[0])

    if current not in visited:
        return (i >= 0) and (i < rows) and (j >= 0) and (j < cols)
    else:
        return False


# Search neighbours of given position
def search_neighbours(current, maze, visited):
    i, j = current.index
    neighbours = []

    # UP
    if check_neighbours(Node((i - 1, j), None, 0), maze, visited) and maze[i - 1][j] == 1:
        temp = i - 1, j
        neighbours.append(Node(temp, current, current.cost + 1))

    # LEFT
    if check_neighbours(Node((i, j - 1), None, 0), maze, visited) and maze[i][j - 1] == 1:
        temp = i, j - 1
        neighbours.append(Node(temp, current, current.cost + 1))

    # RIGHT
    if check_neighbours(Node((i, j + 1), None, 0), maze, visited) and maze[i][j + 1] == 1:
        temp = i, j + 1
        neighbours.append(Node(temp, current, current.cost + 1))

    # DOWN
    if check_neighbours(Node((i + 1, j), None, 0), maze, visited) and maze[i + 1][j] == 1:
        temp = i + 1, j
        neighbours.append(Node(temp, current, current.cost + 1))

    return neighbours


# Functions to apply Algorithms
def search_maze(maze, start, end, algo):

    arr = []
    visited = []
    total = 0

    start_node = Node(start, None, 0)
    goal_node = Node(end, None, 0)

    # Distance of start node from goal node
    start_node.f = abs(start_node.index[0] - goal_node.index[0]) + abs(start_node.index[1] - goal_node.index[1])

    arr.append(start_node)
    while arr:

        arr.sort()
        current_node = arr.pop(0)

        if current_node == goal_node:
            result = []
            while current_node != start_node:
                result.append(current_node)
                current_node = current_node.parent
            result.append(start_node)

            return total, result[::-1]

        neigbours = search_neighbours(current_node, maze, visited)

        for neigbour in neigbours:
            neigbour.g = current_node.cost
            neigbour.h = abs(neigbour.index[0] - goal_node.index[0]) + abs(neigbour.index[1] - goal_node.index[1])

            if algo == "A*":
                neigbour.f = neigbour.g + neigbour.h
            elif algo == "GBFS":
                neigbour.f = neigbour.h
            else:
                return -1

            if in_open(arr, neigbour):
                arr.append(neigbour)

        if current_node not in visited:
            total += 1

        visited.append(current_node)

    return -1


def main():
    maze = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    # Provide starting and ending points of maze
    start = (14, 0)
    end = (12, 19)

    print("\t\t\t    =========== MAZE ===========   \t\t\t")
    print_matrix(maze)
    print("\t\t\t    =========================================   \t\t\t")

    result = search_maze(maze, start, end, "A*")
    if result == -1:
        print("Invalid.")
    else:
        print("Algorithm: A*")
        print("Path(Position, Distance(f)): \n", result[1])
        print("Number of Moves: ", result[0])
        print("Path Cost: ", len(result[1]) - 1)
        print("======================================================")

    result = search_maze(maze, start, end, "GBFS")
    if result == -1:
        print("Invalid.")
    else:
        print("Algorithm: GBFS")
        print("Path(Position, Distance(h)): \n", result[1])
        print("Number of Moves: ", result[0])
        print("Path Cost: ", len(result[1]) - 1)
        print("======================================================")


if __name__ == "__main__":
    main()
