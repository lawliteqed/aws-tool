# faho

## hgoaghoa


```
# res = ce.get_dimension_values(
#         TimePeriod={
#         'Start': '2019-08-01',
#         'End': '2019-08-31'
#         },
#         Dimension='SERVICE'
#     )
#
# print(res)
    
#get_dimension_values
a = {'DimensionValues': [{'Value': 'AWS Key Management Service', 'Attributes': {}}, {'Value': 'AWS Lambda', 'Attributes': {}}, {'Value': 'EC2 - Other', 'Attributes': {}}, {'Value': 'Amazon Elastic Compute Cloud - Compute', 'Attributes': {}}, {'Value': 'Amazon Simple Notification Service', 'Attributes': {}}, {'Value': 'Amazon Simple Storage Service', 'Attributes': {}}, {'Value': 'AmazonCloudWatch', 'Attributes': {}}, {'Value': 'Tax', 'Attributes': {}}], 'ReturnSize': 8, 'TotalSize': 8, 'ResponseMetadata': {'RequestId': '8ed5b3e6-27db-444c-b110-efd0a28fdda8', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '8ed5b3e6-27db-444c-b110-efd0a28fdda8', 'content-type': 'application/x-amz-json-1.1', 'content-length': '449', 'date': 'Sun, 01 Sep 2019 05:09:33 GMT'}, 'RetryAttempts': 0}}

# cost_res = {'ResultsByTime': [{'TimePeriod': {'Start': '2019-08-01', 'End': '2019-08-31'}, 'Total': {'BlendedCost': {'Amount': '0.690860204', 'Unit': 'USD'}}, 'Groups': [], 'Estimated': True}], 'ResponseMetadata': {'RequestId': '31cda9c5-db26-4c37-bfca-f01bab86c967', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '31cda9c5-db26-4c37-bfca-f01bab86c967', 'content-type': 'application/x-amz-json-1.1', 'content-length': '167', 'date': 'Sun, 01 Sep 2019 05:38:32 GMT'}, 'RetryAttempts': 0}}
#print( cost_res['ResultsByTime'][0]['Total']['BlendedCost']['Amount'])
```


## ディレクトリ構造


```
s3://bucket/foler/
├── 201907_cct.csv
├── 201907_other.csv
├── 201908_cct.csv
├── 201908_other.csv
├── other.csv
└── 
```
