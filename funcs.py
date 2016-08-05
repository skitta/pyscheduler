import sys

from plugins.slack.webhook import Robot


def timing_bot(context=''):
    bot = Robot('Hubot')
    bot.hook_url = '/services/T0EGWT6BU/B1X9ASVQU/0DZA0tEnuEmUNpXBiJbHkqte'
    return bot.send(context)

def __get_fn(fn_name):
    return getattr(sys.modules[__name__], fn_name)