import pandas as pd
import os 
class readder:
    def __init__(self,Path_File):
        self.file = Path_File
        self.isFile = None
        self.Token = None
        self.Token_ed =''
        self.Count = 0
        self.word =None
        self.words_cd = 0

    def oschaack(self,N=0):
        if os.path.isfile(self.file):
            self.isFile = os.path.join(self.file)
            if N ==True:
                print('Reading File:',self.isFile)
                N=None
            return True
        else:
            print(f'Not Find File in {self.file}')
            return False
    
    def read_Token(self,Sheet_name,Headcolumn_Name,isToken=0,Showpathfile=True):
        if self.oschaack(Showpathfile):
            try:
                Token_= pd.read_excel(self.file,sheet_name=Sheet_name)
                self.Token = Token_[Headcolumn_Name][isToken]
                return True
            except:
                print(f'Error:\nSheet_name="{Sheet_name}", Headcolumn_Name="{Headcolumn_Name}"  Some one Wrong! Or All Wrong!')
                return False
        else:
            return False

    def consored_Token(self,CountNumber_Show=0):
        for x in self.Token:
            self.Count += 1
            if self.Count >CountNumber_Show:
                self.Token_ed += '*'
            else:
                self.Token_ed += x
        return self.Token_ed
    def read_Wordlist(self,Sheet_name,Headcolumn_Name):
        if self.oschaack():
            try:
                word = pd.read_excel(self.file,sheet_name=Sheet_name)
                self.word = word[Headcolumn_Name]
                return True
            except:
                print(f'Error:\nSheet_name="{Sheet_name}", Headcolumn_Name="{Headcolumn_Name}"  Some one Wrong! Or All Wrong!')
                return False

    def word_c(self):
        self.words_cd = len(self.word)
        return self.words_cd