#!/bin/sh
PROFILE=default


aws ec2 describe-instances | jq '.Reservations[].Instances[] | select (.Tags[].Value == "$1") | .InstanceId'

