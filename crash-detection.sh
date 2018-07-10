#! /bin/bash

DIR=$(pushd $(dirname $BASH_SOURCE{0}) > /dev/null && pwd  && popd > /dev/null)

export SERIAL=$1
export TESTING_TIME=60

filename=$2
TOOL=sata

for PKG in $(cat ${DIR}/${filename})
do
    echo "Testing $PKG for tool $TOOL"
    if [[ -f ${DIR}/all_logs/${TOOL}-${PKG}.log ]]
    then
        echo "Package $PKG has been tested."
        continue
    fi
    if [[ ! -f ${DIR}/apks/${PKG}.apk ]]
    then
        echo "Package $PKG has been removed."
        continue
    fi
    grep $PKG ${DIR}/tested.txt
    if [[ $? == 0 ]]
    then
        echo "Package $PKG has been tested."
        continue
    fi
    echo "bash ${DIR}/run-${TOOL}.sh $PKG"
    bash ${DIR}/run-${TOOL}.sh $PKG
    echo $PKG >> ${DIR}/tested.txt
done