import socket
import config

#from app_hooks import dict_queues as updateable_dictionaries

try:
    #ServerPort = 2222
    #ServerIP = '10.33.142.235'#'169.254.26.44'
    RPIsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    RPIsocket.bind((config.ServerIP,config.ServerPort))
    RPIsocket.setblocking(False)
except:
    
    pass



def update_queues():

    #This pulls data from the queue
    #print(updateable_dictionaries), if you need more data add a socket check to check if its empty and then continue on!!!!!!!!!!!
    #print(config.dict_queues)
    try:
        bufferSize = 1024
        message, address = RPIsocket.recvfrom(bufferSize)
        readable = message.decode('utf-8')
        print(readable)
    #except:
        #pass
        
        for session in config.dict_queues:
            
            #config.dict_queues[session] = readable
            #config.dict_queues[session].append('readable_data!!')
            config.dict_queues[session].append(readable)
    except:
        print('either buffer empty or socket error in Pull_socket_data')
        pass



        

