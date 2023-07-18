
class UNIT():
	def __init__(self) -> None:
		# attributes
		self.type	= "UNIT"
		self.camp = -1
		self.id = -1
		self.cost = -1
		self.maxhp = -1
		self.speed = -1
		self.attack = -1 
		self.attack_range = -1
		self.crthp	= -1
		# functions 
	def update_hp(self,mount:int):
		self.crthp+=mount
 	
def Attack(A:UNIT,B:UNIT):
	B.update_hp(-A.attack)
	return 

class Warrior(UNIT):
	def __init__(self,id,camp) -> None:
		super().__init__()
		self.type = "warrior"
		self.id = id 
		self.camp = camp 
		self.cost = 1
		self.maxhp = 20
		self.speed = 2
		self.attack = 2
		self.attack_range = 1 # mahattan distance
		self.crthp	= self.maxhp
		
	 
class cavalry(UNIT):
	def __init__(self,id,camp) -> None:
		super().__init__()
		self.type = "cavalry"
		self.id = id
		self.camp = camp 
		self.cost = 3
		self.maxhp = 15

		self.speed = 2
		self.attack = 3
		self.attack_range = 5
		self.crthp	= self.maxhp

	 
class archer(UNIT):
	def __init__(self,id,camp) -> None:
		super().__init__()
		self.type = "archer"
		self.id = id 
		self.camp = camp 
		self.cost = 5	
	
		self.maxhp = 15
		self.speed = 2
		self.attack = 5
		self.attack_range = 2
		self.crthp	= self.maxhp
