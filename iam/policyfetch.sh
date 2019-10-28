CMDNAME=`basename $0`
COUNT=0

function usage ()
{
    echo "Usage :  $0 [options] [--]

    Options:
    -p    Input AWS profile
    -t    Select policy type. "
} 

while getopts ":p:t:" OPT
do
  case $OPT in
    "p" ) VALUE_P="$OPTARG" ; ((COUNT++));;
    "t" ) VALUE_T="$OPTARG" ; ((COUNT++));;
    :|\?) usage ; exit 2 ;
  esac
done

case $COUNT in
    2) 
    echo $COUNT;
    echo $VALUE_T;
    echo $VALUE_P;;
    :|\?)
    usage ;
esac

#if [ $# -ne 1 ]; then
#    echo "指定された引数は$#個です。" 1>&2
#    echo "実行するには3個の引数が必要です。" 1>&2
#    f_usage
#    exit 1
#fi

