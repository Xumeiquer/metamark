#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from helper import print_error
from modules import find_eval_replace


def main():
    print_error()

    with open(sys.argv[1], "r") as msrc:
        mdst = find_eval_replace(msrc.read())
        print(mdst)


if __name__ == "__main__":
    main()
