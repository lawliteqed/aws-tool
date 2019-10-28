PROFILE=$1

function usage ()
{
    echo "usage:  $0 <profile>"
}

function main ()
{
    aws --profile $PROFILE ec2 describe-instances | jq -r '.Reservations[].Instances[].Tags[] | select(.Key == "Name") | .Value'
}

if [ $# -eq 1 ]; then
   main
   exit 0
else
   usage
   exit 2
fi
