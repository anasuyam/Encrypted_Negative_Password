import MySQLdb
import base64
import hashlib
import os
import sys
import binascii
import random
from itertools import permutations
import tkMessageBox
from aes import *
def allPermutations(s): 
       
     # Get all permutations of string '' 
     permList = permutations(s) 
     print list(permList)
     # print all permutations 
##     for perm in list(permList): 
##         print (''.join(perm)) 
def perms(l):
     k=[]
     
     for i in range(0,len(l),4):
         k.append(l[i:i+4])
     print len(k)
     a=k
     for i in range(len(k)):
         for j in range(len(k)):
             k[i],k[j]=k[j],k[i]
     print k
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
         #print "".join(s)
     res+="".join(s)
##     print res
     return res

def permret(l):
     k=[]
     
     for i in range(0,len(l),4):
         k.append(l[i:i+4])
    # k.reverse()
     print k
     print "permrev k\n\n",k
     a=k
     for i in range(len(k)-1,-1,-1):
         for j in range(len(k)-1,-1,-1):
             k[i],k[j]=k[j],k[i]
     #print k
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
         #print "".join(s)
     res+="".join(s)
     print "res\n need this as output\n",res
     return res
def byte_to_binary(n):
    return ''.join(str((n & (1 << i)) and 1) for i in reversed(range(8)))

def hex_to_binary(h):
    return ''.join(byte_to_binary(ord(b)) for b in binascii.unhexlify(h))    

def sha256(string_to_hash):
    a=hashlib.sha256(string_to_hash).hexdigest()
    t=hex_to_binary(a)
    return t
cd=0
while cd==0:
    print "1.Registration"
    print "2.Log In"
    print "Select an option"
    db=MySQLdb.connect("localhost","root","","hashnegenc",3306)
    c=db.cursor()
    a=input()
    if a==1:
        print "Enter Name"
        name=raw_input()
        print "Enter Email"
        email=raw_input()
        print "Enter Address"
        address=raw_input()
        print "Enter Username"
        user=raw_input()
        print "Enter Password"
        password=raw_input()
        
        #allPermutations(t)
        sql="select * from tab where username='%s'"%(user)
        c.execute(sql)
        d=c.fetchall()
        if len(d)>0:
          tkMessageBox.showinfo("Error","Username Already Exists")
        else:
             t=sha256(password)
             print t
             re=perms(t)
             encrypted = encrypt(t, t)
             print "Encrypted"
             print encrypted
             c.execute("insert into tab values('"+name+"','"+email+"','"+address+"','"+user+"','"+encrypted+"')")
             db.commit()
    if a==2:
        print "Enter Username"
        user=raw_input()
        print "Enter Password"
        password=raw_input()
        c.execute("select username,password from tab where username='"+user+"';")
        r=c.fetchall()
        if r:
            t=sha256(password)
            print t
            decrypted = decrypt(r[0][1], t)
            print "Decrypted"
            print decrypted
            rek=permret(decrypted)
            
            if t== rek:
                tkMessageBox.showinfo("Login Successful","Successfully Logged in")
            else:
                tkMessageBox.showinfo("Login Failed","Username not found")
        else:
             tkMessageBox.showinfo("Login Failed","Username not found")
    print "Do you want to continue(yes/no)(y/n)(Y/N)"
    res=raw_input()
    if res=='yes' or res=='y' or res=='YES' or res=='Yes'  or res=='Y':
        cd=0
    else:
        cd=1

    
#db.close()
