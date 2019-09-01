#last month cost output csv for s3
#arg servename:service_dict 
import csv

def service_cost(service):
    import boto3
    ce = boto3.client('ce')
    res = ce.get_cost_and_usage(
            TimePeriod={
                'Start': '2019-08-01', 'End': '2019-08-31'
            },
            Granularity='MONTHLY',
            Filter={
                'Dimensions': {
                    'Key': 'SERVICE',
                    'Values': [ service ]
                }
            },
            Metrics=[ 'BlendedCost' ]
        )
    return res['ResultsByTime'][0]['Total']['BlendedCost']['Amount']

def out_csv(array, out_file):
    with open(out_file, 'w') as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(array)

if __name__ == '__main__':
    s_list = {
        "common": [ 'AWS Key Management Service', 'Amazon Elastic Compute Cloud - Compute', 'Tax', 'EC2 - Other' ],
        "tax": [  'Tax' ]
    }

    for k, v in s_list.items():
        #row_header
        service = ['Services']
        cost = ['Cost']

        #create each line
        for i in v:
            service.append(i)
            cost.append(service_cost(i))

        filename = '201908_' + k + '.csv'
        out_csv([service, cost], filename)
