import turtle

def draw_square():
    DEGREES_IN_CIRCLE = 360
    jacksStartAngle = 0

    window = turtle.Screen()
    window.bgcolor("black")
    
    jack = turtle.Turtle()

    jack.shape("turtle")
    jack.color("green")
    
    
    for i in range(0,DEGREES_IN_CIRCLE/10):
       for i in range(0,4):
           jack.forward(100)
           jack.right(90)
       jack.right(10)
       
    window.exitonclick

draw_square()
    
