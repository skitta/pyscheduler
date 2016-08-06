import json

from apscheduler.schedulers.blocking import BlockingScheduler
from plugins.slack.webhook import Robot


sched = BlockingScheduler()


def timing_bot(context=''):
    bot = Robot('Hubot')
    bot.hook_url = '/services/T0EGWT6BU/B1X9ASVQU/0DZA0tEnuEmUNpXBiJbHkqte'
    stdout = bot.send(context)
    print('sending message %s' % stdout)


@sched.scheduled_job(trigger='cron', id='moring', hour=6, minute=30)
def good_morning():
    timing_bot('Good Morning')


@sched.scheduled_job(trigger='interval', id='test', seconds=5)
def test():
    timing_bot('test')


if __name__ == '__main__':
    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        print('Shutdown By Keyboard Interrupt.')
