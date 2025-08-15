# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
import base64
import hashlib
import MySQLdb
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import tkMessageBox
import os
import sys
import binascii
import random
from models import *
from aes import *
import re 
  
def isValid(s): 
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}") 
    return Pattern.match(s) 

 

def sha256(string_to_hash):
    a=hashlib.sha256(string_to_hash).hexdigest()
    print a
    
    t=hex_to_binary(a)
    
    return t
def perms(l):
     k=[]
     #print len(l)
     for i in range(0,len(l),4):
         k.append(l[i:i+4])
         
     print len(k)
     
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
         #print ("".join(s))
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



def index(request):
    return render(request,'signin.html',{})

def login(request):
    return render(request,'signin.html',{})

def page(request):
    return render(request,'signup.html',{})

def otppage(request):
    return render(request,'signotp.html',{})

name,em,address,phone,username,password,otp="","","","","","",""

def newregistration(request):
    global name,em,address,phone,username,password,otp
    if request.method=="POST":
        name=request.POST.get("name")
        em=request.POST.get("email")
        address=request.POST.get("address")
        phone=request.POST.get("phone")
        username=request.POST.get("username")
        password=request.POST.get("password")
        if (isValid(phone)):  
            otp=""
            for i in range(6):
                a=random.randrange(0,10)
                otp+=str(a)
            print('otp: ',otp)
            email = EmailMessage('OTP for your account', 'Your OTP password is '+str(otp), to=[str(em)])
            email.send()
            return HttpResponse("<script>alert('Enter OTP');window.location.href='/otppage/'</script>")
        else:
            return HttpResponse("<script>alert('Some Errors Occured');window.location.href='/page/'</script>")     
    else : 
        return HttpResponse("<script>alert('Invalid Mobile Number');window.location.href='/page/'</script>")
        
        

def registration(request):
    global name,em,address,phone,username,password,otp
    if request.method=="POST":
        givotp=request.POST.get("otp")
        print("OTP: ",givotp)
        if str(givotp)==str(otp):
            print(name,em,address,phone,username,password)
            try:
                ob=reg_tb.objects.get(username=username,email=em)
                return HttpResponse("<script>alert('Duplicate entries found');window.location.href='/login/'</script>")
            except:
                t=sha256(password)
                print ("sha256")
                print (t)
                re=perms(t)
                print ("permutation")
                print (re)
                print ("sha256")
                print (t)
                encrypted = encrypt(re.encode("utf-8"), t.encode("utf-8"))
                
            
                
                print ("Encrypted")
                print (encrypted)
                obj2=reg_tb(name=name,email=em,address=address,phone=phone,username=username,password=encrypted)
                obj2.save()
                return HttpResponse("<script>alert('Successfully Registered');window.location.href='/login/'</script>")
        else:
            return HttpResponse("<script>alert('INCORRECT OTP ');window.location.href='/page/'</script>")
    else:
        return HttpResponse("<script>alert('Try Again');window.location.href='/login/'</script>")

def logincheck(request):
    
    print("login check")
    username=request.POST.get("username")
    password=request.POST.get("password")
    print(username,password)
    #print("else")
    try:
        obj=reg_tb.objects.get(username=username)
        print ("stored password")
        print (obj.password)
        t=sha256(password)
        print ("KEY")
        print (t)
        print (type(t))
        decrypted = decrypt(obj.password, t)
        #print ("Decrypted")
        #print (decrypted)
        
        rek=permrev(decrypted)
        print ("permutation")
        #print rek
        print (type(rek))
        if t== rek:
            request.session["lid"]=obj.username
            return HttpResponse("<script>alert('Login Successfull');window.location.href='/login/'</script>")
        else:
            return HttpResponse("<script>alert('Login Failed');window.location.href='/login/'</script>")
        
        
    except Exception as ex:
        print (ex)
        return HttpResponse("<script>alert('Invalid Login');window.location.href='/login/'</script>")
