import inquirer
import sys
import boto3
import pydoc
import string
from inquirer import themes
from inquirer.render.console import ConsoleRender, List
from readchar import key

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
        elif pressed in ("j", "l"):
            pressed = key.DOWN
        elif pressed == "q":
            pressed = key.CTRL_C
        super().process_input(pressed)

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
        b.append(i['logStreamName'])
    return b

def open_inquirer(choice_list):
    inq_list = [
        inquirer.List(
            'list_huga',
            choices  = choice_list,
            carousel = True,
        )
    ]
    ans =  inquirer.prompt(
                inq_list,
                render = ExtendedConsoleRender())
    return ans['list_huga']

def get_events(group, stream):
    c = log_c.get_log_events(
        logGroupName = group,
        logStreamName = stream,
        limit = 20)
    b = ''
    for i in c['events']:
        b += i['message']
    return b

if __name__ == '__main__':
    ho = open_inquirer(list_loggroups())
    hu = open_inquirer(list_streams(ho))
    if hu == '../':
        ho = open_inquirer(list_loggroups())

    pydoc.pager(get_events(ho, hu))
