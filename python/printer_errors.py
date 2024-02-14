import re

s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzz"


def printer_error(s):
    s_len = len(s)
    print(s_len)
    errors = len(re.findall("[n-z]", s))
    return f"{errors}/{s_len}"


print(printer_error(s))
