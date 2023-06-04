#!/usr/bin/env python3

with open('ADE20K.tsv', 'r') as f:
    data = f.read()

header = """GIMP Palette
Name: ADE20K
Columns: 8
# https://github.com/Vesnica/ADE20K
"""

data_cn = ""
data_en = ""

for line in data.split('\n')[1:]:
    fields = line.strip().split('\t')
    R = int(fields[6][1:3], 16)
    G = int(fields[6][3:5], 16)
    B = int(fields[6][5:7], 16)
    name_en = fields[8]
    name_cn = fields[9]
    data_cn += f"{R:>3} {G:>3} {B:>3} {name_cn}\n"
    data_en += f"{R:>3} {G:>3} {B:>3} {name_en}\n"

with open('ade20k_cn.gpl', 'w') as f:
    f.write(header + data_cn)

with open('ade20k_en.gpl', 'w') as f:
    f.write(header + data_en)
