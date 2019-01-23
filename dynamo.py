
# coding: utf-8
#put_item


table = db_r.Table('sakai-vpc')
table.put_item(
    Item={
        "id":"subnet-33848329",
        "tag-name": "sakai-subnet",
        "creation-time": "2018091202"
    })
    


