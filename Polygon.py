
class Polygon:

	def __init__(self, number_of_sides,*args, **kwargs):
		self.number_of_sides = number_of_sides
		self.sides = [0 for i in range(number_of_sides)]


	def input_sides(self):
		for i in range(self.number_of_sides):
			self.sides[i] = float(input('Enter sides'+str(i+1)+":"))

	def display_sides(self):
		for i in range(self.number_of_sides):
			print("Sides",i+1,"is",self.sides[i])

		print(self.sides)



class Triangle(Polygon):

	def __init__(self):
		Polygon.__init(self,3)

	def find_area(self):
		a,b,c = self.sides
		#caluculate the semi-perimeter
		s= (a+b+c) / 2
		area = (s*(s-a)*(s-b)*(s-c)) **0.5
		print("This area of the triangle is %0.2f" %area)

