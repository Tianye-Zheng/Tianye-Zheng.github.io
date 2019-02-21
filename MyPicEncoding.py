#!usr/bin/python
# this script is use for generating base64 code of a picture which to be embedded in a post

import base64
import sys

if len(sys.argv) < 2:
    print("\nPlease input at least one picture path.\n")
else:
    for i in range(1, len(sys.argv)):
        f = open(sys.argv[i],'rb')
        ls_f = base64.b64encode(f.read())
        f.close()
        print(sys.argv[i] + ",the base64 code of it is: "+ ls_f + '\n')