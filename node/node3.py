"""import string
import random
#node 1 private key 
N = 25
buffer = 1024
ServerPort = ('localhost',8000)
res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
#import socket
import rpyc

Connect = rpyc.connect(ServerPort[0],ServerPort[1])
#L = Connect(20,10)
Connect.root.connect(ServerPort[0])
Key = Connect.root.share_key(20,25)
print(Key)



K = str.encode(res)"""
import random
import string
from cryptography.fernet import Fernet


import rpyc
P = int(input('Enter the Server Which you Want to connect:'))
FileServerPort = ('localhost',8080)
if P == 1:
    FileServerPort = ('localhost',8080)
if P == 2:
    FileServerPort = ('localhost',8081)
KDC = ('localhost',8000)
connect2 = rpyc.connect(KDC[0],KDC[1])
KDC_var,K1 = connect2.root.share_key_1()
K = Fernet(K1)
connect1 = rpyc.connect(FileServerPort[0],FileServerPort[1])
FS1,M1 = connect1.root.Share_key1()
M = Fernet(M1)
key_KDC = K.decrypt(KDC_var)
id = input('Enter User ID: ')
pw = input('Enter password: ')
#connect1.root.createUser(id,pw)
Flag = connect1.root.checkCredentials(key_KDC.decode('utf-8'),id,pw)
if Flag == False:
    print('Invalid Credentials')
else:
    ch = 'Y'
    while ch!='exit':
        print('___________________________________MENU____________________________________')
        print('Pwd – list the present working directory')
        print('ls – list the contents of the file')
        print('cp - copy one file to another in the same folder')
        print('cat – display contents of the file')
        print('Register - for registering and creating file ')
        print('exit')
        Use = input('>>')
        
        if Use == 'register':
            Name = input('Enter the name')
            content = input('Enter content of the file')
            L = f'{Name},{content}'
            Cn = M.encrypt(bytes(L,'utf-8'))
            respRes = connect1.root.reg_file(Cn)
            respRes = M.decrypt(respRes)
            respRes = respRes.decode('utf-8')
            print('response: ',respRes)
            print('key used: ',key_KDC.decode('utf-8'))
        else:
            U = M.encrypt(bytes(Use,'utf-8'))    
            resp = connect1.root.task(U)


            resp = M.decrypt(resp)
            resp = resp.decode('utf-8')

            print('response: ',resp)
            print('key used: ',key_KDC.decode('utf-8'))
        print()
#S = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
#S.sendto(K,ServerPort)
#M = S.recv(buffer)
#messag1 = "Response from Server: {}".format(M[0])
#print(messag1)
# import os 
# p = os.path.join(<path>)
# File = open(p,'rb+')