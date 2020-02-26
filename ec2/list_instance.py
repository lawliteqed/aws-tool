#!/home/ec2-user/.pyenv/shims/python
import sys
import boto3
import pandas as pd
import logging
logging.basicConfig(level=logging.INFO)
ec2_r = boto3.resource('ec2')

def get_val(tag, key):
    for i in tag:
        if i['Key'] == key:
            return i['Value']

def conv_df(list_2d, header):
    return pd.DataFrame(list_2d,columns=header)
    
def list_ec2():
    i2d = []
    for i in ec2_r.instances.all():
        inst = [
            i.private_ip_address,
            i.instance_id,
            i.instance_type,
            i.state['Name'],
            get_val(i.tags, 'Name')
        ]
        i2d.append(inst)

    header = [
        'ip',
        'id',
        'type',
        'status',
        'name'
    ]
    return conv_df(i2d, header)

def filter_tag(name, val):
    inst_resources = ec2_r.instances.filter(
        Filters=[
            {
                'Name':   'tag:'+ str(name),
                'Values': [val]
            }
        ])
    return inst_resources

def stop_instance(inst_resources):
    for i in inst_resources:
        i.stop()
        logging.info(i.instance_id + " is stopped")
    
def start_instance(inst_resources):
    for i in inst_resources:
        i.start()
        logging.info(i.instance_id + " is starting")
    


if __name__ == '__main__':
    print(list_ec2())

    # stop_instance(
    #     filter_tag('Name', 'doc_gitlab')
    #         )
