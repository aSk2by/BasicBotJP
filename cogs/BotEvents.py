from discord.ext import commands



class BotEvents(commands.Cog):
    def __init__(self, bot):

        super().__init__()
        self.bot = bot

    
    # <--- Console Ready --->
    @commands.Cog.listener()
    async def on_ready(self):

        date = BotEvents.get_time()
        msg = f'---> Reboot Successfully.\n---> {self.bot.user}\n---> {date}'

        print('---> Reboot Successfully.')
        print(f'---> {self.bot.user}')

        await self.bot.get_channel('ここにBOTがログインした時に通知するチャンネルIDを記入').send(msg)


def setup(bot):

    return bot.add_cog(BotEvents(bot))