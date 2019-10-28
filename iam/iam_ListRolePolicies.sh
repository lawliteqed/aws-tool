#!/bin/sh
PROFILE=hoge

roles=`aws iam --profile $PROFILE list-roles | jq -r '.Roles[].RoleName'`
array_roles=(`echo $roles`)

for role in ${array_roles[@]}; do
    role_policies=`aws iam --profile $PROFILE list-role-policies --role-name $role | jq -c -r '.PolicyNames' | sed -e "s/\"//g" -e "s/\[//g" -e "s/\]//g" -e "s/\,/\ /g"`
    array_role_policies=(`echo $role_policies`)
            
    for policy in ${array_role_policies[@]}; do
        policy_json=`aws iam --profile $PROFILE get-role-policy --role-name $role --policy-name $policy`
        echo $role"#"$policy"#"$policy_json
    done
done
