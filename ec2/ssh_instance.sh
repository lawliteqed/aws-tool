#!/usr/bin/bash
ARGUMENT=1
NAMETAG=$1

KEY='~/.ssh/sakai-key.cer'
PORT=22
USER='ec2-user'

function usage() {
  echo "usage : $0 <instance-name>"
}

if [ $# -ne $ARGUMENT ]; then
  usage
  exit 2
else
  DNS=`aws ec2 describe-instances \
    --filter Name=tag:Name,Values=${NAMETAG} \
    --query 'Reservations[].Instances[].PublicDnsName' | jq -r '.[]'`
  ssh -i ${KEY} -p ${PORT}  -l ${USER} ${DNS}
  exit 0
fi
