"""    
    Copyright (C) 2022 ViridianTelamon (Viridian)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import discord
import os
import random
import time

#Botto Oi Discord Bot.
#By:  ViridianTelamon.

client = discord.Client()

token = "Put Discord Bot Token Here."

get_dog = ["doggy.jpg","dog.jpg","adog.jpg","bdog.jpg","doge.jpg","cdog.jpg","d_dog.jpg","edog.jpg","f_dog.jpg","gdog.jpg","hdog.jpg","cat.jpg","coolcat.jpg","idog.jpg","jdog.jpg","kdog.jpg","ldog.jpg","mdog.jpg","ndog.jpg","odog.jpg","snoppdog.jpg","pdog.jpg","qdog.jpg","rdog.jpg","sdog.jpg","cooldog.jpg","tdog.jpg","interestingdog.jpg","udog.jpg","vdog.jpg","wdog.jpg","xdog.jpg","ydog.png","zdog.jpg"]

#On Ready Event.
@client.event
async def on_ready():
  print("Bot Ready.")
  time.sleep(1)
  print("Logged In As:  {0.user}".format(client))

#If The Bot Recieves A Message Event.
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("!dog"):
    dog_image = random.choice(get_dog)
    await message.channel.send(file=discord.File(dog_image))

client.run(token)
