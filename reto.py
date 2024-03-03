"""Reto de código en Python


"Alicia se encontró muy pequeña y vagando por el País de las Maravillas. Incluso la hierba que la rodeaba parecía un laberinto."

Este es un solucionador de laberintos diminutos.
Un laberinto está representado por una matriz

```json
[
    ['S', '0', '1'],
    ['1', '0', '1'],
    ['1', '0', 'E'],
]
```

S : Inicio del laberinto
E : Fin del laberinto
1 : Esto es un muro y no puedes pasar
0 : Espacio libre por el cual puedes moverte.

El objetivo es llegar al final del laberinto. Un laberinto resuelto tendrá una 'X' en el inicio, el camino y el final del laberinto, de la siguiente forma.

```json
[
   ['X', 'X', 1],
   ['1', 'X', 1],
   ['1', 'X', 'X']
]
```

Asume que la matriz proporcionada siempre tendrá los elementos S, E, 0 y 1 , cada matriz tendrá un mínimo de 3 valores y un máximo indeterminado.
"""

def solve_maze(maze):
    # Convert S and E to coordinates for easier manipulation
    start = [(index, row.index('S')) for index, row in enumerate(maze) if 'S' in row][0]
    end = [(index, row.index('E')) for index, row in enumerate(maze) if 'E' in row][0]
    
    def dfs(path, position):
        if position == end:
            # Mark the path from start to end
            for x, y in path:
                maze[x][y] = 'X'
            maze[end[0]][end[1]] = 'X'  # Ensure the end is marked as part of the path
            return True
        
        x, y = position
        # Directions: Down, Right, Up, Left
        directions = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
        
        for next_pos in directions:
            nx, ny = next_pos
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] in ['0', 'E'] and next_pos not in path:
                if dfs(path + [next_pos], next_pos):
                    return True
        
        return False
    
    # Initialize the search
    dfs([], start)
    
    # Convert the start point to 'X'
    maze[start[0]][start[1]] = 'X'
    
    return maze

def interact_with_user():
    print("Bienvenido al solucionador de laberintos. Por favor, introduce tu laberinto.")
    print("Usa 'S' para el inicio, 'E' para el final, '1' para los muros y '0' para los espacios libres.")
    print("Introduce cada fila del laberinto separada por comas. Por ejemplo: S,0,1")
    
    maze = []
    while True:
        row = input("Introduce una fila o escribe 'fin' para terminar: ")
        if row.lower() == 'fin':
            break
        maze.append(row.split(','))
    
    if not maze:
        print("No se proporcionó un laberinto. Terminando el programa.")
        return
    
    # Solve the maze
    solved_maze = solve_maze(maze)
    
    print("Laberinto resuelto:")
    for row in solved_maze:
        print(' '.join(row))

# Uncomment the line below to run the interaction with the user
# interact_with_user()
