import discord, sys, asyncio, aiohttp
from discord.ext import commands 
from discord.ext.commands import command
from config.ayarlar import *
from log.logger import Logger
sys.path.append('../')

class Image(commands.Cog, name="resim"):
    def __init__(self, bot):
        self.bot = bot
        self.api = "https://nekobot.xyz/api/"
        self.aiosession = aiohttp.ClientSession()

    @staticmethod
    async def saniyeConverter(saniye):
        dakika = saniye / 60
        saniye = saniye % 60
        saat = dakika / 60
        dakika = dakika % 60
        gun = saat / 24
        saat = saat % 24
        ay = gun / 30
        gun = gun % 30
        yil = ay / 12
        ay = ay % 12
        result = {'yıl': int(yil), 'ay': int(ay), 'gün': int(gun), 'saat': int(saat), 'dakika': int(dakika), 'saniye': saniye}
        return result

    @command(aliases=['gmagik'])
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def magik(self, msg, args=None):
        await Logger.guildLogger(self, msg)
        async with msg.channel.typing():
            if args is None:
                args = msg.author.avatar_url_as(static_format="png", size=1024)
            
            async with self.aiosession.get("https://nekobot.xyz/api/imagegen?type=magik&image=%s" % args) as r:
                if r.status != 200:
                    emb = discord.Embed(color=Kırmızı, description="**Magik** komutu başarısız oldu")
                    return await msg.send(embed=emb, delete_after=25)
                res = await r.json()
                emb = discord.Embed(color=msg.guild.me.color, description=f"Komutu Kullanan: `{msg.author}`\nAPI: [API](https://nekobot.xyz/api/)")
                emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                emb.set_footer(text=Footer)
                emb.set_image(url=res['message'])
                emb.timestamp = msg.message.created_at
                await msg.send(embed=emb)

    @magik.error
    async def magik_error(self, msg, err):
        if isinstance(err, commands.CommandOnCooldown):
            saniye = int(err.retry_after)
            result = await self.saniyeConverter(saniye)
            emb = discord.Embed(color=Kırmızı, description=f"**`{result['saniye']}`saniye sonra tekrar deneyiniz.**")
            emb.set_footer(text=Footer)
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            return await msg.send(embed=emb, delete_after=25)

    @command()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def deepfry(self, msg, *, args=None):
        await Logger.guildLogger(self, msg)
        async with msg.channel.typing():
            if args is None:
                args = msg.author.avatar_url_as(static_format="png", size=1024)

            async with self.aiosession.get("https://nekobot.xyz/api/imagegen?type=deepfry&image=%s" % args) as r:
                if r.status != 200:
                    emb = discord.Embed(color=Kırmızı, description="**Deepfry** komutu başarısız oldu")
                    return await msg.send(embed=emb, delete_after=25)
                res = await r.json()
                emb = discord.Embed(color=msg.guild.me.color, description=f"Komutu Kullanan: `{msg.author}`\nAPI: [API](https://nekobot.xyz/api/)")
                emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                emb.set_footer(text=Footer)
                emb.set_image(url=res['message'])
                emb.timestamp = msg.message.created_at
                await msg.send(embed=emb)

    @deepfry.error
    async def deepfry_error(self, msg, err):
        if isinstance(err, commands.CommandOnCooldown):
            saniye = int(err.retry_after)
            result = await self.saniyeConverter(saniye)
            emb = discord.Embed(color=Kırmızı, description=f"**`{result['saniye']}`saniye sonra tekrar deneyiniz.**")
            emb.set_footer(text=Footer)
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            return await msg.send(embed=emb, delete_after=25)

    @command(aliases=['trumptweet'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def trump(self, msg, *, args=None):
        await Logger.guildLogger(self, msg)
        if args is None:
            args = "komuttan sonra yazı yaz knk"

        async with self.aiosession.get("https://nekobot.xyz/api/imagegen?type=trumptweet&text=%s" % args) as r:
            if r.status != 200:
                emb = discord.Embed(color=Kırmızı, description="**Trump** komutu başarısız oldu")
                return await msg.send(embed=emb, delete_after=25)
            res = await r.json()
            emb = discord.Embed(color=msg.guild.me.color, description=f"Komutu Kullanan: `{msg.author}`\nAPI: [API](https://nekobot.xyz/api/)")
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            emb.set_footer(text=Footer)
            emb.set_image(url=res['message'])
            emb.timestamp = msg.message.created_at
            await msg.send(embed=emb)

    @trump.error
    async def trump_error(self, msg, err):
        if isinstance(err, commands.CommandOnCooldown):
            saniye = int(err.retry_after)
            result = await self.saniyeConverter(saniye)
            emb = discord.Embed(color=Kırmızı, description=f"**`{result['saniye']}`saniye sonra tekrar deneyiniz.**")
            emb.set_footer(text=Footer)
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            return await msg.send(embed=emb, delete_after=25)

    @command(aliases=['iphone'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def iphonex(self, msg, *, args=None):
        await Logger.guildLogger(self, msg)
        async with msg.channel.typing():
            if args is None:
                args = msg.author.avatar_url_as(static_format="png", size=1024)

            async with self.aiosession.get("https://nekobot.xyz/api/imagegen?type=iphonex&url=%s" % args) as r:
                if r.status != 200:
                    emb = discord.Embed(color=Kırmızı, description="**Iphonex** komutu başarısız oldu")
                    return await msg.send(embed=emb, delete_after=25)
                res = await r.json()
                emb = discord.Embed(color=msg.guild.me.color, description=f"Komutu Kullanan: `{msg.author}`\nAPI: [API](https://nekobot.xyz/api/)")
                emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                emb.set_footer(text=Footer)
                emb.set_image(url=res['message'])
                emb.timestamp = msg.message.created_at
                await msg.send(embed=emb)

    @iphonex.error
    async def iphonex_error(self, msg, err):
        if isinstance(err, commands.CommandOnCooldown):
            saniye = int(err.retry_after)
            result = await self.saniyeConverter(saniye)
            emb = discord.Embed(color=Kırmızı, description=f"**`{result['saniye']}`saniye sonra tekrar deneyiniz.**")
            emb.set_footer(text=Footer)
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            return await msg.send(embed=emb, delete_after=25)

    
        if isinstance(err, commands.CommandOnCooldown):
            saniye = int(err.retry_after)
            result = await self.saniyeConverter(saniye)
            emb = discord.Embed(color=Kırmızı, description=f"**`{result['saniye']}`saniye sonra tekrar deneyiniz.**")
            emb.set_footer(text=Footer)
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            return await msg.send(embed=emb, delete_after=25)

    @command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def clyde(self, msg, *, args=None):
        await Logger.guildLogger(self, msg)
        if args is None:
            args = "komuttan sonra yazı yaz knk"

        async with self.aiosession.get("https://nekobot.xyz/api/imagegen?type=clyde&text=%s" % args) as r:
            if r.status != 200:
                emb = discord.Embed(color=Kırmızı, description="**Clyde** komutu başarısız oldu")
                return await msg.send(embed=emb, delete_after=25)
            res = await r.json()
            emb = discord.Embed(color=msg.guild.me.color, description=f"Komutu Kullanan: `{msg.author}`\nAPI: [API](https://nekobot.xyz/api/)")
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            emb.set_footer(text=Footer)
            emb.set_image(url=res['message'])
            emb.timestamp = msg.message.created_at
            await msg.send(embed=emb)

    @clyde.error
    async def clyde_error(self, msg, err):
        if isinstance(err, commands.CommandOnCooldown):
            saniye = int(err.retry_after)
            result = await self.saniyeConverter(saniye)
            emb = discord.Embed(color=Kırmızı, description=f"**`{result['saniye']}`saniye sonra tekrar deneyiniz.**")
            emb.set_footer(text=Footer)
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            return await msg.send(embed=emb, delete_after=25)

    @command(aliases=['cmm'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def changemymind(self, msg, *, args=None):
        await Logger.guildLogger(self, msg)
        if args is None:
            args = "komuttan sonra yazı yaz knk"

        async with self.aiosession.get("https://nekobot.xyz/api/imagegen?type=changemymind&text=%s" % args) as r:
            if r.status != 200:
                emb = discord.Embed(color=Kırmızı, description="**ChangeMyMind** komutu başarısız oldu")
                return await msg.send(embed=emb, delete_after=25)
            res = await r.json()
            emb = discord.Embed(color=msg.guild.me.color, description=f"Komutu Kullanan: `{msg.author}`\nAPI: [API](https://nekobot.xyz/api/)")
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            emb.set_footer(text=Footer)
            emb.set_image(url=res['message'])
            emb.timestamp = msg.message.created_at
            await msg.send(embed=emb)

    @changemymind.error
    async def changemymind_error(self, msg, err):
        if isinstance(err, commands.CommandOnCooldown):
            saniye = int(err.retry_after)
            result = await self.saniyeConverter(saniye)
            emb = discord.Embed(color=Kırmızı, description=f"**`{result['saniye']}`saniye sonra tekrar deneyiniz.**")
            emb.set_footer(text=Footer)
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            return await msg.send(embed=emb, delete_after=25)

    @command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def jpeg(self, msg, *, args=None):
        await Logger.guildLogger(self, msg)
        async with msg.channel.typing():
            if args is None:
                args = msg.author.avatar_url_as(static_format="png", size=1024)
            async with self.aiosession.get("https://nekobot.xyz/api/imagegen?type=jpeg&url=%s" % args) as r:
                if r.status != 200:
                    emb = discord.Embed(color=Kırmızı, description="**Jpeg** komutu başarısız oldu")
                    return await msg.send(embed=emb, delete_after=25)
                res = await r.json()
                emb = discord.Embed(color=msg.guild.me.color, description=f"Komutu Kullanan: `{msg.author}`\nAPI: [API](https://nekobot.xyz/api/)")
                emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                emb.set_footer(text=Footer)
                emb.set_image(url=res['message'])
                emb.timestamp = msg.message.created_at
                await msg.send(embed=emb)

    @jpeg.error
    async def jpeg_error(self, msg, err):
        if isinstance(err, commands.CommandOnCooldown):
            saniye = int(err.retry_after)
            result = await self.saniyeConverter(saniye)
            emb = discord.Embed(color=Kırmızı, description=f"**`{result['saniye']}`saniye sonra tekrar deneyiniz.**")
            emb.set_footer(text=Footer)
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            return await msg.send(embed=emb, delete_after=25)

    @command(aliases=['phcomment'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def phyorum(self, msg, *, args=None):
        await Logger.guildLogger(self, msg)
        if args is None:
            args = "komuttan sonra yazı yaz knk"
        avatar = msg.author.avatar_url_as(static_format="png", size=1024)
        async with self.aiosession.get(f"https://nekobot.xyz/api/imagegen?type=phcomment&image={avatar}&text={args}&username={msg.author.name}") as r:
            if r.status != 200:
                emb = discord.Embed(color=Kırmızı, description="**Phyorum** komutu başarısız oldu")
                return await msg.send(embed=emb, delete_after=25)
            res = await r.json()
            emb = discord.Embed(color=msg.guild.me.color, description=f"Komutu Kullanan: `{msg.author}`\nAPI: [API](https://nekobot.xyz/api/)")
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            emb.set_footer(text=Footer)
            emb.set_image(url=res['message'])
            emb.timestamp = msg.message.created_at
            await msg.send(embed=emb)

    @phyorum.error
    async def phyorum_error(self, msg, err):
        if isinstance(err, commands.CommandOnCooldown):
            saniye = int(err.retry_after)
            result = await self.saniyeConverter(saniye)
            emb = discord.Embed(color=Kırmızı, description=f"**`{result['saniye']}`saniye sonra tekrar deneyiniz.**")
            emb.set_footer(text=Footer)
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            return await msg.send(embed=emb, delete_after=25)

def setup(bot):
    bot.add_cog(Image(bot))