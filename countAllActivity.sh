#! /bin/bash

DIR=$(pushd $(dirname $BASH_SOURCE{0}) > /dev/null && pwd  && popd > /dev/null)


for PKG in $(cat ${DIR}/packages.txt)
do
    COUNT=$(bash ${DIR}/countActivity.sh ${DIR}/apks/${PKG}.apk)
    printf "$COUNT\t$PKG\n"
done

