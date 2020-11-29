import rpyc
from cryptography.fernet import Fernet
class My_Service(rpyc.Service):
    def __init__(self):
        pass
    def exposed_connect(self,con):
        self.Port0 = con

    def exposed_disconnect(self):
        pass 
    def exposed_share_key(self,seed,N):
        import random
        import string
        random.seed(seed)
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
        self.Key_auth = res 
        return res
    def exposed_share_key_1(self): 
        File_server_key = Fernet.generate_key()
        
        import random
        import string
        self.N = 25
        self.seed1 = 24
        random.seed(self.seed1)
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = self.N))#kb,kdc
        M = Fernet(File_server_key)
        self.File_server_key = M.encrypt(bytes(res,'utf-8'))
        return self.File_server_key,File_server_key

    def exposed_share_key_2(self): #key for Client Side
        #Client_key = Fernet.generate_key()
        
        import random
        import string
        self.N = 25
        self.seed2 = 30
        random.seed(self.seed2)
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = self.N))
        M = Fernet(res)
        self.Client_key_en = M.encrypt(res) 
        return self.Client_key_en





if __name__ == '__main__':
    from rpyc.utils.server import ThreadedServer
    T =  ThreadedServer(My_Service,port = 8000)
    print('Server Running')
    T.start()
    T.close()
    print('Server stopped')
    
    