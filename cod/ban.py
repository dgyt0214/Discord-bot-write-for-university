from tkinter.tix import TCL_IDLE_EVENTS
from discord import Interaction
from core.classes import Cog_Extension
import nextcord
import json
from nextcord.ext import commands
class ban(Cog_Extension):
  @commands.Cog.listener()
  async def on_member_join(self,mem):
    with open('test.json','r',encoding='utf8') as loli:
      loli1=json.load(loli)
      if mem.id in loli1['ban']:
        await mem.ban(reason='機器人行為')   
        c=self.bot.get_channel(978708780445495328)
        await c.send(f"{mem.mention}抓到你咯 還敢亂群")
      else:
        c=self.bot.get_channel(1026185931734130736)
        await c.send(f"{mem.mention} Welcome to MMU Discord Group Nice to Meet You.Dont forget take role at #1026277580233515008")
  
  @commands.command()
  @commands.is_owner()
  @commands.has_permissions(ban_members=True)
  async def ban(self,ctx,*,member,reason=None):
    c_r=member.replace('<','').replace('@','').replace('>','')
    c=str(c_r).split(' ')
    for c_kick in c:
        a=ctx.guild.get_member(int(c_kick))
        await a.ban(reason=reason)

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def join_ban(self,ctx,*,member):
    with open('test.json','r',encoding='utf8') as loli:
      loli1=json.load(loli)
    c_r=member.replace('<','').replace('@','').replace('>','')
  
    c=str(c_r).split(' ')
    for c_kick in c:
        loli1['ban'].append(int(c_kick))
    with open('test.json','w',encoding='utf8') as loli:
      json.dump(loli1,loli)

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def remove_ban(self,ctx,*,member):
    with open('test.json','r',encoding='utf8') as loli:
      loli1=json.load(loli)
    c_r=member.replace('<','').replace('@','').replace('>','')
  
    c=str(c_r).split(' ')
    for c_kick in c:
        loli1['ban'].remove(int(c_kick))
    with open('test.json','w',encoding='utf8') as loli:
      json.dump(loli1,loli)

def setup(bot):
    bot.add_cog(ban(bot))
   
