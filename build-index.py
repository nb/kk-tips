#!/usr/bin/env python3
import re
index = open('index.html').read()
tips = open('tips.json').read()
replace = lambda m: m.group(1) + tips + m.group(2)
built = re.sub(r'(\/\* start tips\.json \*\/).*(\/\* end tips\.json \*\/)', replace, index, flags=re.M | re.S)
with open('index.html', 'w') as out:
    out.write(built)