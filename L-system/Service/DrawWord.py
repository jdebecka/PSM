import turtle


class Draw_Path:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.bgcolor("light blue")
        self.window.title("L-System")
        self.robot = turtle.Turtle()
        self.angle = 25
        self.stack = []
        self.distance = 10

    def draw(self, word):
        # symbols = ["X", "F", "+", "-", "[", "]"]
        self.init()
        for letter in word:
            if letter == "F":
                self.robot.forward(self.distance)
                self.robot.pencolor('red')
            if letter == "X":
                self.robot.penup()
                self.robot.forward(self.distance)
                self.robot.pendown()
                self.robot.pencolor('green')
            if letter == "[":
                self.stack.append((self.robot.heading(), self.robot.pos()))
            if letter == "]":
                head, pos = self.stack.pop()
                self.robot.penup()
                self.robot.goto(pos)
                self.robot.setheading(head)
                self.robot.pendown()
                self.robot.dot()
            if letter == "+":
                self.robot.left(self.angle)
            if letter == "-":
                self.robot.right(self.angle)
        turtle.done()

    def check_boundary(self):
        if self.robot.pos() > self.window.window_height() or self.window.window_width():
            self.robot.right(180)

    def init(self):
        self.robot.left(self.angle)
        self.robot.speed(0)
        self.robot.hideturtle()
        self.robot.penup()
        self.robot.setpos(-self.window.window_width()/2, -self.window.window_height()/2)
        self.robot.showturtle()
        self.robot.pendown()