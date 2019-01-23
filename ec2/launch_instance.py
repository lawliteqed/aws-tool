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

def create_instances(r):
    ec2_r.create_instances(
        MaxCount=1,
        MinCount=1,
        DryRun=False,
        ImageId = r['ImageId'],
        KeyName = r['KeyName'],
#        SubnetId = r['SubnetId'],
        InstanceType = r['InstanceType'],
#        SecurityGroupIds = [r['SecurityGroupIds']],
        NetworkInterfaces = [
            {
                'DeviceIndex': 0,
                'NetworkInterfaceId': r['NetworkInterfaceId']
             #   'NetworkInterfaceId': 'eni-0cd6e6ab0fdfb41b8'
             #   'SubnetId': 'subnet-109fbf59'
            }
        ],
        TagSpecifications = [
            {
                'ResourceType': 'instance',
                'Tags':[
                    {'Key':'Name', 'Value':r['NameTag']}
                ]
            }
        ]
    )

a = read_yaml(YAML_FILE)
print(a)

create_instances(read_yaml(YAML_FILE))
