import boto3
import yaml
ec2_r = boto3.resource('ec2')

YAML_FILE = "test.yaml"

def read_yaml(_read_file):
    f = open(_read_file, 'r')
    _read_data = yaml.load(f)
    f.close()
    return _read_data

def create_instances(_dict_yaml):
    _imageid = _dict_yaml['ImageId']
    _instance_type = _dict_yaml['InstanceType']
    _security_group = _dict_yaml['SecurityGroupIds']
    _subnet = _dict_yaml['SubnetId']
    
    print(_imageid , _instance_type, _security_group, _subnet)
    
    ec2_r.create_instances(
        MaxCount=1,
        MinCount=1,
        ImageId= _imageid,
        InstanceType= _instance_type,
        SecurityGroupIds=[
            _security_group
        ],
        SubnetId=_subnet,
        DryRun=True,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags':[
                    {
                        'Key': 'Name',
                        'Value': 'test'
                    }
                ]
            }
        ]
    )

create_instances(read_yaml(YAML_FILE))
