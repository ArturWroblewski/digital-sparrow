import random
import string

def randStr(chars = string.ascii_uppercase + string.digits, N=10):
	return ''.join(random.choice(chars) for _ in range(N))

# default length(=10) random string
print(randStr())
# random string of length 7
print(randStr(N=7))
# random string with characters picked from ascii_lowercase
print(randStr(chars=string.ascii_lowercase))
# random string with characters picked from 'abcdef123456'
print(randStr(chars='abcdef123456'))
# random string of length 7
print(randStr(N=25))
print(randStr(N=25))
print(randStr(N=25))

s='355879ACB6'

print(s[:4] + '-' + s[4:])

hash = '355879ACB6'
hashlist = list(hash)
hashlist.insert(4, '-')
example = ''.join(hashlist)
print(example)

hash = randStr(N=25)
hashlist = list(hash)
hashlist.insert(20, '-')
hashlist.insert(15, '-')
hashlist.insert(10, '-')
hashlist.insert(5, '-')
example = ''.join(hashlist)
print(example)

hash = randStr(N=15)
hashlist = list(hash)
hashlist.insert(10, '-')
hashlist.insert(5, '-')
example = ''.join(hashlist)
print(example)
print(36**25)
print(36**15)
print(36**5)

print(b'91234567890123456781'.hex())
# 3931323334353637383930313233343536373831
# 3f 3e57de22361042772a3f18f42f05c9afc2cf25
# 8,011,739,643
# Assuming combinations like AAAA or 9999 are possible, then, since there are 26 letters and 10 digits, there are 36^4 possible combinations. That's 1,679,616 possible combinations.
# or 15 characters, letters or digits, there are 36^15 different combinations which is about 10^23. I don't know the number of valid and unused keys exactly,
# BMDPA-9G8FD-SSG85. B5A23-AK39A-28F53

# rstring.ascii_letters
# rstring.ascii_lowercase
# rstring.ascii_uppercase
# rstring.digits
# rstring.hexdigits
# rstring.letters
# rstring.lowercase
# rstring.octdigits
# rstring.punctuation
# rstring.printable
# rstring.uppercase
# rstring.whitespace