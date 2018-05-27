import re

def is_valid_email(addr):
    if re.match(r"(\w+|\w+.\w+)@(\w+.com)",addr):
        return True
    else:
        return False

n=re.compile(r"<([a-zA-z0-9\s]+)>[a-zA-Z0-9\s]*@[a-z]+.[a-z]{3}")

def get_name(addr):
    f=re.match(n,addr)
    if f:
        return f.group(1)
    else:
        return None
print(is_valid_email('someone@gmail.com'))
print(is_valid_email('bill.gates@microsoft.com'))

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')