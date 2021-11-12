import discord
from discord.ext import commands
from Command.read import readder
from Command.bacis import Bacis

Me = readder('Documents\Work.xlsx')

if Me.read_Token(Sheet_name='Token',Headcolumn_Name='Token',isToken=0,Showpathfile=True):
    print(Me.consored_Token(CountNumber_Show=5))
    bot=commands.Bot(command_prefix='-')

    @bot.event
    async def on_ready():
        print('Running.......')
    bot.add_cog(Bacis(bot))
    bot.run(Me.Token)