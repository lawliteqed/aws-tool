import boto3

ec2_r = boto3.resource('ec2')
ec2_c = boto3.client('ec2')

class Instance(object):
    def __init__(self):
        pass

    def start(instance_id):
        ec2_c.start_instances(
            InstanceIds=[instance_id],
            DryRun=False
            )

    def stop(instance_id):
        ec2_c.stop_instances(
            InstanceIds=[instance_id],
            DryRun=False
            )
    
def tag_value(tag_key, tag_list):
    for i in tag_list:
        if i['Key'] == tag_key:
            return i['Value']


if __name__ == '__main__':
    instances = []
    for i in ec2_r.instances.all():
        if tag_value('StartStop', i.tags) == "true":
            instances.append(i.instance_id)
    
    for j in instances:
        Instance.stop(j)
