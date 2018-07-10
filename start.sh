#! /bin/bash

DIR=$(pushd $(dirname $BASH_SOURCE{0}) > /dev/null && pwd  && popd > /dev/null)

export SERIAL_1=${SERIAL_1:-067125a40acc819e}
export SERIAL_2=${SERIAL_2:-09434d61255da52f}


#filter apps whose ActivityCount less than 5.
for apk in $(ls ${DIR}/apks)
do
    COUNT=$(bash ${DIR}/countActivity.sh ${DIR}/apks/${apk})
    echo ${apk}, ${COUNT}
    if [ ${COUNT} -lt 5 ]
    then
        rm ${DIR}/apks/${apk}
    fi
done


# update packages.txt
python ${DIR}/update_packages.py


bash ${DIR}/crash-detection.sh ${SERIAL_1} packages1.txt &
bash ${DIR}/crash-detection.sh ${SERIAL_2} packages2.txt &
wait

#clear urls
rm -f ${DIR}/urls/*

#clear apks
rm -f ${DIR}/apks/*