#!/usr/bin/python3

import os
import subprocess


all_off = '\033[0m'

dk_black_fg = '\033[30m'
dk_red_fg = '\033[31m'
dk_green_fg = '\033[32m'
dk_yellow_fg = '\033[33m'
dk_blue_fg = '\033[34m'
dk_magenta_fg = '\033[35m'
dk_cyan_fg = '\033[36m'
dk_white_fg = '\033[37m'

lt_black_fg = '\033[90m'
lt_red_fg = '\033[91m'
lt_green_fg = '\033[92m'
lt_yellow_fg = '\033[93m'
lt_blue_fg = '\033[94m'
lt_magenta_fg = '\033[95m'
lt_cyan_fg = '\033[96m'
lt_white_fg = '\033[97m'

def doShellCommand(cmd):
    print (f"{lt_black_fg}{cmd}{all_off}")
    return subprocess.run(cmd, shell=True, check=True).returncode


if __name__ == "__main__":
    if os.path.exists('./clib'):
        doShellCommand("cd clib && git pull")
    else:
        doShellCommand("git clone https://github.com/spacemeat/humon ./clib; cd clib")
    
    # NEXT: git checkout versionnumber
    doShellCommand("cd ..")
    doShellCommand("python3 ./setup.py build_ext --inplace")
