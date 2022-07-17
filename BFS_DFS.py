#Name: Talha Mustafa
#Roll No: 18I-0573
#Section: D

path = []
#Function To Print Maze
def printMatrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end="\t")
        print("")

#Function to Check Maze Path if the provided position in within the maze
def CheckPath(current, maze, cost):
    i, j = current
    rows = len(maze)
    cols = len(maze[0])

    return ((i >= 0) and (i < rows) and (j >= 0) and (j < cols)) and (maze[i][j] == cost - 1)

#Find Optimal Path
def FindPath(maze, end):
    i, j = end
    result = []
    cost = maze[i][j]
    temp = i, j
    result.append(temp)
    
    while cost > 1:
        if (CheckPath((i - 1,j),maze,cost)):
            i, j = i - 1, j
        elif (CheckPath((i,j - 1),maze,cost)):
            i, j = i, j - 1
        elif (CheckPath((i,j + 1),maze,cost)):
            i, j = i, j + 1
        elif (CheckPath((i + 1,j),maze,cost)):
            i, j = i + 1, j

        temp = i, j
        result.append(temp)
        cost -= 1
        
    return result

#Node Class To store state in maze and the cost to reach it
class Node:
    def __init__(self, state, cost):
        self.state = state
        self.cost = cost


#Function to Check Maze Neighbours if the provided position in within the maze
def CheckNeighbours(current, maze, visited):
    i, j = current
    rows = len(maze)
    cols = len(maze[0])

    if(current not in visited):
        return ((i >= 0) and (i < rows) and (j >= 0) and (j < cols))
    else:
        return False

#Search neighbours of given position
def SearchNeighbours(maze, current, queue, visited):

    i, j = current.state
    neighbours = []

    #UP
    if (CheckNeighbours((i - 1 , j),maze,visited) and maze[i - 1][j] == 1):
        temp = i - 1,j
        neighbours.append(Node(temp, current.cost+1))
        path[i-1][j] = current.cost + 1

    #LEFT
    if (CheckNeighbours((i,j - 1),maze,visited) and maze[i][j - 1] == 1):
        temp = i, j - 1
        neighbours.append(Node(temp, current.cost + 1))
        path[i][j - 1] = current.cost + 1

    #RIGHT
    if (CheckNeighbours((i,j + 1),maze,visited) and maze[i][j + 1] == 1):
        temp = i, j + 1
        neighbours.append(Node(temp, current.cost + 1))
        path[i][j + 1] = current.cost + 1

    #DOWN
    if (CheckNeighbours((i + 1,j),maze,visited) and maze[i + 1][j] == 1):
        temp = i + 1, j
        neighbours.append(Node(temp, current.cost+1))
        path[i + 1][j] = current.cost + 1

    return neighbours

#Apply BFS or DFS on the maze(use the algo parameter to select which func to call)
def SearchMaze(maze, start, end, algo):
    row, col = start
    end_row, end_col = end
    if(maze[row][col] != 1 or maze[end_row][end_col] != 1):
        return -1

    total = 0
    visited = []
    arr = []
    arr.append(Node(start,0))

    while(arr):
        temp = arr.pop(0)
        if(temp.state == end):
            visited.append(temp.state)
            return (total,visited)

        if(temp.state not in visited):

            visited.append(temp.state)
            neighbours = SearchNeighbours(maze, temp, arr, visited)
            #Adding New Neighbours at start in case of DFS
            if(algo == "DFS"):
                #neighbours.reverse()
                neighbours.extend(arr)
                arr = neighbours
            #Adding New Neighbours at end in case of BFS
            elif(algo == "BFS"):
                arr.extend(neighbours)
            else:
                return -1

            total += 1

    return -1

def main():

    maze = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    #Provide starting and ending points of maze
    start = (4,11)
    end = (10,0)

    global path
    path = [[0] * len(maze) for _ in range(len(maze))]

    print("\t\t\t    === MAZE ===   \t\t\t")
    printMatrix(maze)
    print("\t\t\t    ============   \t\t\t")

    flag = True
    result = SearchMaze(maze,start,end,"BFS")
    if(result == -1):
        print("Invalid.")
        flag = False
    else:
        print("BFS Search Cost: ", result[0])
        print("BFS Search Path: ", result[1])
        print("=========")

    result = SearchMaze(maze,start,end,"DFS")
    if (result == -1):
        print("Invalid.")
        flag = False
    else:
        print("DFS Search Cost: ", result[0])
        print("DFS Search Path: ", result[1])
        print("=========")

    if(flag):
        path_result = FindPath(path, end)
        print("Optimal Path Cost: ", len(path_result))
        print("Optimal Path: ",path_result)


if __name__ == "__main__":
    main()