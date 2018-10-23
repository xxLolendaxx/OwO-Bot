import discord
from discord.ext import commands
import os
import random

image = ["https://i.imgur.com/OLMDuOI.jpg",
         "https://i.imgur.com/KOzp8pI.jpg",
         "https://pics.me.me/notices-your-hug-owo-whats-this-uwu-ironically-3584782.png",
         "https://pics.ballmemes.com/n-emergency-alerts-presidential-alert-rawr-x3-nuzzles-owo-me-irl-36663745.png",
         "https://pics.me.me/owo-whats-this-uwu-3659991.png",
         "https://discordemoji.com/assets/emoji/owo.png",
         "https://pics.esmemes.com/owo-stealing-memes-your-memes-being-stolen-37100155.png",
         "https://pics.esmemes.com/owo-adobe-owo-cc-2017-app-me-irl-32391248.png",
         "https://pics.me.me/w-nintendo-switch-tm-owo-whats-this-ninji-5238992.png",
         "https://res.cloudinary.com/teepublic/image/private/s--x2SgWZDp--/c_crop,x_10,y_10/c_fit,w_846/c_crop,g_north_west,h_1007,w_1007,x_-81,y_-353/l_upload:v1507037313:production:blanks:n2pk899a8qrzxtz4tyvn/fl_layer_apply,g_north_west,x_-208,y_-484/b_rgb:a8006a/c_limit,f_jpg,h_630,q_90,w_630/v1531260375/production/designs/2877161_0.jpg",
         "https://slm-assets0.secondlife.com/assets/21343454/view_small/OWO_MP.jpg",
         "https://discordemoji.com/assets/emoji/100owo.png",
         "https://images.discordapp.net/avatars/289066747443675143/0d8ad3a7a6b0a56f3527019c00ccc4b0.png",
         "https://pics.me.me/tm-owo-rawr-xd-31293610.png",
         "https://preview.redd.it/crmu5sgczvk01.jpg",
         "https://i.redd.it/qlmez4obf4b11.jpg",
         "https://scontent-ort2-1.cdninstagram.com/vp/734743e679d85ec4a076bb6121e3a4fe/5C49B974/t51.2885-15/e35/c0.90.720.720/s480x480/41565136_2194608784118944_5539050201098789449_n.jpg",
         "https://i.pinimg.com/originals/fe/78/4b/fe784bbde546b1c7aebe0006c3b08875.png",
         "https://pics.me.me/8-11-am-discord-discordapp-hello-thank-u-for-making-a-31534190.png",
         "https://i.imgur.com/8zA95lZ.jpg"]
random.shuffle(image)

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=f"With A Body Pillow"))
         
@bot.command()
async def owo(ctx):
    embed=discord.Embed(title="owo", color=0xff08ea)
    embed.set_image(url=random.choice(image))
    embed.set_footer(text="Made with ❤ by xxLolendaxx#8872")
    await ctx.send(embed=embed)
       
@bot.command()
async def help(ctx):
    embed=discord.Embed(title="OwO Guide", color=0xff08ea)
    embed.add_field(name="!help", value = "Shows this message owo", inline = False)
    embed.add_field(name="!owo", value = "Shows a random owo", inline = False)
    embed.set_footer(text="Made with ❤ by xxLolendaxx#8872")
    await ctx.send(embed=embed)

bot.run(os.environ['TOKEN'])
