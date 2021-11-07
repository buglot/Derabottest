from read import readder
import random

class Randommer:
    def __init__(self,word):
        self.name=None
        self.word = word
        self.randomed = None
    def randoms(self):
        Ranme = random
        self.randomed =Ranme.choice(self.word)
        return self.randomed 
        