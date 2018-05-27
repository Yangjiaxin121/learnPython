import hashlib


db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(username,password):
    md5_pasword = hashlib.md5()
    md5_pasword.update(password.encode('utf-8'))
    hexPassword = md5_pasword.hexdigest()
    if hexPassword==db[username]:
        return True
    return False


print(login('michael', '123456'))
print(login('bob', 'abc999'))
print(login('alice', 'alice2008'))
print(login('michael', '1234567'))
print(login('bob', '123456'))
print(login('alice', 'Alice2008'))