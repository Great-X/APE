#! /usr/bin/python2.7

import os
import re

DIR = os.path.abspath(os.path.dirname(__file__))
APK_DIR = os.path.join(DIR, 'apks/')
PKGS_FILE_1 = os.path.join(DIR, 'packages1.txt')
PKGS_FILE_2 = os.path.join(DIR, 'packages2.txt')


def update_packages_txt():
    print("update packages.txt")
    pkgs = []
    for root, dirs, files in os.walk(APK_DIR):
        for file in files:
            pkg = re.findall(r"(.*?)\.apk", file)
            pkgs.extend(pkg)

    mid = len(pkgs) / 2
    with open(PKGS_FILE_1, 'w') as f:
        f.writelines('\n'.join(pkgs[:mid]))
    with open(PKGS_FILE_2, 'w') as f:
        f.writelines('\n'.join(pkgs[mid:]))


if __name__ == '__main__':
    update_packages_txt()