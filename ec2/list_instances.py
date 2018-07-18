import boto3

ec2_c = boto3.client('ec2')
instances = ec2_c.describe_instances()

#for i in c:
#    print(i)
#    print("Name" in i.values())

list_instances = instances["Reservations"]
for i in list_instances:
    a = i["Instances"][0]['InstanceId']
    b = i["Instances"][0]['State']['Name']
    c = i["Instances"][0]['Tags']
    for j in c:
        if ("Name" in j.values()):
            value =j['Value']
            print(value)
    print(a)
    print(b)
    #print(c)
    #t = type(c)
    #print(t)
    

