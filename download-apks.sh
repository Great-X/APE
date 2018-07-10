#! /bin/bash

DIR=$(pushd $(dirname $BASH_SOURCE{0}) > /dev/null && pwd  && popd > /dev/null)

# download apk
for file in $(ls ${DIR}/urls)
do
    wget -P ${DIR}/apks $(cat ${DIR}/urls/${file}) &
done
wait