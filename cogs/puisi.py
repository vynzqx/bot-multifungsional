import discord
from discord.ext import commands
import random # Tambahkan modul ini untuk memilih secara acak

class Puisi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        # Menyimpan koleksi puisi di dalam list
        self.koleksi_puisi = [
            "Jalan-jalan ke kota tua,\nMelihat gedung yang penuh cerita.\nMeskipun koding penuh tanda tanya,\nError di-*solve* hati gembira.",
            
            "Pagi hari minum kopi hangat,\nSambil menatap layar monitor.\nJangan pernah hilang semangat,\nWalau bug datang bagai teror.",
            
            "Bunga mawar bunga melati,\nTumbuh indah di taman sari.\nCoding itu butuh teliti,\nAgar program jalan sendiri.",
            
            "Pergi ke pasar beli semangka,\nPulangnya mampir beli duku.\nBelajar Python tak kusangka,\nKini bot Discord jadi asistenku."
        ]

    @commands.command()
    async def puisi(self, ctx):
        # Memilih satu puisi secara acak dari list koleksi_puisi
        puisi_pilihan = random.choice(self.koleksi_puisi)
        
        # Menggunakan Embed agar tampilan di Discord lebih cantik
        embed = discord.Embed(
            title="📜 Puisi Spesial Untukmu", 
            description=puisi_pilihan, 
            color=discord.Color.purple()
        )
        embed.set_footer(text=f"Diminta oleh {ctx.author.display_name}")
        
        await ctx.send(embed=embed)

# Fungsi wajib untuk mendaftarkan Cog ini ke main.py
async def setup(bot):
    await bot.add_cog(Puisi(bot))