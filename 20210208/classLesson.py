class Human:
	def __init__(self,name,year,birth):
		self.name=name
		self.year=year
		self.birth=birth
	def introduce(self):
		return f'私の名前は{self.name}。今年で{self.year}歳'
	def grow_old(self,after):
		self.year+=after
	
human1=Human('KAWADA',26,'19931013')
print(human1.name,human1.year)
print(human1.introduce())
human2=Human('YAMADA',30,'19890703')
print(human2.name,human2.year)
print(human2.introduce())
human2.grow_old(2)
print(human2.introduce())

class HumanHealth(Human):
	def __init__(self,name,year,birth,height,weight):
		super().__init__(name,year,birth)

		self.height=height
		self.weight=weight
	
	def get_bmi(self):
		return round(self.weight/(self.height**2),2)
	
	def introduce(self):
		return super().introduce()+f'BMIは{self.get_bmi()}'
		

human3=HumanHealth('Souma',26,'19931013',1.74,69)
print(human3.height)
print(human3.weight)
print(human3.get_bmi())
print(human3.introduce())

