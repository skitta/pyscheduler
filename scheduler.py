import json

from plugins.slack.webhook import Robot


def timing_bot(context=''):
    bot = Robot('Hubot')
    bot.hook_url = '/services/T0EGWT6BU/B1X9ASVQU/0DZA0tEnuEmUNpXBiJbHkqte'
    stdout = bot.send(context)
    print('sending message %s' % stdout)


if __name__ == '__main__':
    from setting import sched

    sched.add_job(timing_bot, 'interval', seconds=5, args=['test',])

    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        print('Shutdown By Keyboard Interrupt.')
