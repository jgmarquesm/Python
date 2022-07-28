from random import randint as ri
def private_key(p):
    privateKey = ri(1,p)
    return privateKey
def public_key(p, g, private):
    A = (g**private) % p
    return A
def secret(p, public, private):
    s = (public**private) % p
    return s
