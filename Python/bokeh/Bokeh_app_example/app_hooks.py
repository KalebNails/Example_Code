from datetime import datetime
import config
data = 0


#There is most likely a much better way to do this
#This also is probably against convention
#but this is the first dive into my own modules, so this is fine for now


def on_server_loaded(server_context):
    print('This takes place when a server has loaded')




def on_session_created(session_context):
    print('data has been changed')
    global data
    data += 1
    print('Number of sessions' + str(data))
    #print(session_context._id)
    global Add_session
    Add_session = session_context._id
    config.dict_queues[Add_session] = []
    #print(str(config.dict_queues))





def on_session_destroyed(session_context):
    print('session has be terminated!!!!!!!!!!')
    print(session_context._id)
