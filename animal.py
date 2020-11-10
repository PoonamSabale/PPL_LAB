class Animal:
	def __init__(self, legs = 4, eyes = 2, tail = 1, ears = 2):
		self.legs = legs
		self.eyes = eyes
		self.tail = tail
		self.ears = ears
 
class Wild_animals(Animal):
	def place(self):
		print('jungle')

class Domestic_animals(Animal):
	def __init__(self, legs = 4, eyes = 2, tail = 1, ears = 2):
		Animal.__init__(self, legs = 4, eyes = 2, tail = 1, ears = 2)
	def place(self):
		print("Areas habitated by humans")


class herbivores(Wild_animals):
	def  __init__(self, legs = 4, eyes = 2, tail = 1, ears = 2):
		super().__init__(legs = 4, eyes = 2, tail = 1, ears = 2)
	def food(self):
                print("leaves")

class carnivores(Wild_animals):
	def food(self):
		print("meat") 

class tiger(carnivores):
    def speak(self):
        print("Roar")
    def colour(self):
        print("Yellowish Orange and black stripes")

class lion(carnivores):
    def speak(self):
        print("Roar")
    def colour(self):
        print("Yellow")
        
class deer(herbivores):
    def colour(self):
        print("Brown")
        
class elephant(herbivores):
	def speak(self):
		print("trumpet")
	def colour(self):
		print("Grey")
	def food(self):
		herbivores().food()  #overloading
		print("grass")

class zebra(herbivores):
    def colour(self):
        print("Black and white")

class dog(Domestic_animals):
    def speak(self):
        print("bark")
    def colour(self):
        print("brown, black, white, golden")


class cat(Domestic_animals):
    def speak(self):
        print("meow")
    def colour(self):
        print("Grey,brown, black, white")
        
        
class cow(Domestic_animals):
    def speak(self):
        print("moo")
    def colour(self):
        print("white, brown,etc")


tom = cat()
print("tom.legs = ", tom.legs)
print("tom.place = ")
tom.place()
print("tom.colour = ") 
tom.colour()
print("tom.speak = ") 
tom.speak()
ele1 = elephant()
print("ele1.legs = ", ele1.legs)
print("ele1.food = ")
ele1.food()
