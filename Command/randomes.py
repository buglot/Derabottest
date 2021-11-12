
import random

class Randommer:
    def __init__(self):
        self.name=None
        self.randomed = None
    def randoms(self,word):
        Ranme = random
        self.word = word
        self.randomed =Ranme.choice(self.word)
        return self.randomed 
        