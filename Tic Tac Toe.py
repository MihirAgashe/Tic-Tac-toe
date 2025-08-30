import turtle
screen = turtle.Screen()
screen.setup(800 , 800)
tracer = turtle.Turtle()
tracer.hideturtle()
def state_of_box():
   for row in grid:
      for col in row:
         print(col.state )



 
class GridTurtle(turtle.Turtle):
  count = 9
  turn = 'X'
  end_game= False
  def __init__(
      self,
      x: int,
      y: int,
      color: str = "#D3D3D3"
  ):
     
    super().__init__(
        shape="square"
    )
    self.state= None
    self.x = x
    self.y = y
    self.speed(0)
    self.penup()
    self.goto(x, y)
    self.shapesize(10, 10, 2)
    self.color("black", color)
    self.fillcolor()
    self.used=False
    self.onclick(self.handle_click)
    


  def handle_click(self, x, y):
       if GridTurtle.end_game:
           return
       
       
       if self.used:
          return
       self.used=True
       self.state=GridTurtle.turn
       tracer.penup()
       tracer.goto(self.xcor() ,self.ycor())
       tracer.pendown()
       tracer.pendown()
       tracer.setheading(0)
       tracer.pensize(5)
       tracer.shape('turtle')

       if GridTurtle.turn == 'X':
            tracer.color('Red')
            tracer.right(45)
            tracer.fd(50)
            tracer.back(100)
            tracer.fd(50)
            tracer.left(90)
            tracer.fd(50)
            tracer.back(100)
            GridTurtle.turn = 'O'
       else:
            tracer.color('blue')
            tracer.penup()
            tracer.goto(self.xcor(), self.ycor() - 50)
            tracer.setheading(0)
            tracer.pendown()
            tracer.circle(50)
            GridTurtle.turn = 'X'


       tracer.penup()
       tracer.setheading(0)
       check_row(int(self.x/200),int( self.y/200))
       check_col(int(self.x/200),int( self.y/200))
       check_mdiag(int(self.x/200),int( self.y/200))
       check_adiag(int(self.x/200),int( self.y/200))
       GridTurtle.count -= 1
       if GridTurtle.count == 0:
           print('Draw')
           end_game()
       
           
       
       
       
def check_row(i, j):
   row=grid[i]
   ref_state=row[0].state
   if ref_state == None:
      return
   for box in row:
      if box.state != ref_state:
         return
   else:
         print(f"{ref_state} win")
         end_game()

def check_col(i, j):
    ref_state = grid[0][j].state  
    if ref_state is None:
        return
    for row in grid:
        if row[j].state != ref_state:
            return
    else:
        print(f"{ref_state} win")
        end_game()

def check_mdiag(i, j):    
    if i == j:
        ref_state =grid[0][0].state
        if ref_state is None:
            return
        for D in range(3):
            if grid[D][D].state != ref_state:
                return
        else:
            print(f"{ref_state} win")
            end_game()

def check_adiag(i, j ):
    if int(i) + int(j) == 2:
        ref_state=grid[0][2].state
        if ref_state is None:
            return 
        for D in range (3):
            if grid[D][2-D].state != ref_state: 
                return
        else:
                print(f"{ref_state} win")
                end_game()

def end_game():
    GridTurtle.end_game = True
    print("END")



   
  
       
grid: list[list[GridTurtle]] = []

for i in range(3):
   grid_list: list[GridTurtle] = []
   for j in range(3):
      grid_list.append(GridTurtle(i * 200,j * 200))
   grid.append(grid_list)



turtle.mainloop()


   
      
turtle.done() 



