# coding: utf-8
instances = ec2_c.describe_instances()


#イメージとしては
#no,instanceId,status(stop/start/terminated),tagsname,publicDNS,privateIP


#instanceId = a["Reservations"][0]["Instances"][0]['InstanceId']

list_instances = instances["Reservations"]
for i in list_instances:
    a = i["Instances"][0]['InstanceId']
    b = i["Instances"][0]['State']['Name']
    c = i["Instances"][0]['Tags']
    print(a)
    print(b)
    print(c)
    
c
import pandas
c
type(C)
type(c)
get_ipython().magic('ll ')
a =[1,6,9]
a
[i * 2 for i in a]
c
{k: v for k, v in c}
c
d = [x['Value'] for x in c if x['Key'] == 'Name']
d
get_ipython().magic('save save.py 1-17')
