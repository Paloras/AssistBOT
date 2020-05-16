# command.py
# Recycled 05/16/20
import random

import discord
from discord.ext import commands


def get_random_color():
    """Random generate color"""
    colors = ['white', 'black']
    return random.choice(colors)


class Command(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        """Return you latency"""
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        """8-ball game"""
        responses = ["It is certain (Бесспорно)",
                     "It is decidedly so (Предрешено)",
                     "Without a doubt (Никаких сомнений)",
                     "Yes — definitely (Определённо да)",
                     "You may rely on it (Можешь быть уверен в этом)",
                     "As I see it, yes (Мне кажется — «да»)",
                     "Most likely (Вероятнее всего)",
                     "Outlook good (Хорошие перспективы)",
                     "Signs point to yes (Знаки говорят — «да»)",
                     "Yes (Да)",
                     "Reply hazy, try again (Пока не ясно, попробуй снова)",
                     "Ask again later (Спроси позже)",
                     "Better not tell you now (Лучше не рассказывать)",
                     "Cannot predict now (Сейчас нельзя предсказать)",
                     "Concentrate and ask again (Сконцентрируйся и спроси опять)",
                     "Don’t count on it (Даже не думай)",
                     "My reply is no (Мой ответ — «нет»)",
                     "My sources say no (По моим данным — «нет»)",
                     "Outlook not so good (Перспективы не очень хорошие)",
                     "Very doubtful (Весьма сомнительно)"]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command()
    async def clear(self, ctx, amount=6):
        """Clear chat"""
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.has_role(670599227335770143)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Ban user."""
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention}')

    @commands.command()
    @commands.has_role(670599227335770143)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Ban user."""
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    @commands.command()
    @commands.has_role(691321624108073021)
    async def unban(self, ctx, *, member):
        """Unban user."""
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {member.mention}')

    @commands.command()
    async def users(self, ctx):
        """Return bot users"""
        user = ""
        for i in range(1, len(self.client.users)):
            user += str(self.client.users[i]) + "\n\t"
        await ctx.send(f'Bot users:\n\t' + str(user))

    @commands.command()
    async def spam(self, ctx, time=1, mes="..."):
        """Spam command"""
        for _ in range(time):
            await ctx.send(str(mes))

    @commands.command(aliases=['wbg'])
    async def WhatByGame(self, ctx):
        """Function for choice game"""
        responses = ["Fortnite", "CS:GO", "GTAV", "GTA:SA",
                     "PUBG", "SAR", "Rust", "RDR2", "Assassin's creed",
                     "Call of duty:Warzone"]
        await ctx.send(f'Play to {random.choice(responses)}')

    @commands.command(aliases=['rg'])
    async def RandomGame(self, ctx, *, games):
        """Random choice game"""
        await ctx.send(f'Play to {random.choice(games.split())}')

    @commands.command(aliases=['moa'])
    @commands.has_role(691321624108073021)
    async def MuteOrAdmin(self, ctx, question):
        if question == get_random_color():
            await ctx.author.add_roles(discord.utils.get(ctx.author.guild.roles, id=691280575369314345))
            await ctx.send(f'You winner!')
        else:
            await ctx.author.add_roles(discord.utils.get(ctx.author.guild.roles, id=710841640192835624))
            await ctx.author.remove_roles(discord.utils.get(ctx.author.guild.roles, id=691321624108073021))
            await ctx.author.remove_roles(discord.utils.get(ctx.author.guild.roles, id=703265211888435301))
            await ctx.send(f'You lose(')

    @commands.command()
    async def com(self, ctx):
        """Bot commands"""
        await ctx.send(f'Bot commands:'
                       f'\n\t * !ping - You ping,'
                       f'\n\t * !8ball question - Ball of predictions,'
                       f'\n\t * !clear Qty - Clear chat,'
                       f'\n\t * !kick @user - Kick user,'
                       f'\n\t * !ban @nickname - Ban user,'
                       f'\n\t * !unban nickname#user tag - Unban user,'
                       f'\n\t * !users - Bot users,'
                       f'\n\t * !spam qty message  - spam function,'
                       f'\n\t * !wbg - Advice on what to play,'
                       f'\n\t * !rg game1 game2 game3 ... gameN - Randomly chooses a game,'
                       f'\n\t * !lang lang(EN/RU) - Set language (in-dev),'
                       f'\n\t * !moa user color(white/black) - Game Black / White for the role,'
                       f'\n\t * !com - Bot commands.')


def setup(client):
    client.add_cog(Command(client))