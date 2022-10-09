from core.classes import Cog_Extension
import nextcord
import json
from nextcord.ext import commands
class role (Cog_Extension):
  @commands.command(name='testhi')
  async def sendmenu1(self,ctx):
      async def callback1(interaction):
          if "gif2" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1026695416252727346)#Faculty of IT
            await interaction.user.add_roles(r_role)
          if "gif3" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1026278155364868107)#Faculty of Managment
            await interaction.user.add_roles(r_role)
          if "gif6" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1026278523733823508)#Faculty of Law
            await interaction.user.add_roles(r_role)
          if "gif7" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1026281584984334386)#Faculty of Buisness
            await interaction.user.add_roles(r_role)
          if "gif8" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1026278800952144023)#Faculty of Enineering
            await interaction.user.add_roles(r_role)
          if "gif9" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1026278975493910538)#Faculty of Creative Multimedia
            await interaction.user.add_roles(r_role)
            
      ts3=nextcord.SelectOption(label="Faculty of IT",value="gif2",description="")
      ts4=nextcord.SelectOption(label="Faculty of Management",value="gif3",description="")
      ts7=nextcord.SelectOption(label="Faculty of Law",value="gif6",description="")  
      ts8=nextcord.SelectOption(label="Faculty in Business",value="gif7",description="")  
      ts9=nextcord.SelectOption(label="Faculty of Engineering & Technology",value="gif8",description="")  
      ts10=nextcord.SelectOption(label="Faculty of Creative Multimedia",value="gif9",description="")  
      dropdown=nextcord.ui.Select(placeholder="Please Choose Your Course Ty~",options=[ts3,ts4,ts7,ts8,ts9,ts10],max_values=1)
      dropdown.callback=callback1
      value1=nextcord.ui.View()
      value1.add_item(dropdown)
      await ctx.send("Get Your Course Role here,after choosing you will see your course channel",view=value1)

  @commands.command(name='removehi')
  async def sendmenu2(self,ctx):
      async def callback1(interaction):
          if  "gif2" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1026695416252727346)#Faculty of IT
            await interaction.user.remove_roles(r_role)
          if "gif3" in dropdown.values :
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1026278155364868107)#特殊性癖
            await interaction.user.remove_roles(r_role)
          if "gif6" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1026278523733823508)#專業技術交流
            await interaction.user.remove_roles(r_role)
          if "gif7" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1026281584984334386)#日文交流
            await interaction.user.remove_roles(r_role)
          if "gif8" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1026278800952144023)#原神樂譜
            await interaction.user.remove_roles(r_role)
          if "gif9" in dropdown.values:
            b_g=self.bot.get_guild(interaction.guild_id)
            r_role=b_g.get_role(1026278975493910538)#崩壞
            await interaction.user.remove_roles(r_role)
      ts3=nextcord.SelectOption(label="Faculty of IT",value="gif2",description="")
      ts4=nextcord.SelectOption(label="Faculty of Management",value="gif3",description="")
      ts7=nextcord.SelectOption(label="Faculty of Law",value="gif6",description="")  
      ts8=nextcord.SelectOption(label="Faculty in Business",value="gif7",description="")  
      ts9=nextcord.SelectOption(label="Faculty of Engineering & Technology",value="gif8",description="")  
      ts10=nextcord.SelectOption(label="Faculty of Creative Multimedia",value="gif9",description="")  
      dropdown=nextcord.ui.Select(placeholder="Can remove if u get wrong",options=[ts3,ts4,ts7,ts8,ts9,ts10],max_values=1)
      dropdown.callback=callback1
      value1=nextcord.ui.View()
      value1.add_item(dropdown)
      await ctx.send("Remove role",view=value1)
def setup(bot):
    bot.add_cog(role(bot))