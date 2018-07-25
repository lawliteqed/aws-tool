#!/home/ec2-user/.pyenv/shims/python
import boto3
import yaml
ec2_r = boto3.resource('ec2')

YAML_FILE = "test.yaml"

def read_yaml(read_file):
    f = open(read_file, 'r')
    read_data = yaml.load(f)
    f.close()
    return read_data

def create_instances(dict_yaml):
    imageid = dict_yaml['ImageId']
    instance_type = dict_yaml['InstanceType']
    security_group = dict_yaml['SecurityGroupIds']
    subnet = dict_yaml['SubnetId']
    nametag = dict_yaml['NameTag']
    key_name = dict_yaml['KeyName']
    #print(_imageid , _instance_type, _security_group, _subnet)
    ec2_r.create_instances(
        MaxCount=1,
        MinCount=1,
        ImageId= imageid,
        KeyName= key_name,
        InstanceType= instance_type,
        SecurityGroupIds=[
            security_group
        ],
        SubnetId=subnet,
        DryRun=False,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags':[
                    {
                        'Key': 'Name',
                        'Value':nametag 
                    }
                ]
            }
        ]
    )


create_instances(read_yaml(YAML_FILE))
