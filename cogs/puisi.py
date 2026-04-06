import discord
from discord.ext import commands

class Puisi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def puisi(self, ctx):
        # Contoh puisi 4 baris sederhana
        teks_puisi = (
            "Jalan-jalan ke kota tua,\n"
            "Melihat gedung yang penuh cerita.\n"
            "Meskipun koding penuh tanda tanya,\n"
            "Error di-*solve* hati gembira."
        )
        
        # Menggunakan Embed agar tampilan di Discord lebih cantik
        embed = discord.Embed(title="📜 Puisi Untukmu", description=teks_puisi, color=discord.Color.blue())
        await ctx.send(embed=embed)

# Fungsi wajib untuk mendaftarkan Cog ini ke main.py
async def setup(bot):
    await bot.add_cog(Puisi(bot))