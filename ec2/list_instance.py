#!/home/ec2-user/.pyenv/shims/python
import sys
import boto3
import logging
import uuid
logging.basicConfig(level=logging.INFO)

ec2_r = boto3.resource('ec2')

def get_val(tag, key):
    for i in tag:
        if i['Key'] == key:
            return i['Value']


if __name__ == '__main__':

    a = ec2_r.instances

    instances = {}
    n = 1
    for i in a.all():
        d = {}
        d['system_tag']    = get_val(i.tags, 'System')
        d['image_id']      = i.image_id
        d['instance_id']   = i.instance_id
        d['instance_type'] = i.instance_type
        instances[str(n)] = d
        n += 1


    print(instances)


    # tag = [{'Key': 'System', 'Value': 'common'}, {'Key': 'Name', 'Value': 'amalin2'}, {'Key': 'StartStop', 'Value': 'true'}]
    # print(get_val(tag, 'System'))
