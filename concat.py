from template_lib import *
import datetime
import time
import os
import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')

index = ["活动预告", "参考消息"]
regp = [["活动预告", "\\section{编辑部招聘人才}\n编辑部招聘人才，用爱发电，工作轻松，详情可联系QQ：1329527951 客服小祥\\\\想订阅本消息，可加QQ群：962626571.\n"]]
rega = []
trans_dict = {"@@@@": "{", "^^^^": "}", "\\url": "\\sloppy\\url"}

raw_date = time.localtime()
y, m, d = raw_date.tm_year, raw_date.tm_mon, raw_date.tm_mday
date = f"{y}.{m}.{d}"
baseline = datetime.datetime(2024, 5, 23)
today = datetime.datetime(y, m, d)

interval = (today - baseline).days

def trans(s, dic):
    for k, v in dic.items():
        s = s.replace(k, v)
    return s

def parse_sec(file_name, pattern=partmp, dict=trans_dict):
    with open(file_name) as f:
        part_name = f.readline()[:-1]
        sec_name = f.readline()[:-1]
        sec_raw = trans(f.read(), dict).replace("\n", "\\\\")
    if part_name not in index+['0', '1']:
        index.append(part_name)
    sec_cont = trans(pattern.format(sec_name=sec_name, sec_cont=sec_raw), dict)
    match part_name:
        case '0': part_name = "活动预告"
        case '1': part_name = "参考消息"
    regp.append([part_name, sec_cont])

# dir handle
if len(sys.argv) > 1:
    if sys.argv[1] != 'test':
        os.chdir(f'./{sys.argv[1]}')
else:
    os.chdir(f'./{date}')
ls = os.listdir()
if 'saying' in ls:
    with open('saying') as f:
        saying = f.read()
saying = """“Sidera fines transibunt praescriptos.”\\\\\n“星辰终将凌越其分野。”"""

head = trans(headp.format(date=date, no=interval, saying=saying), trans_dict)

for i in ls:
    ext = i[-4:]
    if ext in [".txt", ".md"]:
        parse_sec(i)
    if ext in [".png", ".jpg", "jpeg", ".tif", "tiff", "gif"]:
        rega.append(i)

logging.info('Concat Completed!')

with open(f'南哪消息{date}.tex', 'wt') as tex:
    # head
    tex.write(head)
    # part
    for name in index:
        tex.write(trans(partbp.format(part_name=name), trans_dict))
        for sec in regp:
            if sec[0] == name:
                tex.write(sec[1])
        tex.write(parte)
    # appendix
    tex.write(appb)
    for name in rega:
        tex.write(trans(appm.format(with_ext=name, no_ext=name[:name.rfind('.')]), trans_dict))
    tex.write(appe)

logging.info('Tex Writing Completed!')

os.system(f"lualatex  -synctex=1 -interaction=nonstopmode -file-line-error -recorder  '南哪消息{date}.tex'")

logging.info('Compilation Completed!')
