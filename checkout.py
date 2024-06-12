# for CI only
import time
import os

raw_date = time.localtime()
y, m, d = raw_date.tm_year, raw_date.tm_mon, raw_date.tm_mday
date = f"{y}.{m}.{d}"

if len(sys.argv) > 1:
    if sys.argv[1] != 'test':
        os.system(f'mv ./{sys.argv[1]/*} ./output/')
else:
    os.system(f'mv ./{date}/* ./output/')