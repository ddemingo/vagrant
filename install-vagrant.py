#!/usr/bin/env python3

import os
import pathlib
import stat
import urllib.request


home = str(pathlib.Path.home())
bin = f'{home}/.local/bin'

def path():
    path = os.environ['PATH']
    if not bin in path:
        print("""
Add $HOME/.local/bin to your $PATH:

    echo 'export PATH=\"$HOME/.local/bin:$PATH\"' >> $HOME/.bashrc
    source $HOME/.bashrc
""")

def make_executable(file):
    st = os.stat(file)
    os.chmod(file, st.st_mode | stat.S_IEXEC)


def download(file):
    path = f'{bin}/{file}'
    if not os.path.exists(path):
        print(f"Add {file} to {bin}")
        url = f'https://github.com/lamerce/vagrant/raw/main/bin/{file}'
        # https://stackoverflow.com/questions/22676/how-to-download-a-file-over-http
        urllib.request.urlretrieve(url, path)
        make_executable(path)

if not os.path.exists(bin):
    os.makedirs(bin)
    print(f"Make dir {bin}")

download('curl')
download('bsdtar')
download('vagrant')

path()
