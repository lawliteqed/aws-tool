ec2_r.instances
a =ec2_r.instances
for i in a.all():
    print(i)
    
for x in dir(i):
    print(x)
    
get_ipython().run_line_magic('history', '')
i.iam
i.id
i.tags
i.instance_type
get_ipython().run_line_magic('save', '-a 1-10 save.py')
