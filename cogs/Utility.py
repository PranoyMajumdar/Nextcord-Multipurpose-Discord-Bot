import nextcord
from nextcord import Embed, Interaction, slash_command, Member, SlashOption, ChannelType
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

    @slash_command(name='create-embed', description='Create embed.', guild_ids=[882441738713718815])
    async def embed_create(self, 
    ctx:Interaction,
    channel: nextcord.abc.GuildChannel = nextcord.SlashOption(channel_types=[ChannelType.text],name='channel', description='Please select a channel', required=False),
    author: str = nextcord.SlashOption(name='embed-author', description='Entre the author msg', required=False),
    author_icon: nextcord.Attachment = nextcord.SlashOption(name='embed-author-icon', description='Please select a image file', required=False),
    title: str = nextcord.SlashOption(name='embed-title', description='Entre title msg.', required=False),
    description: str = nextcord.SlashOption(name='embed-description', description='Entre description msg.', required=False),
    footer: str = nextcord.SlashOption(name='embed-footer', description='Entre footer msg.', required=False),
    footer_icon: nextcord.Attachment = nextcord.SlashOption(name='embed-footer-icon', description='Please select a image file for footer icon', required=False),
    image: nextcord.Attachment = nextcord.SlashOption(name='embed-image', description='Please select a image file for embed image', required=False),
    thumbnail: nextcord.Attachment = nextcord.SlashOption(name='embed-thumbnail', description='Please select a image file for embed thumbnail', required=False),
    colour: str = nextcord.SlashOption(name='embed-colour', description='Please provide a hex code', required=False)
    ):
        embed = nextcord.Embed()
        if not channel:
            channel = ctx.channel
            
        if author is not None and author_icon is not None:
            embed.set_author(name=author, icon_url=author_icon)
        elif author is not None and author_icon is None:
            embed.set_author(name=author)
        elif author is None and author_icon is not None:
            pass
        if title:
            embed.title=title
        if description:
            embed.description=description
        if footer_icon is not None and footer_icon is not None:
            embed.set_footer(text=footer, icon_url=footer_icon)
        elif footer is not None and footer_icon is None:
            embed.set_footer(text=footer)
        elif footer is None and footer_icon is not None:
            pass
        if image:
            embed.set_image(url=image)
        if thumbnail:
            embed.set_thumbnail(url=thumbnail)
        if colour:
            embed.colour=int("0x" + colour, 16)
        if not author and not title and not description and not footer and not image and not thumbnail and not colour:
            await ctx.response.send_message("Please write any of these values", ephemeral=True)
        else:
            await channel.send(embed=embed)
            await ctx.response.send_message(f"Embed sent to {channel}")
        
        
    

def setup(client):
    client.add_cog(Utility(client))