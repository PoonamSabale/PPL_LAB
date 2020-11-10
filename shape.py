import turtle
t = turtle.Turtle()

class polygon():
	def __init__(self, sides = 0, length = 0):
                self.sides = sides
                self.length = length

class triangle(polygon):
        def show(self):
                for i in range(3):
                        t.fd(self.length)
                        t.rt(120)


class square(polygon):
	def show(self):
		for i in range(4):	
			t.fd(self.length)
			t.rt(90)

class pentagon(polygon):
	def show(self):
		for i in range(5):
			t.fd(self.length)
			t.rt(72)

class hexagon(polygon):
        def show(self):
                for i in range(6):
                        t.fd(self.length)
                        t.rt(60)

class octagon(polygon):
        def show(self):
                for i in range(8):
                        t.fd(self.length)
                        t.rt(45)


class circle():
	def __init__(self, radius = 50):
		self.radius = radius
	def show(self):
		t.hideturtle()
		t.circle(self.radius)

t1 = triangle(3, 90)
t1.show()
turtle.Screen().reset()
s1 = square(4, 150)
s1.show()
turtle.Screen().reset()
p1 = pentagon(5, 200)
p1.show()
turtle.Screen().reset()
c1 = circle(90)
c1.show()
turtle.Screen().reset()
o1 = octagon(8, 200)
o1.show()

turtle.done()
