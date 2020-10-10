import discord, sys
import asyncio
from discord.ext import commands
from discord.ext.commands import command
sys.path.append('../')
from config.ayarlar import *
from log.logger import Logger

class Help(commands.Cog, name="Yardım"):
    def __init__(self, bot):
        self.bot = bot

    async def economy(self, msg):
        emb = discord.Embed(color=msg.guild.me.color, title="Ekonomi Komutları")
        emb.set_footer(text=f"Sayfa 8/10")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.add_field(name=f"`{prefix}bakiye, cüzdan, balance, bal`", value="Bottaki bakiyenizi sorgular eğer ilk defa kullandıysanız hesabınıza para aktarılır.", inline=False)
        emb.add_field(name=f"`{prefix}dilen, beg`", value="Para dilenirsiniz şansınız yaver giderse para kazanırsınız.", inline=False)
        emb.add_field(name=f"`{prefix}sıralama, rich, leaderboard`", value="Sunucudaki kullanıcıların bakiye sıralamasını yapar en zenginler ortaya çıkar.", inline=False)
        emb.add_field(name=f"`{prefix}paragönder, pg, transfer`", value="Etiketlediğiniz kullanıcıya bellirttiğiniz miktarda para gönderir.", inline=False)
        emb.add_field(name=f"`{prefix}günlükbonus, günlük, daily`", value="Size günlük olarak para verir.", inline=False)
        emb.add_field(name=f"`{prefix}saatlikbonus, saatlik, hourly`", value="Size saatlik olarak para verir.", inline=False)
        return emb

    async def moderation(self, msg):
        emb = discord.Embed(color=msg.guild.me.color, title="Ekonomi Komutları", description="Buradaki komutları kullanmak için sunucuda belli yetkilere sahip olmanız gerekir ve aynı zamanda bottada bu yetkilerin olması gerekir.")
        emb.set_footer(text=f"Sayfa 6/10")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.add_field(name=f"`{prefix}temizle, clear, t`", value="1-500 arasında belirttiğiniz kadar mesaj siler. [**Mesajları Yönet Yetkisi**]", inline=False)
        emb.add_field(name=f"`{prefix}ban`", value="Etiketlediğiniz kullanıcıyı yasaklar. [**Banlama Yetkisi**]", inline=False)
        emb.add_field(name=f"`{prefix}kick`", value="Etiketlediğiniz kullanıcıyı atar. [**Atma Yetkisi**]", inline=False)
        emb.add_field(name=f"`{prefix}tepkirol, reactionrole`", value="Sunucuda tepkiye basınca rol uygulaması başlatırsınız. [**Yöneticilik**]", inline=False)
        emb.add_field(name=f"`{prefix}otorol, autorole`", value="Sunucuda otorol açarsınız [**Yöneticilik**]", inline=False)
        emb.add_field(name=f"`{prefix}otorolkapat, autoroleoff`", value="Otorolü kapatırsınız [**Yöneticilik**]", inline=False)
        return emb
    
    async def spotify(self, msg):
        emb = discord.Embed(color=msg.guild.me.color, title="Spotify", description="Bu komut bu botu özel kılan bir komuttur bir nevi spotify premium olarak adlandırılabilir.")
        emb.set_footer(text=f"Sayfa 2/10")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.add_field(name=f"`{prefix}spotify, sp`", value="Spotifydan müzik dinliyorsanız +spotify. Başkasının şarkılarını dinlemek istiyosanız +spotify @kullanıcı şeklinde kullanılır. Kullanıcı o an spotifydan ne dinliyosa botta aynı müzigi çalar müzik değişirse bottada değişir.", inline=False)
        emb.add_field(name=f"`{prefix}dur, stop, susamk`", value="Döngüyü ve şarkıyı durdurur.", inline=False)
        emb.add_field(name=f"`{prefix}çık, sg, dc, siktirgit, fuckoff`", value="Döngüyü durdurur ve odadan çıkar.", inline=False)
        emb.add_field(name=f"`{prefix}spbilgi, song, songinfo`", value="Spotifyda sizin veya etiketlediğiniz kişinin şarkısının bilgilerini verir.", inline=False)
        emb.add_field(name=f"`{prefix}arama sp, search sp`", value="spotify'dan arama yaparsınız başlat tik tepkisine basarsanız odanıza gelir ve botta oynatır.", inline=False)
        return emb

    async def games(self, msg):
        emb = discord.Embed(color=msg.guild.me.color, title="Oyunlar")
        emb.set_footer(text=f"Sayfa 7/10")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.add_field(name=f"`{prefix}sayıtahmin, tahmin`", value="Sayı tahmin oyunu oynatır.", inline=False)
        emb.add_field(name=f"`{prefix}gorilla, xox, sos`", value="Goril temalı xox oyunu oynarsınız.", inline=False)
        emb.add_field(name=f"`{prefix}slot, slots`", value="Slot oynarsınız **[Para basmanız gerek]**", inline=False)
        emb.add_field(name=f"`{prefix}yazıtura, spincoin, yt`", value="Yazıtura oynarsınız **[Para basmanız gerek]**", inline=False)
        return emb

    async def general(self, msg):
        emb = discord.Embed(color=msg.guild.me.color, title="Genel Komutlar")
        emb.set_footer(text=f"Sayfa 5/10")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.add_field(name=f"`{prefix}avatar, pp, a`", value="Avataranızı veya etiketlerseniz o kişinin avatarını göterir.", inline=False)
        emb.add_field(name=f"`{prefix}çeviri, translate, tr`", value="yazdıgınız cümlenin hangi dil oldugunu algılayıp onu belirttiginiz dile çevirir.'+çeviri ru yarın görüşürüz' kullanımı bu şekildedir.", inline=False)
        emb.add_field(name=f"`{prefix}kbilgi, user, info`", value="Hesabınız hakkında bilgi verir başka bir kullanıcıda etiketlenebilir.", inline=False)
        emb.add_field(name=f"`{prefix}sunucu, guild, server`", value="Sunucu hakkında bilgi verir.", inline=False)
        emb.add_field(name=f"`{prefix}yaz, say`", value="Bota istediğiniz mesajı yazdırır.", inline=False)
        emb.add_field(name=f"`{prefix}davet, beniekle, invite, inv`", value="Botun davet linkini atar.", inline=False)
        emb.add_field(name=f"`{prefix}eyaz, emojiyazı`", value="Yazdıgınız mesajı emojiye çevirir.", inline=False)
        emb.add_field(name=f"`{prefix}kronometre, stopwatch, sw, afk`", value="Kronometre başlatırsınız komutu birdaha kullandığınızda kaç saniye olduğunu söyler", inline=False)
        return emb

    async def music2(self, msg):
        emb = discord.Embed(color=msg.guild.me.color, title="Müzik Komutları")
        emb.set_footer(text=f"Sayfa 4/10")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.add_field(name=f"`{prefix}çıkar, remove`", value=f"**{prefix}sıradakiler** komutu ile numarası ögrenilen şarkı listeden çıkarılır.", inline=False)
        emb.add_field(name=f"`{prefix}katıl, join, k`", value="Odaya katılır", inline=False)
        emb.add_field(name=f"`{prefix}çık, sg, dc, siktirgit, fuckoff`", value="Odadan ayrılır", inline=False)
        emb.add_field(name=f"`{prefix}duraklat, pause`", value="Çalan parçayı +devam yazana kadar duraklatır.", inline=False)
        emb.add_field(name=f"`{prefix}devam, resume`", value="Duraklatılmış şarkıyı devam ettirir.", inline=False)
        emb.add_field(name=f"`{prefix}çalan, np`", value="Çalan şarkıyı gösterir.", inline=False)
        emb.add_field(name=f"`{prefix}ses, volume, v`", value="Ses seviyesini ayarlar. Yanına sayı belirtmeden kullanımda anlık olarak ses değiştirebileceginiz arayüz atar.", inline=False)
        emb.add_field(name=f"`{prefix}arama, search`", value="Spotify, Youtube ve SoundCloud platformlarından arama yapar dilerseniz sonucu botta çalmaya başlar.", inline=False)
        return emb

    async def music(self, msg):
        emb = discord.Embed(color=msg.guild.me.color, title="Müzik Komutları")
        emb.set_footer(text=f"Sayfa 3/10")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.add_field(name=f"`{prefix}çal, play, p`", value="Şarkı ismi, youtubeURL, ve spotifyURL girdilerini bulup botta çalmaya başlar.", inline=False)
        emb.add_field(name=f"`{prefix}dur, stop, susamk`", value="Çalan müziği durdurur ve sırada müzik varsa hepsini siler.", inline=False)
        emb.add_field(name=f"`{prefix}tekrar, loop, repeat`", value="Çalan şarkıyı siz bidaha bu komutu kullanana kadar tekrar tekrar çalar.", inline=False)
        emb.add_field(name=f"`{prefix}reset, again, yeniden`", value="Çalan şarkıyı başa sarar.", inline=False)
        emb.add_field(name=f"`{prefix}karıştır, shuffle`", value="Sırada şarkı varsa o şarkı kuyruğunu karıştırır.", inline=False)
        emb.add_field(name=f"`{prefix}geç, skip, next, n`", value=f"Sırada şarkı varsa bir sonraki şarkıya geçer **{prefix}sıradakiler** komutu ile sıradaki şarkı numarasına görede geçiş yapılabilir.", inline=False)
        emb.add_field(name=f"`{prefix}sıradakiler, queue, q`", value="Sırada şarkı varsa onları gösterir.", inline=False)
        return emb

    async def image(self, msg):
        emb = discord.Embed(color=msg.guild.me.color, title="Görüntü İşleme")
        emb.set_footer(text=f"Sayfa 9/10")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.add_field(name=f"`{prefix}magik, gmagik`", value="Avatarınızı yada verdiğiniz resmi yamultur komik hale getirir", inline=False)
        emb.add_field(name=f"`{prefix}deepfry`", value="Avatarınızı yada verdiğiniz resmin rekleriyle oynar", inline=False)
        emb.add_field(name=f"`{prefix}trump, trumptweet`", value="Yazdığınız mesajı trump tweetine çevirir", inline=False)
        emb.add_field(name=f"`{prefix}iphone, iphonex`", value="Avatarınızı veya verdiğiniz fotoyu iphone koyar", inline=False)
        emb.add_field(name=f"`{prefix}clyde`", value="Discord clyde bota fake mesaj yazdırırsınız", inline=False)
        emb.add_field(name=f"`{prefix}cmm, changemymind`", value="Change My Mind pankartına yazı yazarsınız", inline=False)
        emb.add_field(name=f"`{prefix}jpeg`", value="Avatarınıza yada verdiğiniz fotoyu bok eder", inline=False)
        emb.add_field(name=f"`{prefix}phyorum, phcomment`", value="PornHubda yorum yaparsınız", inline=False)
        return emb

    async def nsfw(self, msg):
        emb = discord.Embed(color=msg.guild.me.color, title="NSFW", description="Bu kısımdaki komutlar sadece NSFW ayarı açık kanallarda kullanılabilir.")
        emb.set_footer(text=f"Sayfa 10/10")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.add_field(name=f"`{prefix}porno, porn, pgif`", value="Porno gif'i atar", inline=False)
        emb.add_field(name=f"`{prefix}boobs, göğüsler, tits`", value="Göğüs gif'i atar", inline=False)
        emb.add_field(name=f"`{prefix}ass, kalça`", value="Kalça gif'i atar", inline=False)
        emb.add_field(name=f"`{prefix}pussy, amcık, 250gr`", value="250gr gif'i atar", inline=False)
        emb.add_field(name=f"`{prefix}anal`", value="Arka bölüm aga", inline=False)
        emb.add_field(name=f"`{prefix}hentai, paizure`", value="Hentai atar", inline=False)
        emb.add_field(name=f"`{prefix}sizdengelenler`", value="Tüm dünyadan global olarak sizin gönderdiğiniz fotoğraflar", inline=False)
        return emb

    async def mainpage(self, msg):
        msj = "⭐**Spotify:** `2`\n"
        msj += "🎵**Müzik:** `3-4`\n"
        msj += "👥**Genel:** `5`\n"
        msj += "⚒️**Moderasyon:** `6`\n"
        msj += "🎲**Oyunlar:** `7`\n"
        msj += "💰**Ekonomi:** `8`\n"
        msj += "🧠**Görüntü İşleme:** `9`\n"
        msj += "🔞**NSFW:** `10`"
        emb = discord.Embed(color=msg.guild.me.color,title=msj)
        emb.set_footer(text=f"{Footer} 1/10")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        return emb

    @command(aliases=["help", "h", "hlp", "pulchra"])
    async def yardım(self, msg):
        await Logger.guildLogger(self, msg)
        mainpage = await self.mainpage(msg)
        economy = await self.economy(msg)
        spotify = await self.spotify(msg)
        music = await self.music(msg)
        music2 = await self.music2(msg)
        genel = await self.general(msg)
        oyunlar = await self.games(msg)
        moderation = await self.moderation(msg)
        image = await self.image(msg)
        nsfw = await self.nsfw(msg)
        embed = await msg.send(embed=mainpage)
        await embed.add_reaction('\u23EE')  # baş
        await embed.add_reaction('\u25c0')  # sol
        await embed.add_reaction('\u25b6')  # sağ
        await embed.add_reaction('\u23ED')  # son
        pages = [mainpage,spotify,music,music2,genel,moderation,oyunlar,economy,image,nsfw]
        i = 0
        click = ""
        while True:              
            if click == '\u23EE':
                if i != 0:
                    i = 0
                    await embed.edit(embed=pages[i])
            elif click == '\u25c0':
                if i > 0:
                    i -= 1
                    await embed.edit(embed=pages[i])
            elif click == '\u25b6':
                if i < 9:
                    i += 1
                    await embed.edit(embed=pages[i])
            elif click == '\u23ED':
                if i != 9:
                    i = 9
                    await embed.edit(embed=pages[i])
            
            def check(react, user):
                return user == msg.author
            
            try:
                react, user = await self.bot.wait_for('reaction_add', timeout=60, check=check)
            except asyncio.TimeoutError:
                break
            click = str(react.emoji)
            await react.remove(msg.author)

def setup(bot):
    bot.add_cog(Help(bot))