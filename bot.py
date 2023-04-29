#u have to change api keys

import subprocess
import discord
import re
import time
import sys
import os
from discord.ext import commands
import random
import requests
import asyncio

def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def giantcock():
   if sys.platform == "linux":
    os.system("clear")
   elif sys.platform == "win32":
    os.system("cls")

token = 'token here'
intents = discord.Intents.all()
cum = commands.Bot(command_prefix='.', intents=intents)
cum.remove_command('help')

@cum.event
async def on_ready():
    await cum.change_presence(activity=discord.Game(name=".help"))
    giantcock()
    print(f'Logged in as {cum.user} (ID: {cum.user.id})\nMade By: Lotus\n')

@cum.command()
async def help(ctx):
    prefix = cum.command_prefix
    em = discord.Embed(title="Help", color=RandomColor())
    em.add_field(name=f"{prefix}geoip [ip address]", value="Get information about an IP address.", inline=False)
    em.add_field(name=f"{prefix}holehe [email address]", value="Checks if an email is attached to an account on sites like twitter, instagram, imgur and more than 120 others.", inline=False)
    em.add_field(name=f"{prefix}mac [MAC address]", value="Get information about a MAC address.", inline=False)
    em.add_field(name=f"{prefix}numscan [phone number]", value="Get information about a phone number.", inline=False)
    em.add_field(name=f"{prefix}ping", value="Check the bot's latency.", inline=False)
    em.set_footer(text=f"Requested by {ctx.author.display_name}")
    await ctx.send(embed=em)


@cum.command()
async def holehe(ctx, email: str):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        await ctx.send("**Please provide a valid email address.**")
        return

    owo = await ctx.send("**Please Wait...**")
    try:
        output = subprocess.check_output(['holehe', '--only-used', email]).decode()
        uwu = "\n".join(line for line in output.split("\n") if "[+]" in line or "[-]" in line or "[x]" in line)
        if uwu:
            await owo.edit(content=f"```{email}\n" + uwu + "```")
        else:
            await owo.edit(content="```Error.```")
    except subprocess.CalledProcessError as e:
        await owo.edit(content="```Error.```")

@cum.command()
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.send("Pinging! Please Wait!")
    ping = (time.monotonic() - before) * 1000
    await asyncio.sleep(0.1)
    await message.edit(content=f"⏳ Bot Ping: {int(ping)}ms ⌛")
    await asyncio.sleep(2.5)
    await message.edit(content=f"⌛ Bot Ping: {int(ping)}ms ⏳")
    await asyncio.sleep(2.5)
    await message.edit(content=f"⏳ Bot Ping: {int(ping)}ms ⌛")

@cum.command(aliases=['phonescan', 'numscan', 'phonelookup'])
async def numverify(ctx, *, number: str = '14158586273'):
    r = requests.get(f'http://apilayer.net/api/validate?access_key=&number={number}')
    verify = r.json()
    em = discord.Embed(color=RandomColor())
    em.set_author(name="Numverify")
    fields = [
        {'name': '**Number:**', 'value': verify['number']},
        {'name': '**Valid:**', 'value': verify['valid']},
        {'name': '**Local Format:**', 'value': verify['local_format']},
        {'name': '**International Format:**', 'value': verify['international_format']},
        {'name': '**Country:**', 'value': verify['country_name']},
        {'name': '**Country Code:**', 'value': verify['country_code']},
        {'name': '**Country Prefix:**', 'value': verify['country_prefix']},
        {'name': '**Location:**', 'value': verify['location']},
        {'name': '**Carrier:**', 'value': verify['carrier']},
        {'name': '**Line Type:**', 'value': verify['line_type']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
    try:
       return await ctx.send(embed=em)
    except:
       return await ctx.send(f"Numverify:\nNumber: `{verify['number']}`\nValid: `{verify['valid']}`\nLocal Format: `{verify['local_format']}`\nInternational Format: `{verify['international_format']}`\nCountry: `{verify['country_name']}`\nCountry Code: `{verify['country_code']}`\nCountry Prefix: `{verify['country_prefix']}`\nLocation: `{verify['location']}`\nLine Type: `{verify['line_type']}`")

@cum.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.1.1.1'): 
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}?key=')
    geo = r.json()
    em = discord.Embed(color=RandomColor())
    em.set_author(name="GeoIP")
    fields = [
        {'name': '**IP:**', 'value': geo['query']},
        {'name': '**Status:**', 'value': geo['status']},
        {'name': '**ipType:**', 'value': geo['ipType']},
        {'name': '**Country:**', 'value': geo['country']},
        {'name': '**City:**', 'value': geo['city']},
        {'name': '**Continent:**', 'value': geo['continent']},
        {'name': '**IPName**', 'value': geo['ipName']},
        {'name': '**ISP:**', 'value': geo['isp']},
        {'name': '**Latitude:**', 'value': geo['lat']},
        {'name': '**Longitude:**', 'value': geo['lon']},
        {'name': '**Org:**', 'value': geo['org']},
        {'name': '**Region:**', 'value': geo['region']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
    try:
       return await ctx.send(embed=em)
    except:
        return await ctx.send(f"GeoIP:\nIP: `{geo['query']}`\nStatus: `{geo['status']}`\nIP Type: `{geo['ipType']}`\nOrg: `{geo['org']}`\nISP: `{geo['isp']}`\nCountry: `{geo['country']}`\nCity: `{geo['city']}`\nContinent: `{geo['continent']}`\nRegion: `{geo['region']}`\nLatitude: `{geo['lat']}`\nLongitude: `{geo['lon']}`")

@cum.command()
async def mac(ctx, mac): 
    r = requests.get('http://api.macvendors.com/' + mac)
    em = discord.Embed(title='MAC Lookup Result', description=r.text, colour=RandomColor())
    em.set_author(name='MAC Lookup')
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(r.text)

cum.run(token)
