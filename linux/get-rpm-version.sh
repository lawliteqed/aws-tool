#!/usr/bin/bash

#HEADER="パッケージ名,バージョン,リリース番号,アーキテクチャ,更新日,インストール日"
HEADER="Package,Version,Release,Arch,Change,Install"
FORMAT="%{NAME},%{version},%{release},%{arch},%{changelogtime},%{installtime}\n"
AWK_OPTION='{gsub($5,strftime("%Y-%m-%d",$5));gsub($6,strftime("%Y-%m-%d",$6));print}'

echo ${HEADER}
rpm -qa --queryformat ${FORMAT} |  awk -F',' ${AWK_OPTION} | sed "s/(1970-01-01)/-/g" | sort
