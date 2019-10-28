import pandas as pd
import boto3


class ResouceFrame:
    def get_dict_val(self, d_list, get_key, key, val):
        d = {}
        for d in d_list:
            if d[key]==val:
                return d[get_key]

    def id_alarm(self, itr):
        l = []
        for i in itr:
            inst_id = self.get_dict_val(i.dimensions, "Value", "Name", "InstanceId")
            l.append([inst_id, i.name])
        return pd.DataFrame(l, columns=['id', 'name'])

    def id_name(self, itr):
        l = []
        for i in itr:
            inst_name = self.get_dict_val(i.tags, "Value", "Key", "Name")
            l.append([i.instance_id, inst_name])
        return pd.DataFrame(l, columns=['id', 'alarm'])


if __name__ == '__main__':
    ec2_r = boto3.resource('ec2')
    cw_r = boto3.resource('cloudwatch')

    #df = ResouceFrame()
    #merged_df = pd.merge(
    #    df.id_name(ec2_r.instances.all()),
    #    df.id_alarm(cw_r.alarms.all()),
    #    on='id',
    #    how='left'
    #)
    ##merged_df = pd.merge(b, a, on='id', how='left')

    #merged_df.to_csv('/home/ec2-user/hoge.csv', index=None)
