import discord, sys, asyncio, aiohttp
from discord.ext import commands 
from discord.ext.commands import command
from config.ayarlar import *
from log.logger import Logger
sys.path.append('../')

class Nsfw(commands.Cog, name="Nsfw"):
    def __init__(self, bot):
        self.bot = bot
        self.api = "https://nekobot.xyz/api/"
        self.aiosession = aiohttp.ClientSession()

    @command(aliases=['porno', 'pgif'])
    async def porn(self, msg):
        await Logger.guildLogger(self, msg)
        if msg.channel.nsfw is False:
            return await msg.send(":underage: **NSFW kanalı olmadığı için atamıyorum.**")
        async with self.aiosession.get(f"{self.api}image?type=pgif") as r:
            if r.status != 200:
                emb = discord.Embed(color=Kırmızı, description="İçerik getirilemedi")
                return await msg.send(embed=emb, delete_after=25)
            res = await r.json()
            emb = discord.Embed(color=msg.guild.me.color, description=f"Komutu Kullanan: `{msg.author}`\nAPI: [API](https://nekobot.xyz/api/)")
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            emb.set_footer(text=Footer)
            emb.set_image(url=res['message'])
            emb.timestamp = msg.message.created_at
            return await msg.send(embed=emb)

    @command(aliases=['göğüsler', 'tits'])
    async def boobs(self, msg):
        await Logger.guildLogger(self, msg)
        if msg.channel.nsfw is False:
            return await msg.send(":underage: **NSFW kanalı olmadığı için atamıyorum.**")
        async with self.aiosession.get(f"{self.api}image?type=boobs") as r:
            if r.status != 200:
                emb = discord.Embed(color=Kırmızı, description="İçerik getirilemedi")
                return await msg.send(embed=emb, delete_after=25)
            res = await r.json()
            emb = discord.Embed(color=msg.guild.me.color, description=f"Komutu Kullanan: `{msg.author}`\nAPI: [API](https://nekobot.xyz/api/)")
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            emb.set_footer(text=Footer)
            emb.set_image(url=res['message'])
            emb.timestamp = msg.message.created_at
            return await msg.send(embed=emb)

    @command(aliases=['kalça'])
    async def ass(self, msg):
        await Logger.guildLogger(self, msg)
        if msg.channel.nsfw is False:
            return await msg.send(":underage: **NSFW kanalı olmadığı için atamıyorum.**")
        async with self.aiosession.get(f"{self.api}image?type=ass") as r:
            if r.status != 200:
                emb = discord.Embed(color=Kırmızı, description="İçerik getirilemedi")
                return await msg.send(embed=emb, delete_after=25)
            res = await r.json()
            emb = discord.Embed(color=msg.guild.me.color, description=f"Komutu Kullanan: `{msg.author}`\nAPI: [API](https://nekobot.xyz/api/)")
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            emb.set_footer(text=Footer)
            emb.set_image(url=res['message'])
            emb.timestamp = msg.message.created_at
            return await msg.send(embed=emb)

    @command(aliases=['amcık', '250gr'])
    async def pussy(self, msg):
        await Logger.guildLogger(self, msg)
        if msg.channel.nsfw is False:
            return await msg.send(":underage: **NSFW kanalı olmadığı için atamıyorum.**")
        async with self.aiosession.get(f"{self.api}image?type=pussy") as r:
            if r.status != 200:
                emb = discord.Embed(color=Kırmızı, description="İçerik getirilemedi")
                return await msg.send(embed=emb, delete_after=25)
            res = await r.json()
            emb = discord.Embed(color=msg.guild.me.color, description=f"Komutu Kullanan: `{msg.author}`\nAPI: [API](https://nekobot.xyz/api/)")
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            emb.set_footer(text=Footer)
            emb.set_image(url=res['message'])
            emb.timestamp = msg.message.created_at
            return await msg.send(embed=emb)
    
    @command()
    async def anal(self, msg):
        await Logger.guildLogger(self, msg)
        if msg.channel.nsfw is False:
            return await msg.send(":underage: **NSFW kanalı olmadığı için atamıyorum.**")
        async with self.aiosession.get(f"{self.api}image?type=anal") as r:
            if r.status != 200:
                emb = discord.Embed(color=Kırmızı, description="İçerik getirilemedi")
                return await msg.send(embed=emb, delete_after=25)
            res = await r.json()
            emb = discord.Embed(color=msg.guild.me.color, description=f"Komutu Kullanan: `{msg.author}`\nAPI: [API](https://nekobot.xyz/api/)")
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            emb.set_footer(text=Footer)
            emb.set_image(url=res['message'])
            emb.timestamp = msg.message.created_at
            return await msg.send(embed=emb)

    @command()
    async def sizdengelenler(self, msg):
        await Logger.guildLogger(self, msg)
        if msg.channel.nsfw is False:
            return await msg.send(":underage: **NSFW kanalı olmadığı için atamıyorum.**")
        async with self.aiosession.get(f"{self.api}image?type=gonewild") as r:
            if r.status != 200:
                emb = discord.Embed(color=Kırmızı, description="İçerik getirilemedi")
                return await msg.send(embed=emb, delete_after=25)
            res = await r.json()
            emb = discord.Embed(color=msg.guild.me.color, description=f"Komutu Kullanan: `{msg.author}`\nAPI: [API](https://nekobot.xyz/api/)")
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            emb.set_footer(text=Footer)
            emb.set_image(url=res['message'])
            emb.timestamp = msg.message.created_at
            return await msg.send(embed=emb)

    @command(aliases=['paizure'])
    async def hentai(self, msg):
        await Logger.guildLogger(self, msg)
        if msg.channel.nsfw is False:
            return await msg.send(":underage: **NSFW kanalı olmadığı için atamıyorum.**")
        async with self.aiosession.get(f"{self.api}image?type=paizuri") as r:
            if r.status != 200:
                emb = discord.Embed(color=Kırmızı, description="İçerik getirilemedi")
                return await msg.send(embed=emb, delete_after=25)
            res = await r.json()
            emb = discord.Embed(color=msg.guild.me.color, description=f"Komutu Kullanan: `{msg.author}`\nAPI: [API](https://nekobot.xyz/api/)")
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            emb.set_footer(text=Footer)
            emb.set_image(url=res['message'])
            emb.timestamp = msg.message.created_at
            return await msg.send(embed=emb)

def setup(bot):
    bot.add_cog(Nsfw(bot))