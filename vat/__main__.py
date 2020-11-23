import discord
import logging
from vat.client import VatClient
import vat.config as config

def main():
    # Setup Intents to only listen to voice events
    intents = discord.Intents.none()
    intents.guilds = True
    intents.voice_states = True

    # Run the client
    client = VatClient(intents=intents)
    client.run(config.DISCORD_ACCESS_TOKEN)

if __name__ == '__main__':
    main()