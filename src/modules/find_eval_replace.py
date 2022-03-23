# -*- coding: utf-8 -*-

import re
import sys
from io import StringIO

OPEN_TAG = "{{eval"
CLOSE_TAG = "}}"

regexp = re.compile(OPEN_TAG + "\n(?P<code>(.|\n)*?)\n" +
                    CLOSE_TAG, re.MULTILINE)


def find_eval_replace(src: str) -> str:
    dst = ""
    last_match = 0
    for match in regexp.finditer(src):
        code = match.group("code")
        cc = compile(code, "<string>", "single")

        bak_stdout = sys.stdout
        sys.stdout = my_stdout = StringIO()

        eval(cc)

        sys.stdout = bak_stdout
        output = my_stdout.getvalue()

        if last_match == 0:
            dst += src[:match.start()]
        else:
            dst += src[last_match:match.start()]

        dst += output
        last_match = match.end()

    dst += src[last_match:]
    return dst
