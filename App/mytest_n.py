
import base64
import hashlib
import os
import sys
import binascii
import random
from aes import *

def sha256(string_to_hash):
    a=hashlib.sha256(string_to_hash).hexdigest()
    t=hex_to_binary(a)
    return t
def perms(l):
     k=[]
     
     for i in range(0,len(l),4):
         k.append(l[i:i+4])
     #print len(k)
     a=k
     for i in range(len(k)):
         for j in range(len(k)):
             k[i],k[j]=k[j],k[i]
     up=""
     for i in k:
         up+="".join(i)
     s=""

     for i in range(len(l)):
         s+="*"
     s=list(s)
     res=""
     for i in range(0,len(s),2):
         s[i:i+2]=up[i:i+2]
         print ("".join(s))
     res+="".join(s)
     return res

def byte_to_binary(n):
    return ''.join(str((n & (1 << i)) and 1) for i in reversed(range(8)))

def hex_to_binary(h):
    return ''.join(byte_to_binary(ord(b)) for b in binascii.unhexlify(h)) 

def permrev(l):
     k=[]
     
     for i in range(0,len(l),4):
         k.append(l[i:i+4])
     a=k
     for i in range(len(k)-1,-1,-1):
         for j in range(len(k)-1,-1,-1):
             k[i],k[j]=k[j],k[i]
     up=""
     for i in k:
         up+="".join(i)
     s=""

     for i in range(len(l)):
         s+="*"
     s=list(s)
     res=""
     for i in range(len(s)):
         s[i]=up[i]
     res+="".join(s)
     return res



a="hello"

t=sha256(a)
print("sha256",t)


re=perms(t)
print ("permutation",re)

pre=permrev(re)
print(pre)

encrypted = encrypt(pre, t)
print ("Encrypted")
print (encrypted)
