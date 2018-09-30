import boto3
import yaml

ec2_c = boto3.client('ec2')

InstanceId = 'i-064684cb95f2b91af'
CREATE_IMAGE_YAML = "image.yml"

def read_yaml(read_file):
    f = open(read_file, 'r')
    read_data = yaml.load(f)
    f.close()
    return read_data

def create_image(r):
    ec2_c.create_image(
          Description='string',
          DryRun=False,
          InstanceId='kkk',
          Name='string',
          NoReboot=True
      )


a = read_yaml(CREATE_IMAGE_YAML)
print(a)
