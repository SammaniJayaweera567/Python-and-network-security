text = 'Hi...hello world'

import hashlib
m = hashlib.md5()
m.update(text.encode('utf-8'))
print(m.hexdigest())



text = 'Hi...My name is Sammani Jayaweera'

import hashlib
m = hashlib.md5()
m.update(text.encode('utf-8'))
print(m.hexdigest())

#One-Liner Trial 1
text = 'My age is 24 years old';import hashlib;m=hashlib.md5();m.update(text.encode('utf-8'));print(m.hexdigest())



