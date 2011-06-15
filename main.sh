#!/usr/bin/env bash
#$1=lambda_1
#$2=lambda_2
#$3=lambda_3
#$4=epsilon_1
#$5=epsilon_2
#$6=epsilon_3
#IFS=` echo -en "\n\b"`

v=$(awk '{print $1, $2, $3, $4, $5, $6}' salida.out)
echo $v
./leshouches.sh $v
