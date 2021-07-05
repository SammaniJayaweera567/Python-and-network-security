import hashlib,os,uuid
#print(hashlib.algorithms_available)

msg = "This is my second task".encode()


def hashText(text):
    """
        Basic hashing function for a text using random unique salt.  
    """
    salt = uuid.uuid4().hex
    return hashlib.blake2b(salt.encode() + text.encode()).hexdigest() + ':' + salt
    
def matchHashedText(hashedText, providedText):
    """
        Check for the text in the hashed text
    """
    _hashedText, salt = hashedText.split(':')
    return _hashedText == hashlib.blake2b(salt.encode() + providedText.encode()).hexdigest()
print("BLAKE2c:", hashlib.blake2b(msg).hexdigest())






def hashText(text):
    """
        Basic hashing function for a text using random unique salt.  
    """
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + text.encode()).hexdigest() + ':' + salt
    
def matchHashedText(hashedText, providedText):
    """
        Check for the text in the hashed text
    """
    _hashedText, salt = hashedText.split(':')
    return _hashedText == hashlib.sha256(salt.encode() + providedText.encode()).hexdigest()
print("SHA-3-256:", hashlib.sha3_256(msg).hexdigest())



def hashText(text):
    """
        Basic hashing function for a text using random unique salt.  
    """
    salt = uuid.uuid4().hex
    return hashlib.sha512(salt.encode() + text.encode()).hexdigest() + ':' + salt
    
def matchHashedText(hashedText, providedText):
    """
        Check for the text in the hashed text
    """
    _hashedText, salt = hashedText.split(':')
    return _hashedText == hashlib.sha512(salt.encode() + providedText.encode()).hexdigest()

print("SHA-3-512:", hashlib.sha3_512(msg).hexdigest())