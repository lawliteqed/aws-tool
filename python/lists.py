import boto3
import pprint


def tags_value(lis, key_name):
    for i in lis:
        if i['Key'] == key_name:
            return i['Value']
    return None

def sgs():
    s = {}
    n = 1
    for i in boto3.resource('ec2').security_groups.all():
        s[n] = [
            i.group_name, i.id]
        n += 1
    return s

def insts():
    i = {}
    n = 1
    for j in boto3.resource('ec2').instances.all():
        i[n] = [
            tags_value(j.tags, 'Name'),
            j.id,
            j.private_ip_address
        ]
        n += 1
    return i

if __name__ == '__main__':
    pprint.pprint(sgs())
    pprint.pprint(insts())

    # a = [{'Key': 'System', 'Value': 'common'}, {'Key': 'Name', 'Value': 'amalin2'}, {'Key': 'StartStop', 'Value': 'true'}]
