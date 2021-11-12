from Command.Nann import P
from Command.read import readder
from Command.randomes import Randommer
from discord.ext import commands
import discord



def listeds(WORD):
        return [x for x in WORD]
        return k
class Bacis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.word_dontknow = readder('Documents\Work.xlsx')
        self.word_dontknow.read_Wordlist('Wordlist','ตอบ 1')


        self.word_dontknow_ = readder('Documents\Work.xlsx')
        self.word_dontknow_.read_Wordlist('Wordlist','เรียก ยัยซึน')
        
        self.word_calcu = readder('Documents\Work.xlsx')
        self.word_calcu.read_Wordlist('Wordlist','ตอบถามเลขมา')

        
        self.word_h = readder('Documents\Work.xlsx')
        self.word_h.read_Wordlist('Wordlist','คำ 3')

        self.word_he = readder('Documents\Work.xlsx')
        self.word_he.read_Wordlist('Wordlist','ตอบคำ3')

        self.a =Randommer()
        self.b = P()

    @commands.Cog.listener()
    async def on_message(self,message):
        msg=message.content

        if msg in [x for x in self.word_dontknow_.word]:
            await message.channel.send(f'{self.a.randoms(word=self.b.Nan(self.word_dontknow.word))}')
        try:
            await message.channel.send(f'{self.a.randoms(word=self.b.Nan(self.word_calcu.word))} ได้: ***{eval(msg)}***')
        except:
            pass
        if msg in [x for x in self.word_h.word]:

            await message.channel.send(f'{self.a.randoms(word=self.b.Nan(self.word_he.word))}')
        await self.bot.process_commands(message)



    
        
