from config.ayarlar import *
import discord, asyncio, random, sys, aiohttp, sqlite3, aiofiles
from discord.ext import commands
from discord.ext.commands import command
from discord import Webhook, AsyncWebhookAdapter
from log.logger import Logger
sys.path.append('../')

class Moderation(commands.Cog, name="Moderasyon"):
    def __init__(self, bot):
        self.bot = bot
        self.reactions = []
        with sqlite3.connect('users.db') as db:
            cursor = db.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS autorole(guild INT, role INT, channel INT)')
            db.commit()

    @commands.Cog.listener('on_ready')
    async def ready_ready(self):
        async with aiofiles.open("reaction_roles.txt", mode="r") as file:
            lines = await file.readlines()
            for line in lines:
                data = line.split(" ")
                self.reactions.append((int(data[0]), int(data[1]), data[2].strip("\n")))

    @command(aliases=['clear', 't'])
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def temizle(self, msg, amount: int=0, member: discord.Member=None):
        if amount == 0:
            emb = discord.Embed(color=Kırmızı, description=f"{msg.author.mention}, sileceğim mesaj sayısını belirt\n```+temizle [sayı] [isteğe bağlı=kullanıcı]```")
            return await msg.send(embed=emb, delete_after=25)

        if amount > 500:
            emb = discord.Embed(color=Kırmızı, description=f"{msg.author.mention}, `0-500` arasında mesaj silebilirim")
            return await msg.send(embed=emb, delete_after=25)
            
        await Logger.guildLogger(self, msg)
        
        if member is not None:
            def check(m):
                return m.author == member

            deleted = await msg.channel.purge(limit=amount, check=check)
            emb = discord.Embed(color=msg.guild.me.color, title="Temizle LOG", description=f"Mesaj Silme Bilgileri:\n**Silinen Mesaj Sayısı:** `{len(deleted)}`\n**Mesajları Silinen Kullanıcı:** {member.mention}\n**Komutu Kullanan Yetkili:** {msg.author.mention}")
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            emb.set_footer(text=Footer)
            return await msg.send(embed=emb)
        else:
            deleted = await msg.channel.purge(limit=amount)
            emb = discord.Embed(color=msg.guild.me.color, title="Temizle LOG", description=f"Mesaj Silme Bilgileri:\n**Silinen Mesaj Sayısı:** `{len(deleted)}`\n**Komutu Kullanan Yetkili:** {msg.author.mention}")
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            emb.set_footer(text=Footer)
            return await msg.send(embed=emb)
    
    @temizle.error
    async def temizle_error(self, msg, err):
        if isinstance(err, commands.MissingPermissions):
            emb = discord.Embed(color=Kırmızı, description=f"Bu komutu kullanabilmek için **Mesajları Yönet** yetkisine sahip olmanız gerek")
            return await msg.send(embed=emb, delete_after=25)

        if isinstance(err, commands.BotMissingPermissions):
            emb = discord.Embed(color=Kırmızı, description=f"Botta **Mesajları Yönet** yetkisi bulunmuyor")
            return await msg.send(embed=emb, delete_after=25)
        
    @command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, msg, member: discord.Member=None):
        if member is None:
            emb = discord.Embed(color=Kırmızı, description=f"{msg.author.mention}, kimi banlamak istiyorsan o kişiyi etiketle yada idsini at")
            return await msg.send(embed=emb, delete_after=25)
        
        await Logger.guildLogger(self, msg)
        
        try:
            await member.ban()
        except Exception:
            emb = discord.Embed(color=Kırmızı, description=f"{member.mention} adlı kullanıcı banlanamadı")
            return await msg.send(embed=emb, delete_after=50)
        
        emb = discord.Embed(color=msg.guild.me.color, description=f"**Yasaklanan Kullanıcı:** {member.mention}\n**Yasaklayan Yetkili:** {msg.author.mention}", title="Ban LOG")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.set_footer(text=Footer)
        return await msg.send(embed=emb)

    @ban.error
    async def ban_error(self, msg, err):
        if isinstance(err, commands.MissingPermissions):
            emb = discord.Embed(color=Kırmızı, description=f"Bu komutu kullanabilmek için **Kullanıcı Yasaklama** yetkisine sahip olmanız gerek")
            return await msg.send(embed=emb, delete_after=25)
        
        if isinstance(err, commands.BotMissingPermissions):
            emb = discord.Embed(color=Kırmızı, description=f"Botta **Kullanıcı Yasakla** yetkisi bulunmuyor")
            return await msg.send(embed=emb, delete_after=25)
  
    @command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, msg, member: discord.Member=None):
        if member is None:
            emb = discord.Embed(color=Kırmızı, description=f"{msg.author.mention}, kimi kicklemek istiyorsan o kişiyi etiketle yada idsini at")
            return await msg.send(embed=emb, delete_after=25) 
        
        await Logger.guildLogger(self, msg)

        try:
            await member.kick()
        except Exception:
            emb = discord.Embed(color=Kırmızı, description=f"{member.mention} adlı kullanıcı kicklenemedi")
            return await msg.send(embed=emb, delete_after=50)
        emb = discord.Embed(color=msg.guild.me.color, description=f"**Tekmelenen Kullanıcı:** {member.mention}\n**Tekmeleyen Yetkili:** {msg.author.mention}", title="Kick LOG")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.set_footer(text=Footer)
        return await msg.send(embed=emb)

    @kick.error
    async def kick_error(self, msg, err):
        if isinstance(err, commands.MissingPermissions):
            emb = discord.Embed(color=Kırmızı, description=f"Bu komutu kullanabilmek için **Kullanıcı Atma** yetkisine sahip olmanız gerek")
            return await msg.send(embed=emb, delete_after=25)
        
        if isinstance(err, commands.BotMissingPermissions):
            emb = discord.Embed(color=Kırmızı, description=f"Botta **Kullanıcı Atma** yetkisi bulunmuyor")
            return await msg.send(embed=emb, delete_after=25)

    @command()  # Owner Only
    async def durumdegiş(self, ctx, *, status=None):
        await Logger.guildLogger(self, ctx)
        if ctx.author.id != owner:
            return await ctx.send(":no_entry: `Sadece sahibim kullanabilir!`")
        if status is None:
            return
        activity_type = discord.ActivityType.listening
        await self.bot.change_presence(activity=discord.Activity(type=activity_type, name=status), status=discord.Status.idle)

    @command(aliases=['webh']) # Owner Only
    async def webhook(self, ctx, url=None):
        await Logger.guildLogger(self, ctx)
        if ctx.author.id != owner:
            return await ctx.send(":no_entry: `Sadece sahibim kullanabilir!`")
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(url, adapter=AsyncWebhookAdapter(session))
            emb = discord.Embed(color=discord.Color.from_rgb(30,215,96), title="Pulchra Bot", description=f"`Giriş`\nBu bot spotify apisini doğrudan kullanan `türkçe` müzik botudur artık sizlerle, botu eklemek için [Buraya](https://discord.com/oauth2/authorize?client_id=718225758790877374&scope=bot&permissions=573860928) tıklayınız.\n`Güvenlik`\nBot sunucuya eklenirken yöneticilik almaz gerekli yetkileri alır ve bu aldıgı yetkiler saldırı amaçlı kullanılamaz bu yüzden güvenlidir.\n\n**Geliştirici:** <@!{owner}>\n**Web Site:** [PulchraBOT](https://pulchra.glitch.me)\n**Geliştirici GitHub:** [Erdem](https://github.com/R3nzTheCodeGOD)\n**Botun Kodları:** [PulchraSourceCode](https://github.com/R3nzTheCodeGOD/PulchraBOT)")
            emb.set_footer(text="© 2020 Spotify AB")
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url, url="https://pulchra.glitch.me")
            emb.set_image(url="https://oyuncubur.com/wp-content/uploads/2019/02/spotify-gif-oliver-keane.gif")
            await webhook.send(embed=emb, username="Spotify", avatar_url="https://image.flaticon.com/icons/png/512/2111/2111624.png")

    @command(aliases=["reboot", "yenidenbaşlat", "kapan"]) # Owner Only
    async def die(self, ctx):
        await Logger.guildLogger(self, ctx)
        mesaj = await ctx.send("Botu Yeniden Başlatmak için 👋 emojisine basınız.")
        await mesaj.add_reaction("👋")
        def check(react, user):
            return user.id == owner 
        react, user = await self.bot.wait_for('reaction_add', timeout=25, check=check)  
        if str(react.emoji) == '👋':
            await mesaj.delete()
            await ctx.send("Bot Yeniden Başlatılıyor!")
            await self.bot.logout()

    @commands.Cog.listener('on_raw_reaction_add')
    async def reaksiyon_eklendi(self, payload):
        for role_id, msg_id, emoji in self.reactions:
            if msg_id == payload.message_id and emoji == str(payload.emoji.name.encode("utf-8")):
                await payload.member.add_roles(self.bot.get_guild(payload.guild_id).get_role(role_id))
                roles = self.bot.get_guild(payload.guild_id).get_role(role_id)
                member = self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
                return await member.send(f"**{roles.name}** adlı rol verildi")

    @commands.Cog.listener('on_raw_reaction_remove')
    async def reaksiyon_cıkarıldı(self, payload):
        for role_id, msg_id, emoji in self.reactions:
            if msg_id == payload.message_id and emoji == str(payload.emoji.name.encode("utf-8")):
                guild = self.bot.get_guild(payload.guild_id)
                await guild.get_member(payload.user_id).remove_roles(guild.get_role(role_id))
                roles = self.bot.get_guild(payload.guild_id).get_role(role_id)
                member = self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
                return await member.send(f"**{roles.name}** adlı rol geri alındı")

    @command(aliases=['reactionrole'])
    @commands.has_permissions(administrator=True)
    @commands.bot_has_permissions(administrator=True)
    @commands.guild_only()
    async def tepkirol(self, msg, role: discord.Role=None, message: discord.Message=None, emoji=None):
        await Logger.guildLogger(self, msg)
        if role != None and message != None and emoji != None:
            if str(emoji.encode("utf-8")).startswith("b'<"):
                emb = discord.Embed(color=Kırmızı, description=f"{msg.author.mention}, kullanıcağınız emoji discordun kendi orjinal emojisi olmalıdır")
                return await msg.send(embed=emb, delete_after=25)

            await message.add_reaction(emoji)
            self.reactions.append((role.id, message.id, str(emoji.encode('utf-8'))))
            async with aiofiles.open("reaction_roles.txt", mode="a") as file:
                emoji_utf = emoji.encode("utf-8")
                await file.write(f"{role.id} {message.id} {emoji_utf}\n")
            emb = discord.Embed(color=msg.guild.me.color, title=f"Tepkili rol oluşturuldu {emoji} tıklayarak rolü alabilirsiniz", description="botun rolünün vericeği rolden yukarıda olduğuna emin olun yoksa veremez.")
            emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            emb.set_footer(text=Footer)
            return await msg.send(embed=emb)
        else:
            emb = discord.Embed(color=Kırmızı, description=f"Doğru kullanım yapılmadı, Kullanım:\n```+tepkirol [rolID] [mesajID] [:emoji:]```")
            return await msg.send(embed=emb, delete_after=25)

    @tepkirol.error
    async def tepkirol_error(self, msg, err):
        if isinstance(err, commands.MissingPermissions):
            emb = discord.Embed(color=Kırmızı, description=f"Bu komutu kullanabilmek için **Yöneticilik** yetkisine sahip olmanız gerek")
            return await msg.send(embed=emb, delete_after=25)
        if isinstance(err, commands.BotMissingPermissions):
            emb = discord.Embed(color=Kırmızı, description=f"Botta **Yöneticilik** yetkisi bulunmuyor")
            return await msg.send(embed=emb, delete_after=25)
        if isinstance(err, commands.BadArgument):
            emb = discord.Embed(color=Kırmızı, description=f"hatalı kullanım yapılmadı, Kullanım:\n```+tepkirol [rolID|@rol] [mesajID|mesajURL] [:emoji:]```")
            return await msg.send(embed=emb, delete_after=25)

    @commands.Cog.listener('on_member_join')
    async def member_join(self, member):
        with sqlite3.connect('users.db') as db:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM autorole')
            db.commit()
            veri = cursor.fetchall()
            if veri:
                for i in veri:
                    if i[0] == member.guild.id:
                        role = self.bot.get_guild(i[0]).get_role(i[1])
                        channel = self.bot.get_guild(i[0]).get_channel(i[2])
                        try:
                            await member.add_roles(role)
                        except Exception:
                            emb = discord.Embed(color=Kırmızı, title="Hata", description=f"{member.mention} adlı kullanıcıya otorol verilemedi botun rolünün vermesi gereken rolden yukarda olmasına dikkat edin.")
                            emb.set_footer(text=Footer)
                            return await channel.send(embed=emb)
                        emb = discord.Embed(color=member.guild.me.color, title="Moderasyon LOG", description=f"Hoşgeldin {member.mention} seninle birlikte **{member.guild.member_count}** kişi olduk.")
                        emb.set_footer(text=Footer)
                        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                        return await channel.send(embed=emb)

    @command(aliases=['autorole'])
    @commands.has_permissions(administrator=True)
    @commands.bot_has_permissions(administrator=True)
    @commands.guild_only()
    async def otorol(self, msg, role: discord.Role=None, channel: discord.TextChannel=None):
        await Logger.guildLogger(self, msg)
        if role != None and channel != None:
            with sqlite3.connect('users.db') as db:
                cursor = db.cursor()
                guild = msg.guild.id
                cursor.execute(f'SELECT * FROM autorole WHERE guild == {guild}')
                db.commit()
                veri = cursor.fetchone()
                if veri is not None:
                    emb = discord.Embed(color=Kırmızı, description=f"{msg.author.mention}, **Otorol** zaten açık")
                    return await msg.send(embed=emb, delete_after=30)

                elif veri is None:
                    cursor.execute(f"INSERT INTO autorole VALUES({msg.guild.id}, {role.id}, {channel.id})")
                    db.commit()                       
                    emb = discord.Embed(color=msg.guild.me.color, description=f"{role.mention} adlı rol sunucuya yeni katılan kullanıcılara verilicek {channel.mention} adlı kanala loglanıcak Botun rolünün vericeği rolden üstte olduğuna bakınız.", title="Otorol Başarıyla Açıldı")
                    emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                    emb.set_footer(text=Footer)
                    return await msg.send(embed=emb)

        else:
            emb = discord.Embed(color=Kırmızı, description=f"hatalı kullanım yapılmadı, Kullanım:\n```+otorol [rolID|@rol] [kanalID|#kanal]```")
            return await msg.send(embed=emb, delete_after=25)

    @otorol.error
    async def otorol_error(self, msg, err):
        if isinstance(err, commands.MissingPermissions):
            emb = discord.Embed(color=Kırmızı, description=f"Bu komutu kullanabilmek için **Yöneticilik** yetkisine sahip olmanız gerek")
            return await msg.send(embed=emb, delete_after=25)
        if isinstance(err, commands.BotMissingPermissions):
            emb = discord.Embed(color=Kırmızı, description=f"Botta **Yöneticilik** yetkisi bulunmuyor")
            return await msg.send(embed=emb, delete_after=25)
        if isinstance(err, commands.BadArgument):
            emb = discord.Embed(color=Kırmızı, description=f"hatalı kullanım yapılmadı, Kullanım:\n```+otorol [rolID|@rol] [kanalID|#kanal]```")
            return await msg.send(embed=emb, delete_after=25)

    @command(aliases=['autoroleoff'])
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def otorolkapat(self, msg):
        await Logger.guildLogger(self, msg)
        with sqlite3.connect('users.db') as db:
            cursor = db.cursor()
            cursor.execute(f'SELECT * FROM autorole WHERE guild == {msg.guild.id}')
            db.commit()
            veri = cursor.fetchone()
            if veri:
                cursor.execute(f'DELETE FROM autorole WHERE guild == {msg.guild.id}')
                db.commit()
                emb = discord.Embed(color=msg.guild.me.color, title="Otorol Başarıyla Kapatıldı")
                emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                emb.set_footer(text=Footer)
                return await msg.send(embed=emb)
            
            else:
                emb = discord.Embed(color=Kırmızı, description=f"{msg.author.mention}, **Otorol** zaten kapalı")
                return await msg.send(embed=emb, delete_after=30)

    @otorolkapat.error
    async def otorolkapat_error(self, msg, err):
        if isinstance(err, commands.MissingPermissions):
            emb = discord.Embed(color=Kırmızı, description=f"Bu komutu kullanabilmek için **Yöneticilik** yetkisine sahip olmanız gerek")
            return await msg.send(embed=emb, delete_after=25)

def setup(bot):
    bot.add_cog(Moderation(bot))