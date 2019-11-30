import inquirer
import sys
import boto3
import pydoc
import string
from inquirer import themes
from inquirer.render.console import ConsoleRender, List
from readchar import key
import func

class ExtendedConsoleRender(ConsoleRender):
    def render_factory(self, question_type):
        if question_type == "list":
            return ExtendedList
        return super().render_factory(question_type)

class ExtendedList(List):
    def process_input(self, pressed):
        # vi style
        if pressed in ("k", "h"):
            pressed = key.UP
        elif pressed == "H":
            pressed = key.UP
        elif pressed in ("j", "l"):
            pressed = key.DOWN
        elif pressed == "q":
            pressed = key.CTRL_C
        super().process_input(pressed)

def open_inquirer(choice_list):
    try:
        inq_list = [
            inquirer.List(
                'list_huga',
                choices  = choice_list,
                carousel = True,)
        ]
        ans =  inquirer.prompt(
                    inq_list,
                    render = ExtendedConsoleRender())
        return ans['list_huga']
    except Exception as e:
        exit()

log_c = boto3.client('logs')

def list_loggroups():
    s = log_c.describe_log_groups()
    b = ['../']
    for i in s['logGroups']:
        b.append(i['logGroupName'])
    return b

def list_streams(log_group):
    s = log_c.describe_log_streams(
        # logGroupName = '/aws/lambda/start_stop',
        logGroupName = log_group,
        orderBy      = 'LastEventTime',
        descending   = True,
        limit        = 20)
    b = ['../']
    for i in s['logStreams']:
        c = i['logStreamName'] + '\t' +  str(func.utime_to_date(i['lastEventTimestamp']))
        b.append(c)
    return b

def get_events(group, stream):

    c = log_c.get_log_events(
        logGroupName = group,
        logStreamName = stream.split('\t')[0],
        limit = 20)
    b = ''
    for i in c['events']:
        b += i['message']
    return b

if __name__ == '__main__':
    lg = list_loggroups()

    while True:
        ho = open_inquirer(lg)
        if ho == '../':
            break
        while True:
            hu = open_inquirer(list_streams(ho))

            if hu != '../':
                pydoc.pager(get_events(ho, hu))
            elif hu == '../':
                break
