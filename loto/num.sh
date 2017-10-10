max=43 
count=6 

function numgen()
{
array=()
sortarray=()
for i in `seq 1 $count`
do
    num=$(($RANDOM % $max))
    [ $num = 0 ] && array=($max "${array[@]}") || array=($num "${array[@]}") 
done 

sortarray=($(for v in "${array[@]}"; do echo "$v"; done | sort -n | uniq))
}


while [ ${#sortarray[@]} -ne $count ]
do
    numgen
done

echo "${sortarray[@]}"
