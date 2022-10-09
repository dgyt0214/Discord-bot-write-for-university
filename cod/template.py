from core.classes import Cog_Extension
import nextcord
import json
from nextcord.ext import commands
class template (Cog_Extension):
  pass


def setup(bot):
    bot.add_cog(template(bot))