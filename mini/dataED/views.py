from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
alphabet="abcdefghijklmnopqrstuvwxyz"
alpha_up="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums="1234567890"
sp_char="@# $%^&*~`.,<>|_-+=({[)}]:;/?"
#print("1.Data_Encryption")
#print("2.Data_Decryption")
#ch=input("Enter your choice as 1 OR 2\n")
def home(request):
    return render(request,'home.html')
def encrypt(request):
    choice=int(request.POST['ch'])
    if(choice==1):
        return render(request,'enc.html',{'choice':choice})
    elif(choice==2):
        return render(request,'dec.html',{'choice':choice})
def resencrypt(request):
    message=request.POST['string']
    key=int(request.POST['key'])
    new_msg=''
    k=key
    while(k>0):
       new_msg=''
       for i in message:
            if(i.isalpha()):
                if(i.isupper()):
                    position=alpha_up.index(i)
                    newpos=(position+key)%26
                    new_msg+=alpha_up[newpos]
                elif(i.islower()):
                    position=alphabet.index(i)
                    newpos=(position+key)%26
                    new_msg+=alphabet[newpos]
            elif(i.isdigit()):
                position=nums.index(i)
                newpos=(position+key)%10
                new_msg+=nums[newpos]
            else:
                position=sp_char.index(i)
                newpos=(position+key)%29
                new_msg+=sp_char[newpos]
       k-=1 
       message=new_msg
    return render(request,'resenc.html',{"new_msg":message})
def resdecrypt(request):
    message=request.POST['string']
    key=int(request.POST['key'])
    original_msg=''
    k=key
    while(k>0):
        original_msg=''
        for i in message:
            if(i.isalpha()):
                if(i.isupper()):
                    position=alpha_up.index(i)
                    newpos=(position-key)%26
                    original_msg+=alpha_up[newpos]
                elif(i.islower()):
                    position=alphabet.index(i)
                    newpos=(position-key)%26
                    original_msg+=alphabet[newpos]
            elif(i.isdigit()):
                position=nums.index(i)
                newpos=(position-key)%10
                original_msg+=nums[newpos]
            else:
                position=sp_char.index(i)
                newpos=(position-key)%29
                original_msg+=sp_char[newpos]
        k-=1
        message=original_msg
    return render(request,'resdec.html',{"original_msg":message})
def home1(request):
    return render(request,'home.html')
def dec(request):
    return render(request,'dec.html')
def home2(request):
    return render(request,'home.html')
def enc(request):
    return render(request,'enc.html')
