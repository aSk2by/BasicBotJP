import asyncio
import math
import re

import discord
from discord.ext import commands



class Commands(commands.Cog):
    def __init__(self, bot):

        super().__init__()
        self.bot= bot


    # <--- aSk2by Command --->
    @commands.command()
    async def aSk2by(self, ctx):

        embed = discord.Embed(title='aSk2byですか？', description='このBOTの開発者ですよ', color=0x0072ff)
        embed.add_field(name='連絡先はこちらです', value='discord : aSk2by#1433')
        embed.set_footer(text='BasicBotJP by aSk2by')
        await ctx.send(embed=embed)


    # <--- Help Command --->
    @commands.command()
    async def help(self, ctx, args=None):

        HelpCommandList = {
        'ping': 'WebSocket Latencyをms形式で送信します',
        'info': '指定したユーザーの名前とIDとオンライン状態と一番上位権限のロールとサーバーに参加した日時とアイコンを送信します',
        'serverinfo': 'サーバーの名前とIDとロール数とメンバー数とアイコンを送信します',
        'delete': '過去200件のトークの削除を試みます。消せない可能性もあります',
        'mute': '指定したユーザーをサーバーミュートにします。通話に参加していない場合サーバーミュートに出来ません',
        'unmute': '指定したユーザーのサーバーミュートを解除します。通話に参加していない場合サーバーミュートを解除出来ません',
        'link': 'IDか名前で指定したチャンネルへのリンクを作成します。BOTが参加していないサーバーのリンクは作成出来ません',
        'kick': '指定したユーザーを追放します。BOTより上位の権限者を追放することは出来ません',
        'ban': '指定したユーザーを永久追放します。BOTより上位の権限者を永久追放することは出来ません',
        'support': 'BasicBotJPの問い合わせ先を送信します',
        }
        if not args: # 引数が何もなかった場合
            embed = discord.Embed(title='BasicBotJP Help', description='BasicBotJPのコマンドリストです', color=0x0072ff)
            embed.add_field(name='情報系コマンド', value='!ping\n・処理速度を計測し、送信します\n\n!info @user\n・指定したユーザーの情報を表示\n\n!serverinfo\n・サーバーの情報を表示します')
            embed.add_field(name='サーバーコマンド', value='!delete\n・トーク履歴を削除します\n\n\!mute @user\n・指定したユーザーをサーバーミュートにします\n\n!unmute @user\n・指定したユーザーのサーバーミュートを解除します\n\n!link id or name\n・IDか名前で指定したチャンネルへのリンクを作成します\n\n!kick @user\n・指定したユーザーをサーバーから追放します\n\n!ban @user\n・指定したユーザーをサーバーから永久追放します')
            embed.add_field(name='その他', value='!support\n・BasicBotJPに関する問い合わせ先を表示します\n\n!help CommandName\n・指定したコマンドの詳細を送信します')
            embed.set_footer(text='BasicBotJP by aSk2by')
            await ctx.send(embed=embed)
        elif args in HelpCommandList: # 引数があった場合
            embed = discord.Embed(title='BasicBotJP Command - {0}'.format(args), description='{0}'.format(HelpCommandList[args]), color=0x0072ff)
            embed.set_footer(text='BasicBotJP by aSk2by')
            await ctx.send(embed=embed)
        else: # 引数があったが、正常な引数じゃない場合
            embed = discord.Embed(title='BasicBotJP Help', description='指定されたコマンドが見つかりませんでした。!helpで一覧をご確認下さい', color=0x0072ff)
            embed.set_footer(text='BasicBotJP by aSk2by')
            await ctx.send(embed=embed)


    # <--- Support Command --->
    @commands.command()
    async def support(self, ctx):

        embed = discord.Embed(title='Support', description='discord: aSk2by#1433', color=0x0072ff)
        embed.set_footer(text='BasicBotJP by aSk2by')
        await ctx.send(embed=embed)


    # <--- Ping Command --->
    @commands.command()
    async def ping(self, ctx):

        embed = discord.Embed(title='Pong! :ping_pong:', description='WebSocket Latency: {0} ms'.format(math.floor(self.bot.latency * 1000)), color=0x0072ff)
        embed.set_footer(text='BasicBotJP by aSk2by')
        await ctx.send(embed=embed)


    # <--- Delete Command --->
    @commands.command()
    async def delete(self, ctx):

        if ctx.author.guild_permissions.administrator: # 管理人かどうか
            await ctx.channel.purge()
            embed = discord.Embed(title='Delete System', description='このメッセージは10秒後に削除されます', color=0x0072ff)
            embed.set_footer(text='BasicBotJP by aSk2by')
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(10)
            await msg.delete()
        else:
            embed = discord.Embed(title='Delete System', description=f'{ctx.author.name}さんには実行権限がありません', color=0x0072ff)
            embed.set_footer(text='BasicBotJP by aSk2by')
            await ctx.send(embed=embed)

    
    # <--- Mute Command --->
    @commands.command()
    async def mute(self, ctx, user: discord.Member):

        try:
            if ctx.author.guild_permissions.mute_members: # コマンドの送信者がメンバーをミュートにする権限を持っているか
                member = ctx.guild.get_member(user.id)
                if member.voice.mute: # ミュートかどうか
                    embed = discord.Embed(title='Mute System', description='{0}さんは既にミュートになっています\n解除するには !unmute @user を実行して下さい'.format(user.name), color=0x0072ff)
                    embed.set_thumbnail(url=user.avatar_url)
                    embed.set_footer(text='BasicBotJP by aSk2by')
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title='Mute System', description='{0}さんをミュートしました\n解除するには !unmute @user を実行して下さい'.format(user.name), color=0x0072ff)
                    embed.set_thumbnail(url=user.avatar_url)
                    embed.set_footer(text='BasicBotJP by aSk2by')
                    await member.edit(mute=True)
                    await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title='Mute System', description='{0}さんには実行権限がありません'.format(ctx.author.name), color=0x0072ff)
                embed.set_thumbnail(url=user.avatar_url)
                embed.set_footer(text='BasicBotJP by aSk2by')
                await ctx.send(embed=embed)
        except discord.errors.HTTPException: # 対象がボイスチャンネルに参加していない
            embed = discord.Embed(title='Mute System', description='{0}さんはボイスチャンネルに参加していません'.format(user.name), color=0x0072ff)
            embed.set_footer(text='BasicBotJP by aSk2by')
            await ctx.send(embed=embed)
        except: # 対象をメンションしていない
            embed= discord.Embed(title='Mute System', description='ミュートしたいユーザーをメンションして下さい', color=0x0072ff)
            embed.set_footer(text='BasicBotJP by aSk2by')
            await ctx.send(embed=embed)


    # <--- UnMute Command --->
    @commands.command()
    async def unmute(self, ctx, user: discord.Member):

        try:
            if ctx.author.guild_permissions.mute_members: # コマンドの送信者がメンバーをミュートにする権限を持っているか
                member = ctx.guild.get_member(user.id)
                if member.voice.mute:
                    embed = discord.Embed(title='UnMute System', description='{0}さんのミュートを解除しました\nミュートにするには !mute @user を実行して下さい'.format(user.name), color=0x0072ff)
                    embed.set_thumbnail(url=user.avatar_url)
                    embed.set_footer(text='BasicBotJP by aSk2by')
                    await member.edit(mute=False)
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title='UnMute System', description='{0}さんはミュートになっていません\nミュートにするには !unmute @user を実行して下さい'.format(user.name), color=0x0072ff)
                    embed.set_thumbnail(url=user.avatar_url)
                    embed.set_footer(text='BasicBotJP by aSk2by')
                    await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title='UnMute System', description='{0}さんには実行権限がありません'.format(ctx.author.name), color=0x0072ff)
                embed.set_thumbnail(url=user.avatar_url)
                embed.set_footer(text='BasicBotJP by aSk2by')
                await ctx.send(embed=embed)
        except discord.errors.HTTPException: # 対象がボイスチャンネルに参加していない
            embed = discord.Embed(title='UnMute System', description='{0}さんはボイスチャンネルに参加していません'.format(user.name), color=0x0072ff)
            embed.set_footer(text='BasicBotJP by aSk2by')
            await ctx.send(embed=embed)
        except: # 対象をメンションしていない
            embed = discord.Embed(title='UnMute System', description='ミュートを解除したいユーザーをメンションして下さい', color=0x0072ff)
            embed.set_footer(text='BasicBotJP by aSk2by')
            await ctx.send(embed=embed)

    
    # <--- Channel Command --->
    @commands.command()
    async def link(self, ctx, args=None):

        if not args: # 引数が何もなかった場合
            embed = discord.Embed(title='ChannelLink System', description='URLを表示したいチャンネルが指定されていません', color=0x0072ff)
            embed.set_footer(text='BasicBotJP by aSk2by')
            await ctx.send(embed=embed)
        else:
            result = re.fullmatch('[0-9]+', args) # 正規表現で引数が数字のみか判断
            if result == None: # 数字のみじゃない場合、名前で指定されている可能性を考慮して名前で検索
                guild = discord.utils.get(self.bot.guilds, name=ctx.guild.name)
                for ch in guild.channels:
                    if ch.name == args:
                        channel = ch.id
                        if ch.type == discord.ChannelType.voice: # 指定されたチャンネルがボイスチャンネルかどうか
                            embed = discord.Embed(title='ChannelLink System', description='Link: <#{0}>\nボイスチャンネルへのリンクアクセスはPCのみ可能です'.format(channel), color=0x0072ff)
                            embed.set_footer(text='BasicBotJP by aSk2by')
                            await ctx.send(embed=embed)
                            return
                        else:
                            embed = discord.Embed(title='ChannelLink System', description='Link: <#{0}>\nリンクをクリックするとテキストチャンネルへアクセスします'.format(channel), color=0x0072ff)
                            embed.set_footer(text='BasicBotJP by aSk2by')
                            await ctx.send(embed=embed)
                            return
                embed = discord.Embed(title='ChannelLink System', description='チャンネルが存在しないか\nBOTの参加していないサーバーのチャンネルです', color=0x0072ff)
                embed.set_footer(text='BasicBotJP by aSk2by')
                await ctx.send(embed=embed)
            else:
                channel = self.bot.get_channel(int(args))
                if channel == None:
                    embed = discord.Embed(title='ChannelLink System', description='チャンネルが存在しないか\nBOTの参加していないサーバーのチャンネルです', color=0x0072ff)
                    embed.set_footer(text='BasicBotJP by aSk2by')
                    await ctx.send(embed=embed)
                else:
                    guild = discord.utils.get(self.bot.guilds, name=ctx.guild.name)
                    for ch in guild.channels:
                        if ch.id == int(args):
                            channel = ch.id
                            if ch.type == discord.ChannelType.voice: # 指定されたチャンネルがボイスチャンネルかどうか
                                embed = discord.Embed(title='ChannelLink System', description='Link: <#{0}>\nボイスチャンネルへのリンクアクセスはPCのみ可能です'.format(channel), color=0x0072ff)
                                embed.set_footer(text='BasicBotJP by aSk2by')
                                await ctx.send(embed=embed)
                                return
                            else:
                                embed = discord.Embed(title='ChannelLink System', description='Link: <#{0}>\nリンクをクリックするとテキストチャンネルへアクセスします'.format(channel), color=0x0072ff)
                                embed.set_footer(text='BasicBotJP by aSk2by')
                                await ctx.send(embed=embed)
                                return
                    embed = discord.Embed(title='ChannelLink System', description='チャンネルが存在しないか\nBOTの参加していないサーバーのチャンネルです', color=0x0072ff)
                    embed.set_footer(text='BasicBotJP by aSk2by')
                    await ctx.send(embed=embed)


    # <--- Kick Command --->
    @commands.command()
    async def kick(self, ctx, user: discord.Member):

        try:
            if ctx.author.guild_permissions.kick_members: # コマンドの送信者がメンバーを追放する権限を持っているか
                embed = discord.Embed(title='Kick System', description='{}さんを追放しました'.format(user.name), color=0x0072ff)
                embed.set_thumbnail(url=user.avatar_url)
                embed.set_footer(text='BasicBotJP by aSk2by')
                await user.kick()
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title='Kick System', description=f'{ctx.author.name}さんには実行権限がありません', color=0x0072ff)
                embed.set_footer(text='BasicBotJP by aSk2by')
                await ctx.send(embed=embed)
        except discord.errors.Forbidden: # 対象がBOTよりも上位の権限者
            embed = discord.Embed(title='Kick System', description='BOTより上位の権限保持者を追放することは出来ません', color=0x0072ff)
            embed.set_footer(text='BasicBotJP by aSk2by')
            await ctx.send(embed=embed)
        except: # 対象をメンションしていない
            embed = discord.Embed(title='Kick System', description='追放したいユーザーをメンションして下さい', color=0x0072ff)
            embed.set_footer(text='BasicBotJP by aSk2by')
            await ctx.send(embed=embed)


    # <--- Ban Command --->
    @commands.command()
    async def ban(self, ctx, user: discord.Member):

        try:
            if ctx.author.guild_permissions.ban_members: # コマンドの送信者がメンバーをBANする権限を持っているか
                embed = discord.Embed(title='Ban System', description='{}さんを永久追放しました'.format(user.name), color=0x0072ff)
                embed.set_thumbnail(url=user.avatar_url)
                embed.set_footer(text='BasicBotJP by aSk2by')
                await user.ban()
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title='Ban System', description=f'{ctx.author.name}さんには実行権限がありません', color=0x0072ff)
                embed.set_footer(text='BasicBotJP by aSk2by')
                await ctx.send(embed=embed)
        except discord.errors.Forbidden: # 対象がBOTよりも上位の権限者
            embed = discord.Embed(title='Ban System', description='BOTより上位の権限保持者を永久追放することは出来ません', color=0x0072ff)
            embed.set_footer(text='BasicBotJP by aSk2by')
            await ctx.send(embed=embed)
        except: # 対象をメンションしていない
            embed = discord.Embed(title='Ban System', description='永久追放したいユーザーをメンションして下さい', color=0x0072ff)
            embed.set_footer(text='BasicBotJP by aSk2by')
            await ctx.send(embed=embed)


    # <--- Userinfo Command --->
    @commands.command()
    async def info(self, ctx, user: discord.Member):

        try:
            embed = discord.Embed(title='{}の情報'.format(user.name), description='Discord API情報', color=0x0072ff)
            embed.add_field(name='Name', value=user.name)
            embed.add_field(name='ID', value=user.id, inline=True)
            embed.add_field(name='Status', value=user.status, inline=True)
            embed.add_field(name='Role', value=user.top_role, inline=True)
            embed.add_field(name='Joined At', value=user.joined_at, inline=True)
            embed.set_thumbnail(url=user.avatar_url)
            embed.set_footer(text='BasicBotJP by aSk2by')
            await ctx.send(embed=embed)
        except: # 対象をメンションしていない
            embed = discord.Embed(title='Information System', description='情報を取得したいユーザーをメンションして下さい', color=0x0072ff)
            embed.set_footer(text='BasicBotJP by aSk2by')
            await ctx.send(embed=embed)


    # <--- Server Info Command --->
    @commands.command()
    async def serverinfo(self, ctx):

        embed = discord.Embed(title='{}の情報'.format(ctx.guild.name), description='Discord APIからの情報', color=0x0072ff)
        embed.add_field(name="Server Name", value=ctx.guild.name)
        embed.add_field(name="ID", value=ctx.guild.id, inline=True)
        embed.add_field(name="Roles", value=len(ctx.guild.roles), inline=True)
        embed.add_field(name="Members", value=len(ctx.guild.members))
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text='BasicBotJP by aSk2by')
        await ctx.send(embed=embed)


def setup(bot):

    return bot.add_cog(Commands(bot))