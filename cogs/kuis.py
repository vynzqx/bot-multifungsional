import discord
from discord.ext import commands

class Kuis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kuis(self, ctx):
        pertanyaan = "Bahasa pemrograman apa yang sering dipakai untuk membuat bot Discord?"
        jawaban = "Python"
        
        await ctx.send(f"KUIS WAKTUNYA!\n{pertanyaan}\n(Ketik jawabanmu di bawah!)")

        # Mengecek apakah jawaban dari user yang sama dan di channel yang sama
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            # Menunggu jawaban selama 15 detik
            msg = await self.bot.wait_for('message', check=check, timeout=15.0)
            
            if msg.content.lower() == jawaban.lower():
                await ctx.send(f"Benar sekali, {ctx.author.mention}! Jawabannya adalah {jawaban}.")
            else:
                await ctx.send(f"Sayang sekali, jawaban yang benar adalah {jawaban}.")
        except:
            await ctx.send("⏰ Waktu habis! Kamu terlalu lama menjawab.")

async def setup(bot):
    await bot.add_cog(Kuis(bot))