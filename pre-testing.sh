#! /bin/bash

DIR=$(pushd $(dirname $BASH_SOURCE{0}) > /dev/null && pwd  && popd > /dev/null)

echo "Install package at first"
adb -s $SERIAL install -g -r ${DIR}/apks/${PKG}.apk > /dev/null