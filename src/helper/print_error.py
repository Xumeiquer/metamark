# -*- coding: utf-8 -*-

import sys


def print_error():
    """
    print_error validate the command line to be complin with the MetaMark argument
    specification.

    If an error is found this function writes the error in the stderr and exits.
    """
    err = False
    if len(sys.argv) < 2:
        sys.stderr.write("Need markdown source document")
        err = True

    if err:
        sys.exit(1)
