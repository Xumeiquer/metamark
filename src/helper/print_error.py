# -*- coding: utf-8 -*-

import sys


def print_error():
    err = False
    if len(sys.argv) < 2:
        sys.stderr.write("Need markdown source document")
        err = True

    if err:
        sys.exit(1)
