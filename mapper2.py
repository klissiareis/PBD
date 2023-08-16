# -*- coding: utf-8 -*-

import sys
import re

for line in sys.stdin:
    line = line.strip()
    words=line.split()

    for word in words:
      if re.match(r"^[A-Za-z]+$", word):
        print('%s\t%s' % (word, 1))
