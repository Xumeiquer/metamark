# -*- coding: utf-8 -*-

import re
import sys
from io import StringIO

OPEN_TAG = "{{eval"
CLOSE_TAG = "}}"

regexp = re.compile(OPEN_TAG + "\n(?P<code>(.|\n)*?)\n" +
                    CLOSE_TAG, re.MULTILINE)


def find_eval_replace(src: str) -> str:
    """
    find_eval_replace is the generic function to process the Markdown document
    looking for Python code enclosed between `{{eval` and `}}`, it also compiles
    and evaluates the code and finally replaces the Python code snippet by its
    output.
    """
    dst = ""
    last_match = 0

    for match in regexp.finditer(src):
        code = match.group("code")

        try:
            bak_stdout = sys.stdout
            sys.stdout = my_stdout = StringIO()

            cc = compile(code, "<string>", "exec")
            eval(cc)

            sys.stdout = bak_stdout
            output = my_stdout.getvalue()
        except Exception as err:
            sys.stderr.write("Compile error between lines " +
                             str(match.start()) + " and " + str(match.end()) + ": " + str(err))
            sys.exit(1)
        else:

            if last_match == 0:
                dst += src[:match.start()]
            else:
                dst += src[last_match:match.start()]

            dst += output
            last_match = match.end()

    dst += src[last_match:]
    return dst
