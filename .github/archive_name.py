#!/usr/bin/python3

with open('./debian/brain-config/DEBIAN/control', 'r') as f:
    for l in f.readlines():
        if l.startswith('Version:'):
            print(f'brain-config_{l.replace("Version: ", "").rstrip()}_all.deb', end='')
            break
    else:
        raise RuntimeError('Version line was not found')
