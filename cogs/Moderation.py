import nextcord
from nextcord import slash_command, Interaction
from nextcord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


    @slash_command(name='kick', description='Kick a member', guild_ids=[882441738713718815])
    async def kick(
        self,
        ctx:Interaction,
        member: nextcord.Member = nextcord.SlashOption(
            name='member',
            description='Please select a member'
        ),
        reason: str = nextcord.SlashOption(
            name='reason',
            description='Please provide a reason',
            required=False #This will make this option as a Optional.
        )
    ):
        if not reason: reason="No reason"
        await member.kick(reason=reason)
        await ctx.response.send_message(f"{member} has been kicked by {ctx.user.mention} for {reason}")

    @slash_command(name='ban', description='Ban a member', guild_ids=[882441738713718815])
    async def ban(
        self,
        ctx:Interaction,
        member: nextcord.Member = nextcord.SlashOption(name='member', description='Please select a member'),
        reason: str = nextcord.SlashOption(name='reason', description='Please provide a reason', required=False)
    ):
        if not reason: reason = "No reason"
        await member.ban(reason=reason)
        await ctx.response.send_message(f"{member} has been banned by {ctx.user.mention} for {reason}")

    @slash_command(name='unban', description='Unban a member', guild_ids=[882441738713718815])
    async def unban(
        self,
        ctx:Interaction,
        member: nextcord.User = nextcord.SlashOption(name='member', description='Please provid a user id')
    ): 
        await ctx.guild.unban(user=member)
        await ctx.response.send_message(f"{member} has been unban by {ctx.user.mention}.")



def setup(client):
    client.add_cog(Moderation(client))