#!/bin/sh
PROFILE=default

groups=(`aws iam --profile $PROFILE list-groups | jq -r '.Groups[].GroupName'`)

echo ${#groups[*]}

for group in ${groups[@]}; do
    group_policies=(`aws iam --profile $PROFILE list-group-policies --group-name $group | jq -c -r '.PolicyNames' | sed -e "s/\"//g" -e "s/\[//g" -e "s/\]//g" -e "s/\,/\ /g"`)

    for policy in ${group_policies[@]}; do
        policy_json=`aws iam --profile $PROFILE get-group-policy --group-name $group --policy-name $policy`
        echo $group"#"$policy"#"$policy_json
    done
done

#aws_function LIST_G
#
#for group in ${groups[@]}; do
#    aws_function LIST_P $group
#
#    for policy in ${group_policies[@]}; do
#        aws_function GET_P $group $policy
#    done
#done
