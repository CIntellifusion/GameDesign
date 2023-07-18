import numpy as np 
from tqdm import tqdm,trange
class board():
    def __init__(self) -> None:
        # register location 
        self.board = np.zeros(100).astype(int).reshape(10,10)
        self.unitlist = []

class player():
	def __init__(self,campid) -> None:	
		self.campid = campid

def place_units(player1,player2):
    

def run(player1,player2,rounds = 10):
    playground = board()
    # place units
    for i in trange(rounds):
        
        pass
    
