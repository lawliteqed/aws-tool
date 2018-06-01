import requests
import json



def get_my_instanceid():
    instance_info = requests.get('http://169.254.169.254/latest/dynamic/instance-identity/document/').text
    return type(instance_info)


print (get_my_instanceid())
