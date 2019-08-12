#!/bin/sh
PROFILE=default

users=`aws iam --profile $PROFILE list-users | jq -r '.Users[].UserName'`
array_users=(`echo $users`)

for user in ${array_users[@]}; do
    user_policies=`aws iam --profile $PROFILE list-user-policies --user-name $user | jq -c -r '.PolicyNames' | sed -e "s/\"//g" -e "s/\[//g" -e "s/\]//g" -e "s/\,/\ /g"`
    array_user_policies=(`echo $user_policies`)
            
    for policy in ${array_user_policies[@]}; do
        policy_json=`aws iam --profile $PROFILE get-user-policy --user-name $user --policy-name $policy`
        echo $user"#"$policy"#"$policy_json
    done
done
