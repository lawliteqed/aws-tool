PROFILE=$1
DP_NAME=$2
CONFIG_FILE=conf/$DP_NAME.conf
SAMPLE_FILE=sample/sample.json



#confファイル内のアイテム(AMI_ID,INSTANCE_TYPE, etc.)を変数化
CONFIG_ITEMS=(`cut -d";" -f1 $CONFIG_FILE`)
for i in ${CONFIG_ITEMS[@]}; do
    declare $i=`grep "$i" $CONFIG_FILE | cut -d";" -f2`
    eval echo '$'$i
done


#for i in ${CONFIG_ITEMS[@]}; do
#    declare $i=`grep "$i" $CONFIG_FILE | cut -d";" -f2`
#    eval echo '$'$i
#done

function usage ()
{
   echo "usage:  $0 <profile> <pipeline-name>"
}


if [ $# -eq 2 ]; then
   exit 0
else
    echo $AMI_ID
   exit 2
fi
