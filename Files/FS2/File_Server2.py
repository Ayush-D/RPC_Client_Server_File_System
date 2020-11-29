
import os 
import rpyc
import sys
from cryptography.fernet import Fernet
class Request2(rpyc.Service):
    def exposed_checkCredentials(self,k,id,pwd):
        P = self.K.decrypt(self.en)
        O = P.decode('utf-8')
        self.ID = {'AD':('AD','AD2020'),'CS':('CS','CS2020'),'DS':('DS','DS2020')}
        if O == k and self.ID[id][0]==id and self.ID[id][1]==pwd:
            return True
        else:
            return False

    def exposed_task(self,S):
        self.path = os.path.join('Files/')
        self.PathN = os.path.join('Files')
        l = self.K.decrypt(S)
        l = l.decode('utf-8')
        l = l.lower()
        K = l.split()
        
        if len(K)>2:
            #print(K)
            ch = K[0]
            f1 = K[1]
            f2 = K[2]
            if ch == 'cp':
                try:
                    #content = ''
                    #File1 = 
                    #File2 = 
                    File = os.path.abspath(os.getcwd())
                    with open(File+f'/{f1}','rb') as L1:
                        #print('constant1')
                        with open(File+f'/{f2}','w') as L2:
                            #print('constant2')
                            for line in L1:
                                #print('constant3')
                                k = line.strip()
                                k = k.decode('utf-8')
                                L2.write(k)
                except:
                    return self.K.encrypt(bytes(str(FileNotFoundError('There was no file name as '+f'{f1}' )),'utf-8'))
            
            return self.K.encrypt(bytes('Write Complete','utf-8'))



        elif len(K)==2:
            ch = K[0]
            f = K[1]
            if ch == 'cat':
                content = ''
                File1 = os.path.abspath(os.getcwd()) 
                with open(File1+f'/{f}','rb') as L1:
                    for line in L1:
                        k = line.strip()
                        k = k.decode('utf-8')
                        content += k + '\n'
                return self.K.encrypt(bytes(str(content),'utf-8'))
            
        
        else:
            ch = K[0]

            if ch == 'pwd':
                return self.K.encrypt(bytes(str(os.path.abspath(os.getcwd())),'utf-8'))

            elif ch == 'ls':
                return self.K.encrypt(bytes(str(os.listdir(os.path.abspath(os.getcwd()))),'utf-8'))
            
            elif ch == 'exit':
                sys.exit()
        return ' '
    def exposed_reg_file(self,S):
        F = self.K.decrypt(S)
        L = F.decode('utf-8')
        #print(L)
        L = L.lower()
        #L = L.strip()
        #print(L)
        L = L.split(',')
        f1 = L[0]
        f2 = L[1]
        
                #Name = input('Enter the file name you want to register: ')
                #content = input('Enter the content for the file: ')
        File = os.path.abspath(os.getcwd())
        with open(File+f'/{f1}','w') as L2:
            #print('constant2')
            for line in f2.split():
                #print('constant3')
                k = line +' '
                #k = k.decode('utf-8')
                L2.write(k)
        return self.K.encrypt(bytes('File Registered Successfully and data is stored accordingly','utf-8'))
    def exposed_createUser(self,id,pwd):
        if id not in self.ID:
            self.ID[id] = (id,pwd)
        else:
            return 

    def exposed_Share_key1(self):

        self.key = Fernet.generate_key()
        self.K = Fernet(self.key)
        import random
        import string
        self.N = 25
        self.seed1 = 24
        #self.ID ={}
        random.seed(self.seed1)
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k =self.N))
        encrypted_key = self.K.encrypt(bytes(res,'utf-8'))
        #self.id = 'AK'
        #self.pwd = 'AKAM2020' 
        #H = self.K
        self.en = encrypted_key
        return encrypted_key,self.key
    def Share_key2(self):

        self.key = Fernet.generate_key()
        self.K = Fernet(self.key)
        import random
        import string
        self.N = 25
        self.seed2 = 30

        random.seed(self.seed2)
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k =self.N))
        encrypted_key = self.K.encrypt(res)
        self.en2 = encrypted_key
        return encrypted_key
    

if __name__ == '__main__':
    from rpyc.utils.server import ThreadedServer
    T =  ThreadedServer(Request2,port = 8081)
    print('Server Running')
    T.start()