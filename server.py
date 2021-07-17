#Madan Bhurtel
#1001752499
#reference link: https://emalsha.wordpress.com/2016/11/24/how-create-http-server-using-python-socket-part-ii/
from socket import *
serverPort = 1000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)


#This following code is the thread that I try to create with the help of online source. When I include this code and execute the program
#I get so many errors so I put this into comment section 
#Reference for this code: https://www.techbeamers.com/python-tutorial-write-multithreaded-python-server/

####                    Hope this helps for some partial credits. Just Trying......          ###
'''
class ServerHelpThread(Thread):      #Serverhelp class
    def run(self): 
        while True : 
            data = conn.recv(2048) 
            print ('Server received data:", data')
            MESSAGE = raw_input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            if MESSAGE == 'exit':
                break
            conn.send(MESSAGE)  # echo 

    def __init__(self,ip_address,port_socket): 
        Thread.__init__(self) 
        self.ip_address = ip_address 
        self.port_socket = port_socket 
        print ('[+] New server socket thread started for " + ip_address+ ":" + str(port_socket)') 
 
while True: 
    serverSocket.listen(4) 
    print('Multithreaded Python server : Waiting for connections from TCP clients...') 
    (conn, (ip_address,port_socket)) = serverSocket.accept() 
    newthread = ServerHelpthread(address,serverSocket) 
    newthread.start() 
    threads.append(newthread) 
'''


while True:
     #we establish the connection
     print('Ready to receive')
     connectionSocket, address = serverSocket.accept()

     #print('Address:',address)     #adresss with connecton socket in them 
     #print('Thread at address and port number: ',address)
     sentence = connectionSocket.recv(1024).decode('utf-8')

     #we split the request from space 
     client_request = []
     client_request = sentence.split(' ')
     data = client_request[0]
     requested_file = client_request[1]     #requested file 
     #printing the requested file 
     print('Client request',requested_file)

     data = requested_file.split('?')[0] # After the "?" symbol not relevent here
     data = data.lstrip('/')   #remove left side / to read the file 
     #if(data ==''):
      #  data = 'test.html' # Load index file 
     try:
        if(data=='tes.html'): 
            response = ''
            redirect = ''
            response = response.encode()
            header = 'HTTP/1.1 301 Moved Permanently\r\n'   
            
            if(data.endswith(".jpg")):         #for images 
                mimetype = 'image/jpg'
            elif(data.endswith(".css")):
                mimetype = 'text/css'
            else:
                mimetype = 'text/html'
            
            
            header += 'Type: '+str(mimetype)+'\r\n'
            
            
            redirect = 'Location: http://localhost:'+str(serverPort) + '/test.html\r\n\r\n' 
            #print(header)
            header = header + redirect
            
            print(header)
        else:
            file = open(data,'rb') # open file read in byte format which is binary mode 
            response = file.read()
            file.close()
        
            header = 'HTTP/1.1 200 OK\n'       #response 200

         


            if(data.endswith(".jpg")):         #for images 
                mimetype = 'image/jpg'
            elif(data.endswith(".css")):
                mimetype = 'text/css'
            else:
                mimetype = 'text/html'
    
            header += 'Type: '+str(mimetype)+'\n\n'
     except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode('utf-8')
     final = header.encode('utf-8')
     final += response
     #print(final.decode('utf-8'))
     connectionSocket.send(final)
     connectionSocket.close()