class P:
    def __init__(self):
        self.word = None
    def Nan(self,Word):
        self.word =[]
        for x in Word:
            if type(x) != float:
                self.word.append(x)
        return self.word