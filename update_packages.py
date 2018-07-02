#! /usr/bin/python2.7

import os
import re

DIR = os.path.abspath(os.path.dirname(__file__))
APK_DIR = os.path.join(DIR, 'apks/')
PKGS_FILE = os.path.join(DIR, 'packages.txt')


def update_packages_txt():
    print("update packages.txt")
    pkgs = []
    for root, dirs, files in os.walk(APK_DIR):
        for file in files:
            pkg = re.findall(r"(.*?)\.apk", file)
            pkgs.extend(pkg)
    with open(PKGS_FILE, 'w') as f:
        f.writelines('\n'.join(pkgs))


if __name__ == '__main__':
    update_packages_txt()