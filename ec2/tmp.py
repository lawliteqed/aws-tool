# coding: utf-8
get_ipython().magic('ll ')
ec2
ec2.describe_instances
get_ipython().magic('pinfo ec2.describe_instances')
ec2.describe_instances()
cli_ec2 = boto3.client('ec2')
get_ipython().magic('pinfo cli_ec2.start_instances')
get_ipython().magic('pinfo cli_ec2')
r_ec2 = boto3.resource('ec2')
get_ipython().magic('pinfo r_ec2.create_instances')
get_ipython().magic('save tmp.py 8-10')
get_ipython().magic('save tmp.py 8-10')
get_ipython().magic('save tmp.py 8-12')
get_ipython().magic('save tmp.py 8-12')
get_ipython().magic('save tmp.py 1-12')
get_ipython().magic('save')
get_ipython().magic('pinfo %save')
get_ipython().magic('save -f tmp.py 1-17')
get_ipython().magic('save -f tmp.py 1-5')
