ServerPort = ('localhost',8080)
import rpyc
connect = rpyc.connect(ServerPort[0],ServerPort[1])
print('___________________________________MENU_____________________________')
print('Pwd – list the present working directory')
print('ls – list the contents of the file')
print('cp - copy one file to another in the same folder')
print('cat – display contents of the file')
Use = input()

resp = connect.root.task(Use)
print(resp)