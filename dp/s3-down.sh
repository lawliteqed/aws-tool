PROFILE=$1
S3_PATH=$2

function usage ()
{
   echo "usage:  $0 <profile> <s3path>"
}

function download ()
{
   aws --profile $PROFILE s3 cp $S3_PATH .
}

if [ $# -eq 2 ]; then
   download
   exit 0
else
   usage
   exit 2
fi
