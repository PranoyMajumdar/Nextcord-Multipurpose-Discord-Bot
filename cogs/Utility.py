import nextcord
from nextcord import Embed, Interaction, slash_command, Member, SlashOption
from nextcord.ext import commands

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.colour = 0x4555ff


    @slash_command(name='ping', description='See bot ping!', guild_ids=[882441738713718815])
    async def ping(
        self,
        ctx:Interaction
    ):
        await ctx.response.send_message(f"Pong {round(self.client.latency * 1000)} !")



    @slash_command(name='server-info', description='Server information!', guild_ids=[882441738713718815])
    async def server_info(self, ctx: Interaction):
        role_count = len(ctx.guild.roles)
        list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
        embed = Embed(colour=self.colour)
        embed.set_author(name=ctx.guild)
        embed.add_field(name='Owned by', value=ctx.guild.owner)
        embed.add_field(name='Owner id', value=ctx.guild.owner_id)
        embed.add_field(name='Verification Level', value=ctx.guild.verification_level)
        embed.add_field(name='Members', value=ctx.guild.member_count)
        embed.add_field(name='Bots', value=list_of_bots)
        embed.add_field(name='Top role', value=ctx.guild.roles[-2])
        embed.add_field(name='Guild created', value=ctx.guild.created_at)
        await ctx.response.send_message(embed=embed)


    @slash_command(name='user-info', description='See information of the mentioned user', guild_ids=[882441738713718815])
    async def user_info(self, ctx:Interaction, member: nextcord.Member = nextcord.SlashOption(name='member', description='Mention a user', required=False)):
        if not member:
            member = ctx.user
        
        date_format = "%a, %d %b %Y %i:%M %p"
        embed = Embed(colour=self.colour)
        embed.add_field(name='Name', value=member.name)
        embed.add_field(name='ID', value=member.id)
        embed.add_field(name='User joined at', value=member.joined_at.strftime(date_format))
        embed.add_field(name='Account age', value=member.created_at)
        await ctx.response.send_message(embed=embed)
    

def setup(client):
    client.add_cog(Utility(client))