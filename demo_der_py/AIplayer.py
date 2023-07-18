import torch
from torch import nn
class basemlp(nn.Moudle):
    def __init__(self,input_dim,output_dim) -> None:
        super().__init__()
        self.seq = nn.Sequential(
		 nn.Linear(input_dim,128),
        nn.LeakyReLU(),
        nn.Linear(128,256),
        nn.LeakyReLU(),
        nn.Tanh(),
        nn.Linear(256,output_dim),
        nn.LeakyReLU(), 
        nn.Softmax()
		)
    def forward(self,input):
        return self.seq(input)
        
class AIplayer():
    def __init__(self,name_path_arch) -> None:
        self.model = self.load_model(name_path_arch)
    def load_model(name_path_arch):
        # pesudo implementation
        input_dim = 20
        output_dim = 6
        return basemlp(input_dim,output_dim)

        