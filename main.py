import discord
import pytz
from discord.ext import commands
import datetime 

TOKEN="MTA3OTgwNDI2NDI4MjYwMzU1Mg.G7GgeN.CwrcsLbAOu6acjHeGNFSoteel7L5Ey2qS3kF9Y"
CHANNEL_ID = 1079809656286887936

# Set the time zone for Abuja, Nigeria
tz = pytz.timezone('Africa/Lagos')
# Define a function to get the current time in Abuja
current_time = datetime.datetime.now(tz).time()

# Set the prayer times in 24-hour format
Fajr = "5:30"
Dhuhr= "12:50"
Asr= "15:42"
Maghrib= "18:0"
Isha= "20:0"


# Create a new Discord client
athan_bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


# Define a function to send the prayer reminder message
async def send_prayer_reminder():
  channel = athan_bot.get_channel(CHANNEL_ID)
  while True:
    if current_time == Fajr:
      await channel.send("@everyone It's time for Fajr prayer!")
    elif current_time == Dhuhr:
      await channel.send("@everyone It's time for Dhuhr prayer!")
     
    elif current_time == Asr:
      await channel.send("@everyone It's time for Asr prayer!")
      
    elif current_time == Maghrib:
      await channel.send("@everyone It's time for Maghrib prayer!")
      
    elif current_time == Isha:
      await channel.send("@everyone It's time for Isha prayer!")
      
    else:
      await athan_bot.sleep(60)  # Check again in 1 minute
  # Start the prayer reminder loop
  athan_bot.loop.create_task(send_prayer_reminder())
  await task
  ex = task.exception()

# Define an event listener for when the bot is ready
@athan_bot.event
async def on_ready():
  print("Hello! Your friendly neighbourhood athan bot here to help ^_^ ")
  channel = athan_bot.get_channel(CHANNEL_ID)
  await channel.send(
    "Hello! I am Hakeem, your friendly neighbourhood athan bot ^_^ ")
  
  
# Start the bot
athan_bot.run(TOKEN)