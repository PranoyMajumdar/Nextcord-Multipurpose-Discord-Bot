import nextcord
from nextcord import Embed, Interaction, slash_command
from nextcord.ext import commands

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client


    @slash_command(name='ping', description='See bot ping!', guild_ids=[882441738713718815])
    async def ping(
        self,
        ctx:Interaction
    ):
        await ctx.response.send_message(f"Pong {round(self.client.latency * 1000)} !")


def setup(client):
    client.add_cog(Utility(client))