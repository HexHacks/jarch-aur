#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess as sp

def run(args, verbose=True):
    if isinstance(args, str):
        args = args.split(' ')

    # args should now be a list
    if verbose:
        print(' '.join(args))

    out = sp.check_output(args)
    if verbose and len(out) > 0:
        print(out)

    return out

def get_pkg_dirs(folder, recurse=True):
    files = os.listdir(folder)
    out = []
    for f in files:
        full = os.path.join(folder, f)

        if os.path.isdir(full):
            if 'PKGBUILD' in os.listdir(full):
                out.append(full)
            elif recurse:
                out = out + get_pkg_dirs(full)
    return out

run('git submodule update --recursive --remote')

pkgs = get_pkg_dirs(os.getcwd())
for p in pkgs:
    print('-'*5 + p)
    sp.run(['makepkg', '-si', '--needed'], cwd=p)
