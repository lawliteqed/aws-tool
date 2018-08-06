#!/home/ec2-user/.pyenv/shims/python
import yaml
import boto3

ec2_r = boto3.resource('ec2')
YAML_FILE = "test.yaml"

def read_yaml(read_file):
    f = open(read_file, 'r')
    read_data = yaml.load(f)
    f.close()
    return read_data

def create_instances(dict_yaml):
    ec2_r.create_instances(
        MaxCount=1,
        MinCount=1,
        DryRun=False,
        ImageId = dict_yaml['ImageId'],
        KeyName = dict_yaml['KeyName'],
        SubnetId = dict_yaml['SubnetId'],
        InstanceType = dict_yaml['InstanceType'],
        SecurityGroupIds = [ dict_yaml['SecurityGroupIds'] ],
        TagSpecifications = [
            {
                'ResourceType': 'instance',
                'Tags':[
                    {'Key':'Name', 'Value':dict_yaml['NameTag']}
                ]
            }
        ]
    )


create_instances(read_yaml(YAML_FILE))
