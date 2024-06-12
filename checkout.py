# for CI only
import time
import os
import sys

raw_date = time.localtime()
y, m, d = raw_date.tm_year, raw_date.tm_mon, raw_date.tm_mday
date = f"{y}.{m}.{d}"

os.system('mkdir output')

if len(sys.argv) > 1:
    if sys.argv[1] != 'test':
        os.system(f'mv ./{sys.argv[1]}/*{date}.pdf ./output/')
        os.system(f'mv ./{sys.argv[1]}/*{date}.tex ./output/')
        os.system(f'mv ./{sys.argv[1]}/*{date}.log ./output/')
else:
    os.system(f'mv ./{date}/*.pdf ./output/')