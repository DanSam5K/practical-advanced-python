import turtle

START= "S"
OBSTACLE = "+"
TRIED = "."
DEAD_END = "_"
PART_OF_PATH = "O"

class Maze:
    def __init__(self, maze_filename):
        with open(maze_filename, "r") as maze_file:
            self.maze_list = [
                [ch for ch in line.rstrip("\n")] for line in maze_file.readlines()
            ]
        self.rows_in_maze = len(self.maze_list)
        self.columns_in_maze = len(self.maze_list[0])
        for row_idx, row in enumerate(self.maze_list):
            if START in row:
                self.start_row = row_idx
                self.start_col = row.index(START)
                break
        
        self.x_translate = -self.columns_in_maze / 2
        self.y_translate = self.rows_in_maze / 2
        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(
            -(self.columns_in_maze - 1) / 2 - 0.5,
            -(self.rows_in_maze - 1) / 2 - 0.5,
            (self.columns_in_maze - 1) / 2 + 0.5,
            (self.rows_in_maze - 1) / 2 + 0.5,
        )

    def draw_maze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(
                        x + self.x_translate, -y + self.y_translate, "orange"
                    )
        self.t.color("black")
        self.t.fillcolor("blue")
        self.wn.update()
        self.wn.tracer(1)

    def draw_centered_box(self, x, y, color):
        self.t.up()
        self.t.goto(x - 0.5, y - 0.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
        

    def update_position(self, row, col, val=None):
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            color = "green"
        elif val == OBSTACLE:
            color = "red"
        elif val == TRIED:
            color = "black"
        elif val == DEAD_END:
            color = "red"
        else:
            color = None

        if color:
            self.drop_bread_crumb(color)

    def move_turtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate, -y + self.y_translate))
        self.t.goto(x + self.x_translate, -y + self.y_translate)

    def drop_bread_crumb(self, color)
        self.t.dot(10, color)

    def is_exit(self, row, col):
        return(
            row == 0 or row == self.rows_in_maze - 1 or col == 0 or col == self.columns_in_maze - 1
        )
        
    def __getitem__(self, idx):
        return self.maze_list[idx]
    
    
def search_from(maze, row, column):
    # Try each of four directions from this point until we find a way out.
    maze.update_position(row, column)
    # Base Case return values:
    # 1. We have run into an obstacle, return false
    if maze[row][column] in OBSTACLE:
        return False
    # 2. We have found an already explored square
    if maze[row][column] in [TRIED, DEAD_END]:
        return False
    # 3. We have found exit
    if maze.is_exit(row, column):
        maze.update_position(row, column, PART_OF_PATH)
        return True
    maze.update_position(row, column, TRIED)
    # Otherwise, use logical short circuiting to try each direction
    # in turn (if needed)
    found = (
        search_from(maze, row - 1, column) or search_from(maze, row + 1, column) or search_from(maze, row, column - 1) or search_from(maze, row, column + 1) 
    )

    if found:
        maze.update_position(row, column, PART_OF_PATH)
    else:
        maze.update_position(row, column, DEAD_END)
    return found