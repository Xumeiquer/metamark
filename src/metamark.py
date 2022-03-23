#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MetaMark is a pre-processor for markdown documents. It executes (evaluate) python
code from the Markdown document and generates an output in which the code gets
replaced by the python sniped output.

This is a really simple pre-processor it does not validate pretty much anything.
Use it at your own risk.
"""
import sys
from helper import print_error
from modules import find_eval_replace


def main():
    """
    MetaMark entrypoint it evaluates the input and produces the output.
    """
    print_error()

    with open(sys.argv[1], "r") as msrc:
        mdst = find_eval_replace(msrc.read())
        sys.stdout.write(mdst)


if __name__ == "__main__":
    main()
