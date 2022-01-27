import sys
import os


ver = sys.version_info
if ver < (3, 10):
    print(ver)
    print('Python 3.10 or newer is required to run the bot.')
    print('You are currently using {0}.{1}.{2}.'.format(ver[0], ver[1], ver[2]), file=sys.stderr)
    sys.exit()

try:
    import discord
    from discord.ext import commands
except ImportError:
    if os.name == 'nt':
        command = 'py -3'
        print('\n'.join(['<--- Missing dependencies --->'.center(60),
                         'Please install the missing dependencies by running the following command:',
                         '{0} -m pip install --user -r requirements.txt'.format(command),
                         '',
                         'If you do not have pip and do not know how to install it, follow this link:',
                         'https://pip.pypa.io/en/stable/installation/',
                         '',
                         'If you need any further help with setting up and/or running the bot,',
                         ' we will be happy to help you in aSk2by#1433 on discord',
                         '',
                         '- The BasicBotJP developer']), file=sys.stderr)
    sys.exit()


def start():

    intents= discord.Intents.all()
    bot= commands.Bot(
        command_prefix = commands.when_mentioned_or('!'),
        case_insensitive = True,
        help_command = None,
        activity = discord.Game('BasicBotJP | !help'),
        intents = intents
        )

    return bot


bot = start()


extensions = [
    'cogs.Commands',
    'cogs.BotEvents',
]
for extension in extensions:
    bot.load_extension(extension)


bot.run('ここにトークンを記入')