

import re
import string
from typing import NoReturn

table = str.maketrans({key: ' ' for key in string.punctuation})

splitter_re = re.compile(r"\w+|[^\w\s]")

def splitter(text):
    return splitter_re.findall(text)

def tr_lower(txt):
    return txt.replace('İ','i').replace('I','ı').lower()

def tr_upper(txt):
    return txt.replace('i','İ').replace('ı','I').upper()

def remove_punc(text):
    s = text.translate(table).strip()
    s.replace('"',' ')
    s.replace('\n',' ')
    s.replace('\t',' ')
    while '  ' in s:
        s = s.replace('  ',' ')
    return s