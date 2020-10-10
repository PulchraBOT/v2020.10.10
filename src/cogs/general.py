from config.ayarlar import *
import discord
import asyncio
import aiohttp
import random
import datetime
import textblob
import sys
import time
from discord.ext import commands
from discord.ext.commands import command
from log.logger import Logger
sys.path.append('../')

class General(commands.Cog, name="Genel"):
    def __init__(self, bot):
        self.bot = bot
        self.stopwatches = {}

    @command(aliases=["pp", "a"])
    async def avatar(self, ctx, user: discord.User = None):
        await Logger.guildLogger(self, ctx)
        if user is None:
            user = ctx.message.author

        avatar = user.avatar_url_as(static_format="png", size=1024)
        e = discord.Embed(
            description=f"Avatar Sahibi: `{user}`\nAvatar Linki: [{user.name}]({avatar})", colour=ctx.guild.me.color)
        e.set_image(url=avatar)
        e.set_footer(text=Footer)
        e.set_author(name=self.bot.user.name,
                     icon_url=self.bot.user.avatar_url)
        e.timestamp = ctx.message.created_at
        await ctx.send(embed=e)

    @command()
    async def ping(self, ctx):
        await Logger.guildLogger(self, ctx)
        msg = await ctx.send("**Ping Hesaplanıyor :** `□□□□□□□□□□`")
        await asyncio.sleep(0.3)
        await msg.edit(content="**Ping Hesaplanıyor :** `■■□□□□□□□□`")
        await asyncio.sleep(0.3)
        await msg.edit(content="**Ping Hesaplanıyor :** `■■■■□□□□□□`")
        await asyncio.sleep(0.3)
        await msg.edit(content="**Ping Hesaplanıyor :** `■■■■■■□□□□`")
        await asyncio.sleep(0.3)
        await msg.edit(content="**Ping Hesaplanıyor :** `■■■■■■■■□□`")
        await asyncio.sleep(0.3)
        await msg.edit(content="**Ping Hesaplanıyor :** `■■■■■■■■■■`")
        await asyncio.sleep(0.3)
        await msg.delete()
        e = discord.Embed(colour=ctx.guild.me.color,
                          description=f"Ping Değeri: `{round(self.bot.latency * 1000)}ms`")
        e.set_author(name=self.bot.user.name,
                     icon_url=self.bot.user.avatar_url)
        e.set_footer(text=Footer)
        e.timestamp = ctx.message.created_at
        await ctx.send(embed=e)

    @command(aliases=['user', 'kbilgi'])
    async def info(self, ctx, *users: discord.Member):
        await Logger.guildLogger(self, ctx)
        try:
            if len(users) == 0:
                users = [ctx.message.author]
            guild = ctx.message.guild
            for user in users:
                msg = f":id:: `{user.id}`\n\n"
                if user.nick:
                    msg += f":name_badge: **Takma Adı**: `{user.nick}`\n\n"
                if not user.bot:
                    msg += ":robot: **Bot**: `Hayır`\n\n"
                elif user.bot:
                    msg += ":robot: **Bot**: `Evet`\n\n"
                msg += f":inbox_tray: **Sunucuya Katılma Tarihi**: \n__{user.joined_at.strftime('%d/%m/%Y %H:%M:%S')}__\n\n"
                msg += f":globe_with_meridians: **Discorda Katılma Tarihi**: \n__{user.created_at.strftime('%d/%m/%Y %H:%M:%S')}__\n\n"
                msg += f":information_source: **Durum**: `{str(user.status).upper()}`\n\n"
                if user.activity:
                    msg += f":joystick: **Oynuyor**: `{user.activity.name}`\n\n"
                if user.voice:
                    msg += f":microphone2: **Bulunduğu Ses Kanalı**: `{user.voice.channel.name}`\n\n"
                msg += ":shield: **Rolleri**:{0} - `{1}`\n\n".format(
                    len(user.roles), ", ".join([role.name for role in user.roles]))
                e = discord.Embed(title=f"👤 {user}",
                                  colour=user.color, description=msg)
                e.set_footer(text=Footer)
                e.set_thumbnail(url=user.avatar_url)
                e.timestamp = ctx.message.created_at
                await ctx.send(embed=e)
        except Exception as err:
            await ctx.send(f"Bir Hata Meydana Geldi Hata:\n```{err}```")

    @command(aliases=["guild", "server"])
    async def sunucu(self, ctx):
        await Logger.guildLogger(self, ctx)
        try:
            guild = ctx.message.guild
            msg = f":id: `{guild.id}`\n\n"
            msg += f":bust_in_silhouette: **Sahip**: {guild.owner.mention}\n\n"
            msg += f":map: **Server Konumu**: `{str(guild.region).upper()}`\n\n"
            msg += f":calendar_spiral: **Oluşturulma Tarihi**: \n__{guild.created_at.strftime('%d/%m/%Y %H:%M:%S')}__\n\n"
            msg += f":busts_in_silhouette: **Üye Sayısı**: `{guild.member_count}`\n\n"
            if guild.verification_level:
                msg += f":exclamation: **Güvenlik Seviyesi**: `{str(guild.verification_level).upper()}`\n\n"
            if guild.system_channel:
                msg += f":speech_balloon: **Sistem Kanalı**: {guild.system_channel}\n\n"
            if guild.afk_channel:
                msg += f":telephone_receiver: **Afk Kanalı**: `{guild.afk_channel}`\n\n"
                msg += f":keyboard: **Afk Düşme Zamanı**: `{str(int(int(guild.afk_timeout) / 60))}`\n\n"
            msg += f":arrow_forward: **Kanallar**: Ses:`{len(guild.voice_channels)}`|Yazı: `{len(guild.text_channels)}`|Toplam: `{int(len(guild.voice_channels)) + int(len(guild.text_channels))}`\n\n"
            msg += f":arrow_forward: **Roller**: `{len(guild.roles)}`\n\n"
            msg2 = ""
            msg2 = msg
            page = False
            if len(guild.emojis) != 0:
                emotes = ""
                for emoji in guild.emojis:
                    emotes += str(emoji)
                msg2 += f":arrow_forward: **Emojiler**: {emotes}\n\n"
                if len(msg2) <= 2048:
                    msg += f":arrow_forward: **Emojiler**: {emotes}\n\n"

                elif len(msg2) >= 2048:
                    page = True
                    page2 = f":arrow_forward: **Emojiler**: {emotes}\n\n"

            e = discord.Embed(
                title=f":desktop: {guild.name}", colour=ctx.guild.me.color, description=msg)
            e.set_footer(text=Footer)
            e.set_thumbnail(url=guild.icon_url)
            e.timestamp = ctx.message.created_at
            embed = await ctx.send(embed=e)
            if page == True:
                e2 = discord.Embed(
                    title=f":desktop: {guild.name}", color=siyah, description=page2)
                e2.set_footer(text=Footer)
                e2.timestamp = ctx.message.created_at
                await embed.add_reaction('\u25c0')  # Sol
                await embed.add_reaction('\u25b6')  # Sağ
                pages = [e, e2]  # indexler "0, 1"
                i = 0
                click = ""
                while True:
                    if click == '\u25c0':
                        if i > 0:
                            i -= 1
                            await embed.edit(embed=pages[i])
                    elif click == '\u25b6':
                        if i < 1:
                            i += 1
                            await embed.edit(embed=pages[i])

                    def check(react, user):
                        return msg.author == user

                    react, user = await self.bot.wait_for('reaction_add', timeout=30, check=check)
                    
                    click = str(react.emoji)
                    await react.remove(msg.author)

        except Exception as err:
            print(err)

    @command(aliases=['say'])
    async def yaz(self, ctx, *, msg=None):
        await Logger.guildLogger(self, ctx)
        if msg == None:
            await ctx.send(f"{ctx.author.mention} Bi Mesaj Belirt Knk Kullanım:\n```+yaz <Mesaj>```", delete_after=10)
            await asyncio.sleep(10)
            await ctx.message.delete()
            return
        else:
            await asyncio.sleep(0.1)
            await ctx.message.delete()
            await ctx.send(msg)

    @command(aliases=["beniekle", "invite", "inv"])
    async def davet(self, ctx):
        await Logger.guildLogger(self, ctx)
        url = discord.utils.oauth_url(client_id=str(
            self.bot.user.id), permissions=discord.Permissions(permissions=8))
        e = discord.Embed(color=ctx.guild.me.color,
                          description=f"Beni eklemek için [buraya]({url}) tıkla")
        e.set_author(name=self.bot.user.name,
                     icon_url=self.bot.user.avatar_url)
        e.set_footer(text=Footer)
        e.timestamp = ctx.message.created_at
        await ctx.send(embed=e)

    @command(aliases=["emojiyazı"])
    async def eyaz(self, ctx, *, text):
        await Logger.guildLogger(self, ctx)
        def converter(text):
            karakterler = {
                "a": ":regional_indicator_a:", "A": ":regional_indicator_a:",
                "b": ":regional_indicator_b:", "B": ":regional_indicator_b:",
                "c": ":regional_indicator_c:", "C": ":regional_indicator_c:",
                "d": ":regional_indicator_d:", "D": ":regional_indicator_d:",
                "e": ":regional_indicator_e:", "E": ":regional_indicator_e:",
                "q": ":regional_indicator_q:", "Q": ":regional_indicator_q:",
                "w": ":regional_indicator_w:", "W": ":regional_indicator_w:",
                "r": ":regional_indicator_r:", "R": ":regional_indicator_r:",
                "t": ":regional_indicator_t:", "T": ":regional_indicator_t:",
                "y": ":regional_indicator_y:", "Y": ":regional_indicator_y:",
                "u": ":regional_indicator_u:", "U": ":regional_indicator_u:",
                "ı": ":regional_indicator_i:", "I": ":regional_indicator_i:",
                "o": ":regional_indicator_o:", "O": ":regional_indicator_o:",
                "p": ":regional_indicator_p:", "P": ":regional_indicator_p:",
                "ğ": ":regional_indicator_g:", "Ğ": ":regional_indicator_g:",
                "ü": ":regional_indicator_u:", "Ü": ":regional_indicator_u:",
                "s": ":regional_indicator_s:", "S": ":regional_indicator_s:",
                "f": ":regional_indicator_f:", "F": ":regional_indicator_f:",
                "g": ":regional_indicator_g:", "G": ":regional_indicator_g:",
                "h": ":regional_indicator_h:", "H": ":regional_indicator_h:",
                "j": ":regional_indicator_j:", "J": ":regional_indicator_j:",
                "k": ":regional_indicator_k:", "K": ":regional_indicator_k:",
                "l": ":regional_indicator_l:", "L": ":regional_indicator_l:",
                "ş": ":regional_indicator_s:", "Ş": ":regional_indicator_s:",
                "i": ":regional_indicator_i:", "İ": ":regional_indicator_i:",
                "z": ":regional_indicator_z:", "Z": ":regional_indicator_z:",
                "x": ":regional_indicator_x:", "X": ":regional_indicator_x:",
                "v": ":regional_indicator_v:", "V": ":regional_indicator_v:",
                "n": ":regional_indicator_n:", "N": ":regional_indicator_n:",
                "m": ":regional_indicator_m:", "M": ":regional_indicator_m:",
                "ö": ":regional_indicator_o:", "Ö": ":regional_indicator_o:",
                "ç": ":regional_indicator_c:", "Ç": ":regional_indicator_c:",
                "0": ":zero:", "1": ":one:", "2": ":two:", "3": ":three:", "4": ":four:", "5": ":five:", "6": ":six:", "7": ":seven:", "8": ":eight:", "9": ":nine:",
                " ": "   "
            }
            text = list(text)
            for karakter in text:
                if karakter in karakterler:
                    text[text.index(karakter)] = karakterler[karakter]

            return "".join(text)

        mesaj = converter(text)
        await ctx.send(mesaj)
        await ctx.message.delete()
    
    @command(aliases=["tr", "translate"])
    async def çeviri(self, ctx, lang1: str = None, *, text: str = None):
        await Logger.guildLogger(self, ctx)
        if lang1 is None:
            await ctx.send(f"{ctx.author.mention} Mesaj ve çevirilecek dil belirtin! Kullanım;\n```+çeviri en nasılsın```", delete_after=15)
            return
        if text is None:
            await ctx.send(f"{ctx.author.mention} Mesaj Belirtin! Kullanım;\n```+çeviri en nasılsın```", delete_after=15)
            return
        try:
            result = textblob.TextBlob(text).translate(
                from_lang="auto", to=lang1)
        except textblob.exceptions.NotTranslated:
            await ctx.send(f"{ctx.author.mention} Çeviri Yapılamadı!", delete_after=15)
        else:
            await ctx.send(f"```{result}```")

    @command(aliases=['support'])
    async def destek(self, ctx):
        await Logger.guildLogger(self, ctx)
        return await ctx.send("https://discord.gg/C8wvJqG")

    @command(aliases=['stopwatch', 'sw', 'afk'])
    async def kronometre(self, msg):
        author = msg.author
        if not author.id in self.stopwatches:
            self.stopwatches[author.id] = int(time.perf_counter())
            emb = discord.Embed(color=msg.guild.me.color, description=f"{author.mention}, Kronometre Başladı bidaha komutu kullanana kadar zaman tutulacak.")
            await msg.send(embed=emb, delete_after=60)
        else:
            tmp = abs(self.stopwatches[author.id] - int(time.perf_counter()))
            tmp = str(datetime.timedelta(seconds=tmp))
            emb = discord.Embed(color=msg.guild.me.color, description=f"Kronometre Durduruldu! Süre: **{str(tmp)}**")
            await msg.send(embed=emb)
            self.stopwatches.pop(author.id, None)

    @command()
    async def newupdate(self, msg, channel: int=None):
        await Logger.guildLogger(self, msg)
        kanal = self.bot.get_channel(channel)
        emb = discord.Embed(color=discord.Color.from_rgb(120, 164, 250), title="v2020.10.10")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url_as(static_format="png", size=1024))
        emb.set_footer(text=Footer)
        emb.add_field(name="`Yenilikler`", value=":white_small_square: **+arama sp** komutu eklendi spotifyda arama yaparsınız ve karşınıza maximum 50 tane sonuç gelir bu sonuçları isterseniz botta açabilirsiniz\n:white_small_square: **+spbilgi** sizin veya etiketlediğiniz kişinin eğer dinliyorsa dinlediği şarkının bilgilerini verir\n:white_small_square: **+kronometre** komutu kullandığınızda sayaç başlatır komutu bidaha kullandığınızda geçen süreyi söyler.", inline=False)
        emb.add_field(name="`Düzeltmeler Ve Hata Gidermeleri`", value=":white_small_square: Spotify komutlarında artık albüm kapağındaki en baskın renk ortalamaları alınıyor ve embede koyuluyor\n:white_small_square: yardım komutunda artık tüm komutların kısatmalarıda gözüküyor\n:white_small_square: Eğer bot hakkında bir sorun yaşıyorsanız <@!{0}> benimle iletişime geçin veya [DestekSunucusuna](https://discord.gg/C8wvJqG) gelerek yardım alabilirsiniz.".format(owner), inline=False)
        emb.timestamp = msg.message.created_at
        return await kanal.send(embed=emb)
        
    @command(aliases=['botstat'])
    async def istatistikler(self, msg):
        await Logger.guildLogger(self, msg)
        ping = self.bot.latency * 1000
        emojiCount = len(self.bot.emojis)
        commandCount = len(self.bot.commands)
        guildCount = len(self.bot.guilds)
        userCount = len(self.bot.users)
        muzikCalınanSunucu = len(self.bot.voice_clients)
        KKsayısı  = await Logger.sqlLoggerGet()
        ListeningMusicCount = await Logger.sqlMusicLoggerGet()
        MusicErrorCount = await Logger.sqlMusicErrorGet()
        msj = f"**Ping:** `{ping:.2f}`\n"
        msj += f"**Sunucu Sayısı:** `{guildCount}`\n"
        msj += f"**Kullanıcı Sayısı:** `{userCount}`\n"
        msj += f"**Bu Zamana Kadar Kullanılan Komut Sayısı:** `{KKsayısı[0][1]}`\n"
        msj += f"**Bu Zamana Kadar Dinlenen Müzik Sayısı:** `{ListeningMusicCount[1]}`\n"
        msj += f"**Müzik Açarken Başarısız Olma Sayısı:** `{MusicErrorCount[1]}\n`"
        msj += f"**Emoji Sayısı:** `{emojiCount}`\n"
        msj += f"**Komut Sayısı:** `{commandCount}`\n"
        msj += f"**Müzik Çalınan Sunucu Sayısı:** `{muzikCalınanSunucu}`"
        emb = discord.Embed(color=msg.guild.me.color, title="Bot İstatistik", description=msj)
        emb.set_footer(text=Footer)
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url, url="https://pulchra.glitch.me")
        return await msg.send(embed=emb)

    @command()
    @commands.is_owner()
    async def eval(self, msg, *, code: str):
        code = code.strip("` ")
        python = "```\n{}\n```"
        result = None
        veriables = {
            'bot': self.bot,
            'msg': msg,
            'message': msg.message,
            'guild': msg.guild,
            'channel': msg.channel,
            'discord': discord,
            'author': msg.author
        }
        try:
            result = eval(code, veriables)
        except Exception as e:
            return await msg.send(python.format(type(e).__name__ + ': ' + str(e)))
        if asyncio.iscoroutine(result):
            result = await result
        await msg.send(python.format(result))

    @eval.error
    async def eval_error(self, msg, err):
        if isinstance(err, commands.NotOwner):
            emb = discord.Embed(color=Kırmızı, description="Sadece Sahibim Kullanabilir")
            await msg.send(embed=emb, delete_after=25)

def setup(bot):
    bot.add_cog(General(bot))
