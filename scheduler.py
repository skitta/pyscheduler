import json
import funcs

from apscheduler.schedulers.blocking import BlockingScheduler


def get_config(path):
    with open(path) as fp:
        return json.load(fp)

schedule = BlockingScheduler(get_config('config.json'))
tasks = get_config('tasks.json')

for task in tasks:
    try:
        func = funcs.__get_fn(task['func'])
        ttype = task['type']
        name = task['name']
        time = task['time']
        args = task['args']
        schedule.add_job(func, trigger=ttype, seconds=time, id=name, args=args)
    except Exception as e:
        print(e)   

schedule.start()
