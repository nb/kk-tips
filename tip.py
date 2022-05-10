#!/usr/bin/env python3
import json
import random

tips = json.load(open('tips.json'))
for tip in random.choices(tips, k=3):
    print('%s\n\t– #%d, %d' % (tip['text'], tip['i'], tip['year']))