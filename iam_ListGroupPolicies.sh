#!/bin/sh
PROFILE=hoge

groups=`aws iam --profile $PROFILE list-groups | jq -r  '.Groups[].GroupName'`
array_groups=(`echo $groups`)

for group in ${array_groups[@]}; do
    group_policies=`aws iam --profile $PROFILE list-group-policies --group-name $group | jq -c -r '.PolicyNames' | sed -e "s/\"//g" -e "s/\[//g" -e "s/\]//g" -e "s/\,/\ /g"`
    array_group_policies=(`echo $group_policies`)
            
    for policy in ${array_group_policies[@]}; do
        policy_json=`aws iam --profile $PROFILE get-group-policy --group-name $group --policy-name $policy`
        echo $group"#"$policy"#"$policy_json
    done
done
