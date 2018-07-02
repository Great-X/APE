#! /bin/bash

DIR=$(pushd $(dirname $BASH_SOURCE{0}) > /dev/null && pwd  && popd > /dev/null)

#export SERIAL=${SERIAL:-067125a40acc819e}
export SERIAL=${SERIAL:-09434d61255da52f}

export TESTING_TIME=60

TOOL=sata

for PKG in $(cat ${DIR}/packages.txt)
do
    echo "Testing $PKG for tool $TOOL"
    if [[ -f ${DIR}/logs/${TOOL}-${PKG}.log ]]
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