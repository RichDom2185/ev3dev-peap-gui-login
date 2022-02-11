#!/usr/bin/env python
with open('/var/lib/connman/test.config', 'r') as f:
    with open('out.txt', 'w') as g:
        g.write(f.read())