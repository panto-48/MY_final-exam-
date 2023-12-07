import turtle
import random

Choice = input("Which art do you want to generate? Enter a number between 1 to 8,inclusive: ")

def draw_polygon(num_sides, size, orientation, location, color, border_size):
    turtle.penup()
    turtle.goto(location[0], location[1])
    turtle.setheading(orientation)
    turtle.color(color)
    turtle.pensize(border_size)
    turtle.pendown()
    for _ in range(num_sides):
        turtle.forward(size)
        turtle.left(360/num_sides)
    turtle.penup()

def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

# draw a polygon at a random location, orientation, color, and border line thickness
num_sides = random.randint(3, 5) # triangle, square, or pentagon
#Lock the shape
if Choice == "1"or Choice =="5" :
    num_sides = 3
if Choice == "2"or Choice =="6" :
    num_sides = 4
if Choice == "3"or Choice =="7" :
    num_sides = 5
if Choice == "4"or Choice =="8" :
    pass

size = random.randint(50, 150)
orientation = random.randint(0, 90)
location = [random.randint(-300, 300), random.randint(-200, 200)]
color = get_new_color()
border_size = random.randint(1, 10)
draw_polygon(num_sides, size, orientation, location, color, border_size)

# specify a reduction ratio to draw a smaller polygon inside the one above
#if 
reduction_ratio = 0.618

# reposition the turtle and get a new location
turtle.penup()
turtle.forward(size*(1-reduction_ratio)/2)
turtle.left(90)
turtle.forward(size*(1-reduction_ratio)/2)
turtle.right(90)
location[0] = turtle.pos()[0]
location[1] = turtle.pos()[1]

# adjust the size according to the reduction ratio
size *= reduction_ratio
draw_polygon(num_sides, size, orientation, location, color, border_size)

#Choice and Shape
if Choice == "1" or Choice == "2" or Choice == "3" or Choice == "4":
    if Choice == "4":
        for i in range(random.randint(30, 50)) :
            num_sides2 = random.randint(3, 5)
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = get_new_color()
            border_size = random.randint(1, 7)
            draw_polygon(num_sides2, size, orientation, location, color, border_size)
    else :    
        for i in range(random.randint(30, 50)) :
            num_sides2 = num_sides # triangle, square, or pentagon
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = get_new_color()
            border_size = random.randint(1, 7)
            draw_polygon(num_sides2, size, orientation, location, color, border_size)
elif Choice == "5" or Choice == "6" or Choice == "7" or Choice == "8":
    if Choice == "8":
        for i in range(random.randint(20, 30)) :
            num_sides2 = random.randint(3, 5)
            size = random.randint(50, 150)
            size *= reduction_ratio
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = get_new_color()
            border_size = random.randint(1, 7)
            draw_polygon(num_sides2, size, orientation, location, color, border_size)
            size *= reduction_ratio
            turtle.penup()
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            draw_polygon(num_sides2, size, orientation, location, color, border_size)
            size *= reduction_ratio
            turtle.penup()
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            draw_polygon(num_sides2, size, orientation, location, color, border_size)
    else :    
        for i in range(random.randint(20, 30)) :
            num_sides2 = num_sides # triangle, square, or pentagon
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = get_new_color()
            border_size = random.randint(1, 7)
            draw_polygon(num_sides2, size, orientation, location, color, border_size)
            size *= reduction_ratio
            turtle.penup()
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            draw_polygon(num_sides2, size, orientation, location, color, border_size)
            size *= reduction_ratio
            turtle.penup()
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            draw_polygon(num_sides2, size, orientation, location, color, border_size)
            

# draw the second polygon embedded inside the original 

# hold the window; close it by clicking the window close 'x' mark
turtle.done()





