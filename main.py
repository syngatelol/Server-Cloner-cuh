import discord
from colorama import Fore, init, Style
from utilities import Clone
import os

def print_add(message):
    print(f'{Fore.GREEN}[+]{Style.RESET_ALL} {message}')

def print_delete(message):
    print(f'{Fore.RED}[-]{Style.RESET_ALL} {message}')

def print_warning(message):
    print(f'{Fore.RED}[WARNING]{Style.RESET_ALL} {message}')

def print_error(message):
    print(f'{Fore.RED}[ERROR]{Style.RESET_ALL} {message}')

client = discord.Client()

@client.event
async def on_ready():
    os.system("cls & title [Server Cloner] - Created By .gg/eviction")
    print(f"""
    
░░░░██████╗░░██████╗░░░░░██╗███████╗██╗░░░██╗██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
░░░██╔════╝░██╔════╝░░░░██╔╝██╔════╝██║░░░██║██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
░░░██║░░██╗░██║░░██╗░░░██╔╝░█████╗░░╚██╗░██╔╝██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║
░░░██║░░╚██╗██║░░╚██╗░██╔╝░░██╔══╝░░░╚████╔╝░██║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║
██╗╚██████╔╝╚██████╔╝██╔╝░░░███████╗░░╚██╔╝░░██║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
╚═╝░╚═════╝░░╚═════╝░╚═╝░░░░╚══════╝░░░╚═╝░░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝
    Created By .gg/eviction | discord.gg/eviction
    """)

    guild_s = input('[+] Input Guild ID To Copy: ')
    guild = input('[+] Input Guild ID To Paste: ')
    token = input(f'[+] Input Token: ')

    corpse1 = guild_s 
    corpse2 = guild  
    token = token 

    guild_from = client.get_guild(int(corpse1))
    guild_to = client.get_guild(int(corpse2))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)

    await client.close()
    await client.logout()

client.run("token" ,bot=False)
