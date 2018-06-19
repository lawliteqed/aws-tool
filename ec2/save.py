# coding: utf-8
ec2_r
get_ipython().magic('pinfo ec2_c.describe_instances')
ec2_c.describe_instances()
res = ec2_c.describe_instances()
res
res["Reservations"][0]["Instances"][0]['InstanceId']
res["Reservations"][0]["Instances"][1]['InstanceId']
res["Reservations"][1]["Instances"][0]['InstanceId']
res["Reservations"]?
type(res["Reservations"]?)
type(res["Reservations"])
list_res = res["Reservations"]
for i in list_res:
    a = i["Instances"][0]['InstanceId']
    print(a)
    
get_ipython().magic('save save.py 1-14')
