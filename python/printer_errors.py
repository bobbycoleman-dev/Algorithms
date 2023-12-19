import re

s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"


def printer_error(s):
    s_len = len(s)
    errors = len(re.findall("[n-z]", s))
    return f"{errors}/{s_len}"


print(printer_error(s))
