class Book:
	a = 0
	b = 0
	def __init__(self, a=0, b=0):
		self.a = a
		self.b = b
	def __str__(self):
		return "%s" % [self.a,self.b]
		
if __name__=="__main__":
	book = Book( 3, 4)
	print book
