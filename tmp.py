# coding: utf-8
import dynamo.py
db_r
import dynamo.py
db_r
table = db_r.Table('sakai-vpc')
table
import dynamo.py
table.put_item(
    Item={
        "id":"subnet-33848329",
        "tag-name": "sakai-subnet",
        "creation-time": "2018091202"
    })
    
ec2_r.instances.all()
for i in ec2_r.instances.all():
    print(i)
    
get_ipython().magic('pinfo ec2_r.Instance')
ec2_r.Instance(i-064684cb95f2b91af')
ec2_r.Instance('i-064684cb95f2b91af')
i = ec2_r.Instance('i-064684cb95f2b91af')
i
get_ipython().magic('ll ')
i.subnet_id
i.tags
i
i.subnet_id
i
for i in ec2_r.instances.all():
    print(i.id)
    
for i in ec2_r.instances.all():
    print(i.subnet_id)
    
for i in ec2_r.instances.all():
    print(i.subnet_id)
    print(i.id)
    
for i in ec2_r.instances.all():
    d = {
        "subnet_id": i.subnet_id,
        "instance_id": i.id
        }
        
         

    
get_ipython().magic('pinfo ec2_r.Subnet')

ec2_r.Subnet('i.subnet_id')
a = ec2_r.Subnet('i.subnet_id')
a
a = ec2_r.Subnet(i.subnet_id)
a
a.tags
get_ipython().magic('history ')
for i in ec2_r.instances.all():
    print(i.id)
    print(i.tags)
    print(i.subnet_id)
    print(ec2_r.Subnet(i.subnet_id).tags)
    
for i in ec2_r.instances.all()]:
for i in ec2_r.instances.all():
    put_item = {
        'instance_id': i.id,
        'instance_name': i.tags,
        'subnet_id': i.subnet_id,
        'subnet_name': ec2_r.Subnet(i.subnet_id).tags
    }
    
put_item
get_ipython().magic('cat dynamo.py')
table = db_r.Table('sakai-vpc')
table.put_item(Item=put_item)
put_item
put_item['id'] = 'hoge'
put_item
table.put_item(Item=put_item)
get_ipython().magic('save tmp.py 1-53')
