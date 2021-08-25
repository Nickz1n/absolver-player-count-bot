import discord
import time
import requests
from bs4 import BeautifulSoup

token = open('token.txt', 'r').readline()

client = discord.Client()

def get_players() -> str:
    try:
        html = requests.get('https://steamplayercount.com/app/473690').text
        bs = BeautifulSoup(html, 'html.parser')
        return bs.find('span', class_='big-text').text
    except:
        return "??"

@client.event
async def on_ready():
    print("bot online!!")
    next_check_ms = int(time.time() * 1000)
    count = 0
    while True:
        current_ms = int(time.time() * 1000)
        if next_check_ms <= current_ms:
            next_check_ms = next_check_ms + (30 * 60 * 1000)
            players = get_players()
            act = discord.Game(name=f"Absolver with {players} players")
            await client.change_presence(activity=act)
            count +=1
            print(f"#{count} player count updated: {players} players")

client.run(token)