import discord

__TOKEN__ = 'token'

client = discord.Client()

@client.event
async def on_ready():
    print(client.user)

@client.event
async def on_message(message):
    if message.content == '!unban':
        if not message.author.guild_permissions.administrator:
            return
        bans = await message.guild.bans()
        lists = ["{0.id}".format(entry.user) for entry in bans]

        for i in lists:
            a = await client.fetch_user(i)
            await message.guild.unban(a)
            print(f'{a} was unbanned')
            await message.channel.send(f'{a} was unbanned')
            
		
client.run(__TOKEN__)
