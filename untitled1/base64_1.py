# -- coding: utf-8 --

import base64

def safe_base64_decode(s):
    x1 = len(s)
    x2 = x1 % 4

    if x2==0:
        y1 = base64.urlsafe_b64decode(s)
        return y1
    elif x2==1:
        s1 = s + b'==='
        y1 = base64.urlsafe_b64decode(s1)
        return y1
    elif x2==2:
        s2 = s + b'=='
        y1 = base64.urlsafe_b64decode(s2)
        return y1
    else:
        s3 = s + b'='
        y1 = base64.urlsafe_b64decode(s3)
        return y1


assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print(safe_base64_decode(b'YWJjZA=='))
print('ok')