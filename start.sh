#! /bin/bash

DIR=$(pushd $(dirname $BASH_SOURCE{0}) > /dev/null && pwd  && popd > /dev/null)

# download apk
for file in $(ls ${DIR}/urls)
do
    wget -P ${DIR}/apks $(cat ${DIR}/urls/${file})
done

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


bash ${DIR}/crash-detection.sh